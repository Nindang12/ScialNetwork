from Post import Post
from PostDAO import PostDAO
from datetime import datetime

if __name__ == "__main__":
    dao = PostDAO()

    # Thêm post mới
    post1 = Post("123", "Đây là bài post thử nghiệm", ["image1.png"], datetime.now())
    post2 = Post("user_124", "Một bài post thử nghiệm khác", [], datetime.now())
    post3 = Post("user_125", "Thêm một bài post nữa", ["image3.png"], datetime.now())

    # Thêm posts và lưu ID được trả về
    post1_id = dao.add(post1)
    post2_id = dao.add(post2)
    post3_id = dao.add(post3)

    if not post1_id or not post2_id or not post3_id:
        print("❌ Lỗi khi thêm posts!")
        exit(1)

    # Lấy danh sách post
    print("\nDanh sách các post hiện có:")
    posts = dao.get_all()
    for post in posts:
        print(post.to_json())

    # Tìm post theo ID
    found_post = dao.get(post1_id)
    if found_post:
        print(f"\n🔍 Đã tìm được post: {found_post.to_json()}")
    else:
        print("\n❌ Không tìm thấy post!")

    # Cập nhật post
    updated_post = Post("123", "Nội dung đã được cập nhật", ["image1.png"], datetime.now(), post1_id)
    if dao.update(post1_id, updated_post):
        print(f"\n✅ Đã cập nhật post có ID '{post1_id}'")
    else:
        print("\n❌ Không tìm thấy post để cập nhật!")

    # Xóa post
    if dao.delete(post1_id):
        print(f"\n🗑️ Đã xóa post có ID '{post1_id}'")
    else:
        print("\n❌ Không tìm thấy post để xóa!")

    # Thêm like vào post
    if dao.like(post2_id, "user_456"):
        print(f"\n👍 User 'user_456' đã like post '{post2_id}'")
    else:
        print("\n❌ Không thể like post!")

    # Thêm repost vào post
    if dao.repost(post2_id, "user_789"):
        print(f"\n🔁 User 'user_789' đã repost post '{post2_id}'")
    else:
        print("\n❌ Không thể repost post!")
