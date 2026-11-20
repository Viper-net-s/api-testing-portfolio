import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    # generous limit: network speed varies, so a strict value makes the test flaky
    assert response.elapsed.total_seconds() < 3

    body = response.json()
    assert body["id"] == 1
    assert "title" in body
    assert isinstance(body["userId"], int)


def test_create_post():
    payload = {"title": "QA test", "body": "Hello", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)

    assert response.status_code == 201
    assert "id" in response.json()


def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/posts/9999", timeout=10)

    assert response.status_code == 404
