from datetime import datetime
from colorama import Fore
def export_learning_report(records):
    total_students = len(records)
    passed_students = 0
    failed_students = 0
    for student in records:
        avg_score = sum(student["scores"]) / len(student["scores"])
        if avg_score >= 5.0:
            passed_students += 1
        else:
            failed_students += 1
    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("learning_report.txt", "w", encoding="utf-8") as file:
        file.write("--- BÁO CÁO HỌC TẬP ---\n")
        file.write(f"Thời gian tạo báo cáo: {report_time}\n")
        file.write(f"Tổng số sinh viên: {total_students}\n")
        file.write(f"Số sinh viên đạt yêu cầu: {passed_students}\n")
        file.write(f"Số sinh viên cần cải thiện: {failed_students}\n")
    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed_students}")
    print(f"Số sinh viên cần cải thiện: {failed_students}")
    print(
        Fore.GREEN
        + ">> Đã xuất báo cáo ra file learning_report.txt"
    )