import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Shared state for test chaining
user_id = None
post_id = None
comment_id = None


def test_register_user():
    global user_id
    response = client.post("/users", json={
        "fullname": "Alice Test",
        "email": "alice@example.com",
        "password": "password123",
        "bio": "Test user"
    })
    assert response.status_code == 200
    data = response.json()
    user_id = data["id"]
    assert data["fullname"] == "Alice Test"


def test_login():
    response = client.post("/auth/login", params={
        "email": "alice@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.json()


def test_get_current_user():
    response = client.get("/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert data["fullname"] == "Test User"


def test_follow_user():
    response = client.post(f"/users/{user_id}/follow")
    assert response.status_code == 200
    assert "followed" in response.json()["message"]


def test_unfollow_user():
    response = client.delete(f"/users/{user_id}/unfollow")
    assert response.status_code == 200
    assert "unfollowed" in response.json()["message"]


def test_create_post():
    global post_id
    response = client.post("/posts", json={
        "content": "This is a test post!",
        "image_urls": [],
        "video_urls": []
    })
    assert response.status_code == 200
    data = response.json()
    post_id = data["id"]
    assert data["content"] == "This is a test post!"


def test_list_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_comment_post():
    global comment_id
    response = client.post(f"/posts/{post_id}/comments", json={
        "content": "This is a comment"
    })
    assert response.status_code == 200
    data = response.json()
    comment_id = data["id"]
    assert data["content"] == "This is a comment"


def test_get_comments():
    response = client.get(f"/posts/{post_id}/comments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


# Add comment, Repost, Delete post, edit post,..
# Test content of posts, image, video,....