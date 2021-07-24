# for 무작정 따라해보기
for i in range(1, 11):
    if (i%2==0):
     print(i, '은/는 짝수입니다.')
    else:
     print(i, '은/는 홀수입니다.')  

# for 문의 구조
# for i in 범위:
#     반복할 명령어1
#     반복할 명령어2

# 전체 주석처리 : 전체 드래그 후,  ctrl + /

# for문 with list
mylist = ['상욱', '윤근', '재현', '성찬']
for i in mylist:
    print(i)
print('끝')

# print list range
print(list(range(10))) # 시작점 기본값은 일반적으로 0
print(list(range(1,11)))
print(list(range(1,20,2))) # 1부터 19까지 2칸씩 올라감
print(list(range(20,0,-2))) # 20부터 0전까지 2칸씩 내려감 20~2의 짝수 내려가면서 출력

# for문 with range
for i in range(1,11):
    print(i, end=" ") # 숫자 사이에 스페이스바 적용.