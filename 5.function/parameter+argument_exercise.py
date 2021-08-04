# 매개변수 기본값 바꿔주기
def add_two_num(a=100, b=200): # 매개변수
    print("덧셈 중...")
    print(a, b)
    result = a + b
    return result

value1 = add_two_num() # 인수
value2 = add_two_num(10, 30)
value3 = add_two_num(10)
value4 = add_two_num(b=20)
print(value1, value2, value3, value4)