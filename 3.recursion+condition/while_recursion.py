# # for 와 while 의 차이
# for 문은 정해진 횟수만큼 돌린다
# while 문은 정해진 목표까지 돌린다 -> 조건이 참인 경우

# while 문의 기초
it = 0
while it < 5:
    it += 1
    print(it)


# # while 문의 구조
# while 조건 :
#     반복할 명령어 1
#     반복할 명령어 2


# while 무한루프 , 종료 시 ctrl + c
it = 0
while True:
    it += 1
    print(it)


# while 무한루프 + break
ik = 0
while True:
    ik += 1
    print(ik)
    if ik > 500:
        break