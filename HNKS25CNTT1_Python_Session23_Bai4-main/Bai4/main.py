from data.student import student_records
from reports.report_generator import display_student
from util.string_util import student_name_formats
from util.random_util import generate_exercise_code
from reports.reports import export_learning_report
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
                student_name_formats(student_records)
            case '3':
                generate_exercise_code()
                
            case '4':
                export_learning_report(student_records)
                
            case '5':
                break
main()