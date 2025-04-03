from User import User
from UserDAO import UserDAO

if __name__ == "__main__":
    dao = UserDAO()

    # Thêm user mớicd DAO
    user1 = User("123", "testuser", "test@gmail.com", "0123456789", "hashedpass", "https://avatar.com/test.png")
    user2 = User("124", "testuser", "test2@gmail.com", "0987654321", "hashedpass2", "https://avatar.com/test2.png")
    user3 = User("125", "anotheruser", "test3@gmail.com", "0111222333", "hashedpass3", "https://avatar.com/test3.png")

    dao.add(user1)
    dao.add(user2)
    dao.add(user3)

    # Lấy danh sách user
    print("Danh sách user hiện có:")
    users = dao.getAll()
    for user in users:
        print(user.to_json())

    # Tìm user theo email
    user = dao.findByEmail("test@gmail.com")
    if user:
        print(f"🔍 Đã tìm được user với email 'test@gmail.com': {user.to_json()}")
    else:
        print("❌ Không tìm thấy user!")

    # Tìm user theo username
    users_by_name = dao.findByName("testuser")
    if users_by_name:
        print(f"🔍 Đã tìm được {len(users_by_name)} user có username 'testuser':")
        print([user.to_json() for user in users_by_name])
    else:
        print("❌ Không tìm thấy user!")

    # Tìm user theo số điện thoại
    user_by_phone = dao.findByPhone("0123456789")
    if user_by_phone:
        print(f"📞 Đã tìm được user với số điện thoại '0123456789': {user_by_phone.to_json()}")
    else:
        print("❌ Không tìm thấy user!")

    # Cập nhật user
    updated_user = User("123", "newname", "test@gmail.com", "0987654321", "newpass", "https://newavatar.com/test.png")
    if dao.update("123", updated_user):
        print(f"✅ Đã cập nhật user có ID '123'.")
    else:
        print("❌ Không tìm thấy user để cập nhật!")

    # Xóa user
    if dao.delete("123"):
        print("🗑️ Đã xóa user có ID '123'.")
    else:
        print("❌ Không tìm thấy user để xóa!")
