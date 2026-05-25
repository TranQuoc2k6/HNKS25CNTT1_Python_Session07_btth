raw_input = "   nGuyen vaN aN  ;  2004   "

while True:
    print ("""
        ===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
        1. Hiển thị chuỗi dữ liệu gốc
        2. Chuẩn hóa Họ tên và tính Tuổi
        3. Tạo Mã ID và Email tự động
        4. Thoát chương trình
        =====================================
    """)
    choice = input("Nhập lựa chọn của bạn (1-4):")
    print()
    match choice:
        case "1":
            print(f"Chuỗi gốc hiện tại:\n'{raw_input}'")
        case "2":
            new_raw_input = raw_input.strip().split(";")
            full_name = new_raw_input[0].strip().title()
            year_of_birth = int(new_raw_input[1].strip())

            print("[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:")
            print(f"- Họ và tên: {full_name}")
            print(f"- Tuổi hiện tại: {2026 - year_of_birth} tuổi")
        case "3":
            print("""
        ======================================
                  THẺ THÀNH VIÊN MỚI
        ======================================
                """)
            new_raw_input = raw_input.strip().split(";")
            
        case "4":
            print("Chương trình đã dừng!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        