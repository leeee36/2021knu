# class_example_fishbread_underbar_variable.py
# 클래스 -> 붕어빵 틀 만들기
class FishBread :
    # 클래스 변수
    banjook = '밀가루'
    # 메소드 만들기
    # 붕어빵 굽기
    def make_fb(self, ingredients, price) :
        self.__ingredients = ingredients
        self.__price = price

    # 붕어빵 살펴보기
    def see_fb(self) :
        print(self.__ingredients, self.__price)

# 객체(인스턴스) 만들기 -> 붕어빵 만들기
a = FishBread()
a.make_fb('팥', 400)
print(a.__ingredients, a.__price) # same  as  a.see_fb()
a.__price = 10
a.see_fb()

# 결과 : def_make_fb 안에는 ingredients가 있지만, 없는 속성이라고 뜸 : 접근 권한이 없다는 뜻