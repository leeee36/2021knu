class Student :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def __str__(self) :
        return '안녕하세요, 저는 {}이고, 학생입니다.'.format(self.name)

class EStudent(Student) :
    def __str__(self) :
        return '안녕하세요 저는 {}이고, 초등학생입니다.'.format(self.name)

    def print_age(self) :
        print('{}의 나이는 {}살 입니다.'.format(self.name, self.age))
    
class MStudent(EStudent) :
    def __str__(self) :
        return '안녕하세요 저는 {}이고, 중학생입니다.'.format(self.name)

sangwook = Student('상욱이', 5)
sungchan = EStudent('성찬이', 12)
jaehyun = MStudent('재현이', 16)

print(sangwook)
print(sungchan)
print(jaehyun)

# sangwook.print_age()
sungchan.print_age()
jaehyun.print_age()
