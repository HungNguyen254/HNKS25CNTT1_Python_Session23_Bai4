from data.student import student_records
from reports.report_generator import display_student
def main():
    while True:
        print("""
===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====
1. Xem danh sách sinh viên và điểm trung bình
2. Chuẩn hóa tên sinh viên
3. Sinh mã bài tập ngẫu nhiên
4. Xuất báo cáo học tập
5. Thoát chương trình
====================================================  
              """)
        choice = input('Chọn chức năng (1-5):')
        match choice:
            case '1':
                display_student(student_records)
            case '2':
                pass
            case '3':
                pass
                
            case '4':
                pass
                
            case '5':
                break
main()