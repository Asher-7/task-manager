def test_project_crud(auth_client):
    res = auth_client.post("/projects/", json={"name": "Website"})
    assert res.status_code == 201
    project = res.get_json()
    assert project["color"] == "#6366f1"
    assert project["task_count"] == 0

    url = f"/projects/{project['id']}"
    res = auth_client.put(url, json={"name": "Redesign", "color": "#ef4444"})
    assert res.get_json()["name"] == "Redesign"
    assert res.get_json()["color"] == "#ef4444"

    assert len(auth_client.get("/projects/").get_json()["projects"]) == 1
    assert auth_client.delete(url).status_code == 200
    assert auth_client.get(url).status_code == 404


def test_project_requires_name_and_auth(client, auth_client):
    assert auth_client.post("/projects/", json={}).status_code == 400
    client.post("/auth/logout")
    assert client.get("/projects/").status_code == 401


def test_project_detail_includes_tasks(auth_client):
    project = auth_client.post("/projects/", json={"name": "P"}).get_json()
    auth_client.post("/tasks/", json={"title": "t", "project_id": project["id"]})

    body = auth_client.get(f"/projects/{project['id']}").get_json()
    assert [t["title"] for t in body["tasks"]] == ["t"]


def _make_task(client):
    return client.post("/tasks/", json={"title": "t"}).get_json()


def test_comment_lifecycle(auth_client):
    task = _make_task(auth_client)
    base = f"/api/task/{task['id']}/comments"

    assert auth_client.post(base, json={}).status_code == 400

    comment = auth_client.post(base, json={"content": "hello"}).get_json()
    assert comment["username"] == "alice"

    res = auth_client.put(f"/api/comments/{comment['id']}", json={"content": "edited"})
    assert res.get_json()["content"] == "edited"

    assert len(auth_client.get(base).get_json()["comments"]) == 1

    assert auth_client.delete(f"/api/comments/{comment['id']}").status_code == 200
    assert auth_client.get(base).get_json()["comments"] == []

    actions = [a["action"] for a in
               auth_client.get(f"/api/task/{task['id']}/activity").get_json()["activities"]]
    assert {"commented", "comment_updated", "comment_deleted"} <= set(actions)


def test_comments_require_task_ownership(auth_client, app):
    task = _make_task(auth_client)

    other = app.test_client()
    other.post("/auth/register", json={
        "username": "carol", "email": "carol@example.com", "password": "pw",
    })
    res = other.post(f"/api/task/{task['id']}/comments", json={"content": "x"})
    assert res.status_code == 404
