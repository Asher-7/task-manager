def test_register_success(client):
    res = client.post("/auth/register", json={
        "username": "bob", "email": "bob@example.com", "password": "pw",
    })
    assert res.status_code == 201
    assert res.get_json()["username"] == "bob"
    assert "password_hash" not in res.get_json()


def test_register_missing_fields(client):
    res = client.post("/auth/register", json={"username": "bob"})
    assert res.status_code == 400


def test_register_duplicate_username(client):
    payload = {"username": "bob", "email": "bob@example.com", "password": "pw"}
    client.post("/auth/register", json=payload)
    res = client.post("/auth/register", json={**payload, "email": "other@example.com"})
    assert res.status_code == 409


def test_register_duplicate_email(client):
    payload = {"username": "bob", "email": "bob@example.com", "password": "pw"}
    client.post("/auth/register", json=payload)
    res = client.post("/auth/register", json={**payload, "username": "other"})
    assert res.status_code == 409


def test_login_success_and_me(client):
    client.post("/auth/register", json={
        "username": "bob", "email": "bob@example.com", "password": "pw",
    })
    client.post("/auth/logout")
    assert client.get("/auth/me").status_code == 401

    res = client.post("/auth/login", json={"username": "bob", "password": "pw"})
    assert res.status_code == 200
    assert client.get("/auth/me").get_json()["username"] == "bob"


def test_login_invalid_credentials(client):
    client.post("/auth/register", json={
        "username": "bob", "email": "bob@example.com", "password": "pw",
    })
    res = client.post("/auth/login", json={"username": "bob", "password": "wrong"})
    assert res.status_code == 401


def test_logout_clears_session(auth_client):
    assert auth_client.get("/auth/me").status_code == 200
    auth_client.post("/auth/logout")
    assert auth_client.get("/auth/me").status_code == 401


def test_list_users_requires_auth(client):
    assert client.get("/auth/users").status_code == 401


def test_list_users_returns_only_id_and_username(auth_client, app):
    other = app.test_client()
    other.post("/auth/register", json={
        "username": "aaron", "email": "aaron@example.com", "password": "pw",
    })

    users = auth_client.get("/auth/users").get_json()["users"]
    assert [u["username"] for u in users] == ["aaron", "alice"]
    assert all(set(u) == {"id", "username"} for u in users)


def test_assign_task_to_listed_user(auth_client, app):
    other = app.test_client()
    other.post("/auth/register", json={
        "username": "aaron", "email": "aaron@example.com", "password": "pw",
    })
    aaron = next(u for u in auth_client.get("/auth/users").get_json()["users"]
                 if u["username"] == "aaron")

    res = auth_client.post("/tasks/", json={"title": "t", "assigned_to": aaron["id"]})
    assert res.status_code == 201
    assert res.get_json()["assigned_to"] == aaron["id"]
