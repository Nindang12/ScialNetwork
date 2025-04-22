from flask import Flask, request, jsonify, abort
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = Flask(__name__)

users = {}
posts = {}
comments = {}
followers = {}

class UserBase(BaseModel):
    fullname: str
    email: str
    bio: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str

class PostCreate(BaseModel):
    content: str
    image_urls: Optional[List[str]] = []
    video_urls: Optional[List[str]] = []

class Post(PostCreate):
    id: str
    user_id: str

class CommentCreate(BaseModel):
    content: str

class Comment(CommentCreate):
    id: str
    user_id: str
    post_id: str

@app.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    for uid, user in users.items():
        if user['email'] == email and user['password'] == password:
            return jsonify({"token": f"mock-token-for-{uid}"})
    abort(401, "Invalid credentials")

@app.route("/auth/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logged out"})

@app.route("/auth/me", methods=["GET"])
def get_current_user():
    return jsonify({"id": "mock-user", "fullname": "Test User"})

@app.route("/users", methods=["POST"])
def register_user():
    data = request.get_json()
    user_id = str(uuid4())
    user = UserCreate(**data, id=user_id)
    users[user_id] = user.dict()
    return jsonify({**user.dict(), "id": user_id})

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        abort(404, "User not found")
    return jsonify({**users[user_id], "id": user_id})

@app.route("/users/<user_id>/follow", methods=["POST"])
def follow_user(user_id):
    followers.setdefault(user_id, []).append("mock-user")
    return jsonify({"message": f"You followed {user_id}"})

@app.route("/users/<user_id>/unfollow", methods=["DELETE"])
def unfollow_user(user_id):
    followers.get(user_id, []).remove("mock-user")
    return jsonify({"message": f"You unfollowed {user_id}"})

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    post_id = str(uuid4())
    post = PostCreate(**data, id=post_id, user_id="mock-user")
    posts[post_id] = post.dict()
    return jsonify({**post.dict(), "id": post_id, "user_id": "mock-user"})

@app.route("/posts", methods=["GET"])
def list_posts():
    return jsonify([
        {"id": pid, "user_id": "mock-user", **data}
        for pid, data in posts.items()
    ])

@app.route("/posts/<post_id>/comments", methods=["POST"])
def add_comment(post_id):
    data = request.get_json()
    comment_id = str(uuid4())
    comment = CommentCreate(**data, id=comment_id, user_id="mock-user", post_id=post_id)
    comments[comment_id] = comment.dict()
    return jsonify({
        "id": comment_id,
        "user_id": "mock-user",
        "post_id": post_id,
        **comment.dict()
    })

@app.route("/posts/<post_id>/comments", methods=["GET"])
def get_comments(post_id):
    return jsonify([
        {"id": cid, "user_id": "mock-user", "post_id": post_id, **c}
        for cid, c in comments.items() if c['post_id'] == post_id
    ])

if __name__ == "__main__":
    app.run(debug=True)

# Authentication.....

