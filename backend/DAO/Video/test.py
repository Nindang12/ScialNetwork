from datetime import datetime
from Video import Video
from VideoDAO import VideoDAO


def print_error(message):
    print(f"❌ Lỗi: {message}")

def print_success(message):
    print(f"✅ Thành công: {message}")


if __name__ == "__main__":
    dao = VideoDAO()

    # Thêm video mới
    video1 = Video(user_id="123", post_id="001", url="https://example.com/video1.mp4", comment_id=None, uploaded_at=datetime.now())
    video2 = Video(user_id="124", post_id="002", url="https://example.com/video2.mp4", comment_id="789", uploaded_at=datetime.now())
    video3 = Video(user_id="125", post_id="003", url="https://example.com/video3.mp4", comment_id=None, uploaded_at=datetime.now())

    if dao.add(video1):
        print_success("Đã thêm video 1.")
    else:
        print_error("Không thể thêm video 1.")

    if dao.add(video2):
        print_success("Đã thêm video 2.")
    else:
        print_error("Không thể thêm video 2.")

    if dao.add(video3):
        print_success("Đã thêm video 3.")
    else:
        print_error("Không thể thêm video 3.")

    # Lấy tất cả các video
    videos = dao.get_all()
    if videos:
        print_success("Lấy tất cả video thành công.")
        for video in videos:
            print(video.to_json())
    else:
        print_error("Không tìm thấy video nào.")

    # Lấy video theo ID
    if video1.video_id is not None:
        video = dao.get(video1.video_id)
        if video:
            print_success("Đã tìm được video theo ID.")
            print(video.to_json())
        else:
            print_error("Không tìm thấy video theo ID đã cho.")
    else:
        print_error("ID của video 1 không hợp lệ.")

    # # Lấy video theo post_id
    # videos_by_post = dao.get_by_post("001")
    # if videos_by_post:
    #     print_success("Đã tìm thấy video theo post_id.")
    #     print([video.to_json() for video in videos_by_post])
    # else:
    #     print_error("Không tìm thấy video nào với post_id đã cho.")

    # # Lấy video theo comment_id
    # videos_by_comment = dao.get_by_comment("789")
    # if videos_by_comment:
    #     print_success("Đã tìm thấy video theo comment_id.")
    #     print([video.to_json() for video in videos_by_comment])
    # else:
    #     print_error("Không tìm thấy video nào với comment_id đã cho.")

    # # Cập nhật video
    # updated_video = Video(user_id="123", post_id="001", url="https://example.com/video1_updated.mp4", comment_id=None, uploaded_at=datetime.now())
    
    # if video1.video_id is not None and dao.update(video1.video_id, updated_video):
    #     print_success("Đã cập nhật video 1.")
    # else:
    #     print_error("Không tìm thấy video để cập nhật!")

