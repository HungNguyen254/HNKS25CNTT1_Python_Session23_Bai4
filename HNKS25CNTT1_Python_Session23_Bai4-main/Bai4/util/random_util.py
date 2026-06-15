import random
import string
def generate_exercise_code():
    chars = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(chars) for _ in range(4))
    print(f"Mã bài tập của bạn là:PY-{code}") 
