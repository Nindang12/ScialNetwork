from datetime import datetime
from Image import Image
from ImageDAO import ImageDAO


def print_error(message):
    print(f"❌ Lỗi: {message}")


def print_success(message):
    print(f"✅ Thành công: {message}")


if __name__ == "__main__":
    dao = ImageDAO()

    # Thêm image mới
    image1 = Image(user_id="123", post_id="001", url="https://example.com/image1.png", comment_id=None, uploaded_at=datetime.now())
    image2 = Image(user_id="124", post_id="002", url="https://example.com/image2.png", comment_id="789", uploaded_at=datetime.now())
    image3 = Image(user_id="125", post_id="003", url="https://example.com/image3.png", comment_id=None, uploaded_at=datetime.now())

    if dao.add(image1):
        print_success("Đã thêm ảnh 1.")
    else:
        print_error("Không thể thêm ảnh 1.")

    if dao.add(image2):
        print_success("Đã thêm ảnh 2.")
    else:
        print_error("Không thể thêm ảnh 2.")

    if dao.add(image3):
        print_success("Đã thêm ảnh 3.")
    else:
        print_error("Không thể thêm ảnh 3.")

    # Lấy tất cả các ảnh
    images = dao.get_all()
    if images:
        print_success("Lấy tất cả ảnh thành công.")
        for image in images:
            print(image.to_json())
    else:
        print_error("Không tìm thấy ảnh nào.")

    # Lấy ảnh theo ID
    image = dao.get(image1.image_id)
    if image:
        print_success("Đã tìm được ảnh theo ID.")
        print(image.to_json())
    else:
        print_error("Không tìm thấy ảnh theo ID đã cho.")

    # Lấy ảnh theo post_id
    images_by_post = dao.get_by_post("001")
    if images_by_post:
        print_success("Đã tìm thấy ảnh theo post_id.")
        print([img.to_json() for img in images_by_post])
    else:
        print_error("Không tìm thấy ảnh nào với post_id đã cho.")

    # Lấy ảnh theo comment_id
    images_by_comment = dao.get_by_comment("None")
    if images_by_comment:
        print_success("Đã tìm thấy ảnh theo comment_id.")
        print([img.to_json() for img in images_by_comment])
    else:
        print_error("Không tìm thấy ảnh nào với comment_id đã cho.")

    # Cập nhật ảnh
    updated_image = Image(user_id="123", post_id="001", url="https://example.com/image1_updated.png", comment_id=None, uploaded_at=datetime.now())
    if dao.update(image1.image_id, updated_image):
        print_success("Đã cập nhật ảnh 1.")
    else:
        print_error("Không tìm thấy ảnh để cập nhật!")
