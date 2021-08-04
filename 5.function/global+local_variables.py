# 변수와 인수

# 전역변수와 지역변수의 차이
def add_two_num(a,b):
    print("덧셈 중...")
    result = a + b # 지역변수 result
    return result # 함수 결과값

result = 0 # 전역변수 result
add_two_num(10, 13)
print(result)