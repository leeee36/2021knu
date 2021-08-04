# 여러 값을 받는 함수
def people_num(*args):
    print("공부하는 학생 수는? : ", end='')
    result = len(args)
    return result

value = people_num('상욱이', '윤근이', '성찬이', '재현이', '재민이')
print(value,'명')