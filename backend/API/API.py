from fastapi import FastAPI, Depends, HTTPException, status, Path
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI(title="LOOM Social Network API")

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

@app.post("/auth/login")
def login(email: str, password: str):
    for uid, user in users.items():
        if user['email'] == email:
            return {"token": f"mock-token-for-{uid}"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/auth/logout")
def logout():
    return {"message": "Logged out"}

@app.get("/auth/me")
def get_current_user():
    return {"id": "mock-user", "fullname": "Test User"}

@app.post("/users", response_model=User)
def register_user(user: UserCreate):
    user_id = str(uuid4())
    users[user_id] = user.dict()
    return {**user.dict(), "id": user_id}


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str = Path(...)):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return {**users[user_id], "id": user_id}


@app.post("/users/{user_id}/follow")
def follow_user(user_id: str):
    followers.setdefault(user_id, []).append("mock-user")
    return {"message": f"You followed {user_id}"}


@app.delete("/users/{user_id}/unfollow")
def unfollow_user(user_id: str):
    followers.get(user_id, []).remove("mock-user")
    return {"message": f"You unfollowed {user_id}"}


@app.post("/posts", response_model=Post)
def create_post(post: PostCreate):
    post_id = str(uuid4())
    posts[post_id] = post.dict()
    return {**post.dict(), "id": post_id, "user_id": "mock-user"}


@app.get("/posts", response_model=List[Post])
def list_posts():
    return [
        {"id": pid, "user_id": "mock-user", **data}
        for pid, data in posts.items()
    ]


@app.post("/posts/{post_id}/comments", response_model=Comment)
def add_comment(post_id: str, comment: CommentCreate):
    comment_id = str(uuid4())
    comments[comment_id] = comment.dict()
    return {
        "id": comment_id,
        "user_id": "mock-user",
        "post_id": post_id,
        **comment.dict()
    }


@app.get("/posts/{post_id}/comments", response_model=List[Comment])
def get_comments(post_id: str):
    return [
        {"id": cid, "user_id": "mock-user", "post_id": post_id, **c}
        for cid, c in comments.items()
    ]

#