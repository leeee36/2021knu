# 클래스 -> 붕어빵 틀 만들기
class FishBread :
    # 메소드 만들기
    # 붕어빵 굽기
    def make_fb(self, ingredients, price) :
        self.ingredients = ingredients
        self.price = price

    # 붕어빵 살펴보기
    def see_fb(self) :
        print(self.ingredients, self.price)
        

# 객체(인스턴스) 만들기 -> 붕어빵 만들기
a = FishBread()
b = FishBread()

a.make_fb('팥', 300)
b.make_fb('슈크림', 500)
a.see_fb()
b.see_fb()
