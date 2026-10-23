def make_task(client, **overrides):
    payload = {"title": "Write docs"}
    payload.update(overrides)
    res = client.post("/tasks/", json=payload)
    assert res.status_code == 201
    return res.get_json()


def test_requires_authentication(client):
    assert client.get("/tasks/").status_code == 401
    assert client.post("/tasks/", json={"title": "x"}).status_code == 401
    assert client.get("/tasks/stats").status_code == 401


def test_create_task_defaults(auth_client):
    task = make_task(auth_client)
    assert task["status"] == "todo"
    assert task["priority"] == "medium"
    assert task["completed_at"] is None


def test_create_task_validation(auth_client):
    assert auth_client.post("/tasks/", json={}).status_code == 400
    assert auth_client.post("/tasks/", json={"title": "x", "status": "bogus"}).status_code == 400
    assert auth_client.post("/tasks/", json={"title": "x", "priority": "bogus"}).status_code == 400


def test_get_update_delete_task(auth_client):
    task = make_task(auth_client)
    url = f"/tasks/{task['id']}"

    assert auth_client.get(url).get_json()["title"] == "Write docs"

    res = auth_client.put(url, json={"priority": "urgent", "status": "done"})
    assert res.status_code == 200
    body = res.get_json()
    assert body["priority"] == "urgent"
    assert body["completed_at"] is not None

    res = auth_client.put(url, json={"status": "todo"})
    assert res.get_json()["completed_at"] is None

    assert auth_client.delete(url).status_code == 200
    assert auth_client.get(url).status_code == 404


def test_update_logs_activity(auth_client):
    task = make_task(auth_client)
    auth_client.put(f"/tasks/{task['id']}", json={"priority": "high"})

    res = auth_client.get(f"/api/task/{task['id']}/activity")
    actions = [(a["action"], a["field_name"]) for a in res.get_json()["activities"]]
    assert ("created", None) in actions
    assert ("updated", "priority") in actions


def test_list_filters(auth_client):
    make_task(auth_client, title="a", status="todo", priority="low")
    make_task(auth_client, title="b", status="done", priority="high")
    make_task(auth_client, title="c", status="done", priority="low")

    def titles(query):
        res = auth_client.get(f"/tasks/{query}")
        return sorted(t["title"] for t in res.get_json()["tasks"])

    assert titles("") == ["a", "b", "c"]
    assert titles("?status=done") == ["b", "c"]
    assert titles("?priority=low") == ["a", "c"]
    assert titles("?status=done&priority=low") == ["c"]


def test_search_matches_title_and_description(auth_client):
    make_task(auth_client, title="Fix login bug")
    make_task(auth_client, title="Write report", description="Quarterly LOGIN metrics")
    make_task(auth_client, title="Buy milk")

    def titles(query):
        res = auth_client.get(f"/tasks/?q={query}")
        return sorted(t["title"] for t in res.get_json()["tasks"])

    assert titles("login") == ["Fix login bug", "Write report"]
    assert titles("milk") == ["Buy milk"]
    assert titles("nothing") == []


def test_search_combines_with_filters(auth_client):
    make_task(auth_client, title="Fix login bug", status="done")
    make_task(auth_client, title="Improve login page", status="todo")

    res = auth_client.get("/tasks/?q=login&status=done")
    assert [t["title"] for t in res.get_json()["tasks"]] == ["Fix login bug"]


def test_search_treats_wildcards_literally(auth_client):
    make_task(auth_client, title="100% done")
    make_task(auth_client, title="Something else")

    res = auth_client.get("/tasks/?q=%25")
    assert [t["title"] for t in res.get_json()["tasks"]] == ["100% done"]


def test_tasks_are_private_to_creator(auth_client, app):
    task = make_task(auth_client)

    other = app.test_client()
    other.post("/auth/register", json={
        "username": "carol", "email": "carol@example.com", "password": "pw",
    })
    assert other.get(f"/tasks/{task['id']}").status_code == 404
    assert other.get("/tasks/").get_json()["total"] == 0


def test_stats(auth_client):
    make_task(auth_client, status="done", priority="high")
    make_task(auth_client, status="todo", priority="low", due_date="2000-01-01T00:00:00")

    stats = auth_client.get("/tasks/stats").get_json()
    assert stats["total"] == 2
    assert stats["by_status"]["done"] == 1
    assert stats["by_priority"]["high"] == 1
    assert stats["overdue"] == 1
    assert stats["completion_rate"] == 50.0
