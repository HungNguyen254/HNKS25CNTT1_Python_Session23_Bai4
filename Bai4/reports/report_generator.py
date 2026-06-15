from util.score_util import score_caculate
def display_student(list):
    count = 0
    print('--Danh sách điểm sinh viên--')
    for i in list:
        avg_score,status =  score_caculate(i['scores'])
        print(f'{count + 1}.[{i['student_id']}] {i['name']} | Điểm:{i['scores']} | ĐTB: {avg_score} - {status}')