# 매개변수와 인수의 차이를 알아보자

def add_two_num(a,b): # 매개변수
    print("덧셈 중...")
    result = a + b
    return result

a = 10
b = 12

value = add_two_num(a, b) # 인수
print(value)