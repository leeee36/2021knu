cur_tem = 20
def set_tem(des_tem):
    global cur_tem
    if cur_tem < int(des_tem) :
        while True :
            cur_tem += 1
            print(f"현재 온도는 {cur_tem}도 입니다.")
            if cur_tem == int(des_tem) :
                break
    if cur_tem > int(des_tem) :
        while True :
            cur_tem -= 1
            print(f"현재 온도는 {cur_tem}도 입니다.")
            if cur_tem == int(des_tem) :
                break

print("에어컨을 작동합니다.")
while True :
    des_tem = input('원하는 온도를 설정해 주세요. : ')
    if des_tem == '종료':
        break
    if int(des_tem) >= 18 and int(des_tem) <= 30 :
        if int(des_tem) == 20:
            print("현재 온도는 20도 입니다.")
        set_tem(des_tem)
    elif int(des_tem) < 18 or int(des_tem) > 30 :
        print("입력을 확인해 주세요.")
print("에어컨을 종료합니다.")