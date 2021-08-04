# 두 수를 입력받아 두 수의 차이를 구하는 프로그램

a = input("첫 번째 수를 입력하세요.:")
b = input("두 번째 수를 입력하세요.:")

if a > b:
    result = int(a) - int(b)
else:
    result = int(b) - int(a)

print(result)