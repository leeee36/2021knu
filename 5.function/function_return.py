# return이 발생하면 함수 종료
def return_example(a, b):
    if a > b:
        print("상욱이")
        return
    else:
        print("재현이")
    print("윤근이")

return_example(10, 20)
return_example(20, 10)