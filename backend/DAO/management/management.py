from DAO.User import UserDAO
from DAO.Post import PostDAO
from DAO.Comment import CommentDAO
from DAO.Image import ImageDAO
from DAO.Video import VideoDAO
from config import MONGODB_URL, MONGODB_DB_NAME
from pymongo import MongoClient

class Management:
    @staticmethod
    def _get_db():
        client = MongoClient(MONGODB_URL)
        db = client[MONGODB_DB_NAME]
        return db

    @staticmethod
    def _get_daos():
        db = Management._get_db()
        return {
            'user': UserDAO(db),
            'post': PostDAO(db),
            'comment': CommentDAO(db),
            'image': ImageDAO(db),
            'video': VideoDAO(db)
        }

    # User functions
    @staticmethod
    def get_all_users():
        daos = Management._get_daos()
        return daos['user'].getAll()

    @staticmethod
    def get_user(userID: str):
        daos = Management._get_daos()
        return daos['user'].get(userID)

    @staticmethod
    def find_user_by_email(email: str):
        daos = Management._get_daos()
        return daos['user'].findByEmail(email)

    @staticmethod
    def create_user(data: dict):
        daos = Management._get_daos()
        user_obj = daos['user'].model_class(**data)
        daos['user'].add(user_obj)

    @staticmethod
    def update_user(userID: str, data: dict):
        daos = Management._get_daos()
        user_obj = daos['user'].model_class(**data)
        return daos['user'].update(userID, user_obj)

    @staticmethod
    def delete_user(userID: str):
        daos = Management._get_daos()
        return daos['user'].delete(userID)

    # Post functions
    @staticmethod
    def get_all_posts():
        daos = Management._get_daos()
        return daos['post'].getAll()

    @staticmethod
    def get_post(postID: str):
        daos = Management._get_daos()
        return daos['post'].get(postID)

    @staticmethod
    def create_post(data: dict):
        daos = Management._get_daos()
        post_obj = daos['post'].model_class(**data)
        daos['post'].add(post_obj)

    @staticmethod
    def update_post(postID: str, data: dict):
        daos = Management._get_daos()
        post_obj = daos['post'].model_class(**data)
        return daos['post'].update(postID, post_obj)

    @staticmethod
    def delete_post(postID: str):
        daos = Management._get_daos()
        return daos['post'].delete(postID)

    @staticmethod
    def like_post(postID: str, userID: str):
        daos = Management._get_daos()
        return daos['post'].like(postID, userID)

    @staticmethod
    def repost_post(postID: str, userID: str):
        daos = Management._get_daos()
        return daos['post'].repost(postID, userID)

    # Comment functions
    @staticmethod
    def get_all_comments():
        daos = Management._get_daos()
        return daos['comment'].getAll()

    @staticmethod
    def get_comment(commentID: str):
        daos = Management._get_daos()
        return daos['comment'].get(commentID)

    @staticmethod
    def get_comments_by_post(postID: str):
        daos = Management._get_daos()
        return daos['comment'].getByPost(postID)

    @staticmethod
    def add_comment(data: dict):
        daos = Management._get_daos()
        comment_obj = daos['comment'].model_class(**data)
        daos['comment'].add(comment_obj)

    @staticmethod
    def update_comment(commentID: str, data: dict):
        daos = Management._get_daos()
        comment_obj = daos['comment'].model_class(**data)
        return daos['comment'].update(commentID, comment_obj)

    @staticmethod
    def delete_comment(commentID: str):
        daos = Management._get_daos()
        return daos['comment'].delete(commentID)

    @staticmethod
    def like_comment(commentID: str, userID: str):
        daos = Management._get_daos()
        return daos['comment'].like(commentID, userID)

    # Image functions
    @staticmethod
    def get_all_images():
        daos = Management._get_daos()
        return daos['image'].getAll()

    @staticmethod
    def get_image(imageID: str):
        daos = Management._get_daos()
        return daos['image'].get(imageID)

    @staticmethod
    def get_images_by_post(postID: str):
        daos = Management._get_daos()
        return daos['image'].getByPost(postID)

    @staticmethod
    def upload_image(data: dict):
        daos = Management._get_daos()
        image_obj = daos['image'].model_class(**data)
        daos['image'].add(image_obj)

    @staticmethod
    def update_image(imageID: str, data: dict):
        daos = Management._get_daos()
        image_obj = daos['image'].model_class(**data)
        return daos['image'].update(imageID, image_obj)

    # Video functions
    @staticmethod
    def get_all_videos():
        daos = Management._get_daos()
        return daos['video'].getAll()

    @staticmethod
    def get_video(videoID: str):
        daos = Management._get_daos()
        return daos['video'].get(videoID)

    @staticmethod
    def get_videos_by_post(postID: str):
        daos = Management._get_daos()
        return daos['video'].getByPost(postID)

    @staticmethod
    def upload_video(data: dict):
        daos = Management._get_daos()
        video_obj = daos['video'].model_class(**data)
        daos['video'].add(video_obj)

    @staticmethod
    def update_video(videoID: str, data: dict):
        daos = Management._get_daos()
        video_obj = daos['video'].model_class(**data)
        return daos['video'].update(videoID, video_obj)

    @staticmethod
    def delete_video(videoID: str):
        daos = Management._get_daos()
        return daos['video'].delete(videoID)
