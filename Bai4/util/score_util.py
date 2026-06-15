def score_caculate(scores):
    avg_score = sum(scores)/3
    if avg_score >= 8.0:
        status = 'Giỏi'
    elif 6.5<= avg_score < 8.0:
        status = 'Khá'
    elif 5.0 <= avg_score < 6.5:
        stautus = 'Trung bình'
    else:
        status = 'Yếu'
    return avg_score,status