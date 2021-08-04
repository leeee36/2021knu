# 클래스 -> 붕어빵 틀 만들기
class FishBread :
    # 클래스 변수
    banjook = '밀가루'
    # 메소드 만들기
    # 붕어빵 굽기
    def make_fb(self, ingredients, price) :
        self.ingredients = ingredients
        self.price = price

    # 붕어빵 살펴보기
    def see_fb(self) :
        print(self.ingredients, self.price)

    # 클래스 메소드
    def see_banjook(cls) :
        print(cls.banjook)    

# 객체(인스턴스) 만들기 -> 붕어빵 만들기
a = FishBread()
b = FishBread()

a.see_banjook()
b.see_banjook()
FishBread.banjook = '콩가루'
a.see_banjook()
b.see_banjook()