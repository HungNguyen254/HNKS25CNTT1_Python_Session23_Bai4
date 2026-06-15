def student_name_formats(list):
    for i in list:
        print(f'{i['student_id']}: {' '.join(i['name'].strip().split()).title()}')
    print('>> Đã chuẩn hóa toàn bộ tên sinh viên.')