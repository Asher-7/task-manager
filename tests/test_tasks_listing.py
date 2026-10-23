from datetime import datetime, timedelta


def make_task(client, **overrides):
    payload = {"title": "task"}
    payload.update(overrides)
    res = client.post("/tasks/", json=payload)
    assert res.status_code == 201
    return res.get_json()


def titles(client, query=""):
    res = client.get(f"/tasks/{query}")
    assert res.status_code == 200
    return [t["title"] for t in res.get_json()["tasks"]]


def days_from_now(days):
    return (datetime.utcnow() + timedelta(days=days)).isoformat()


# ---------- sorting ----------

def test_default_order_is_newest_first(auth_client):
    for name in ("first", "second", "third"):
        make_task(auth_client, title=name)
    assert titles(auth_client) == ["third", "second", "first"]


def test_sort_by_title(auth_client):
    for name in ("banana", "apple", "cherry"):
        make_task(auth_client, title=name)
    assert titles(auth_client, "?sort_by=title&order=asc") == ["apple", "banana", "cherry"]
    assert titles(auth_client, "?sort_by=title&order=desc") == ["cherry", "banana", "apple"]


def test_sort_by_priority_uses_severity_not_alphabet(auth_client):
    for name, priority in (("m", "medium"), ("u", "urgent"), ("l", "low"), ("h", "high")):
        make_task(auth_client, title=name, priority=priority)
    assert titles(auth_client, "?sort_by=priority&order=desc") == ["u", "h", "m", "l"]
    assert titles(auth_client, "?sort_by=priority&order=asc") == ["l", "m", "h", "u"]


def test_sort_by_due_date_puts_missing_dates_last(auth_client):
    make_task(auth_client, title="later", due_date=days_from_now(5))
    make_task(auth_client, title="none")
    make_task(auth_client, title="sooner", due_date=days_from_now(1))
    assert titles(auth_client, "?sort_by=due_date&order=asc") == ["sooner", "later", "none"]
    assert titles(auth_client, "?sort_by=due_date&order=desc") == ["later", "sooner", "none"]


def test_invalid_sort_params_rejected(auth_client):
    assert auth_client.get("/tasks/?sort_by=password").status_code == 400
    assert auth_client.get("/tasks/?order=sideways").status_code == 400


# ---------- pagination ----------

def test_no_pagination_params_keeps_original_response_shape(auth_client):
    make_task(auth_client)
    body = auth_client.get("/tasks/").get_json()
    assert set(body) == {"total", "tasks"}


def test_pagination_splits_results(auth_client):
    for i in range(5):
        make_task(auth_client, title=f"t{i}")

    page1 = auth_client.get("/tasks/?sort_by=title&order=asc&page=1&per_page=2").get_json()
    assert page1["total"] == 5
    assert page1["pages"] == 3
    assert [t["title"] for t in page1["tasks"]] == ["t0", "t1"]

    page3 = auth_client.get("/tasks/?sort_by=title&order=asc&page=3&per_page=2").get_json()
    assert [t["title"] for t in page3["tasks"]] == ["t4"]


def test_page_beyond_the_end_is_empty(auth_client):
    make_task(auth_client)
    body = auth_client.get("/tasks/?page=9&per_page=10").get_json()
    assert body["tasks"] == []
    assert body["total"] == 1


def test_per_page_alone_defaults_to_first_page(auth_client):
    for i in range(3):
        make_task(auth_client, title=f"t{i}")
    body = auth_client.get("/tasks/?per_page=2").get_json()
    assert body["page"] == 1
    assert len(body["tasks"]) == 2


def test_pagination_works_with_filters(auth_client):
    for i in range(4):
        make_task(auth_client, title=f"done{i}", status="done")
    make_task(auth_client, title="open", status="todo")

    body = auth_client.get("/tasks/?status=done&per_page=3").get_json()
    assert body["total"] == 4
    assert body["pages"] == 2
    assert len(body["tasks"]) == 3


def test_invalid_pagination_params_rejected(auth_client):
    assert auth_client.get("/tasks/?page=0").status_code == 400
    assert auth_client.get("/tasks/?per_page=0").status_code == 400
    assert auth_client.get("/tasks/?per_page=101").status_code == 400


# ---------- due soon ----------

def test_due_soon_requires_auth(client):
    assert client.get("/tasks/due-soon").status_code == 401


def test_due_soon_includes_overdue_and_upcoming_sorted(auth_client):
    make_task(auth_client, title="overdue", due_date=days_from_now(-2))
    make_task(auth_client, title="tomorrow", due_date=days_from_now(1))
    make_task(auth_client, title="next-month", due_date=days_from_now(30))
    make_task(auth_client, title="no-date")

    body = auth_client.get("/tasks/due-soon").get_json()
    assert [t["title"] for t in body["tasks"]] == ["overdue", "tomorrow"]
    assert body["total"] == 2
    assert body["days"] == 7


def test_due_soon_excludes_done_tasks(auth_client):
    make_task(auth_client, title="finished", status="done", due_date=days_from_now(1))
    make_task(auth_client, title="open", due_date=days_from_now(1))

    body = auth_client.get("/tasks/due-soon").get_json()
    assert [t["title"] for t in body["tasks"]] == ["open"]


def test_due_soon_days_parameter(auth_client):
    make_task(auth_client, title="in-10-days", due_date=days_from_now(10))

    assert auth_client.get("/tasks/due-soon?days=3").get_json()["total"] == 0
    assert auth_client.get("/tasks/due-soon?days=14").get_json()["total"] == 1


def test_due_soon_invalid_days_rejected(auth_client):
    assert auth_client.get("/tasks/due-soon?days=0").status_code == 400
    assert auth_client.get("/tasks/due-soon?days=366").status_code == 400


def test_due_soon_only_shows_own_tasks(auth_client, app):
    make_task(auth_client, title="mine", due_date=days_from_now(1))

    other = app.test_client()
    other.post("/auth/register", json={
        "username": "carol", "email": "carol@example.com", "password": "pw",
    })
    assert other.get("/tasks/due-soon").get_json()["total"] == 0
