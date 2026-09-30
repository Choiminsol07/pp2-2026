# 작성자 : 최민솔
# 작성일 : 2026.9.30
# 문제 : 고양이를 클래스로 정의하고 몇개의 인스턴스를 생성해보자. 접근자와 설정자를 사용해보자.

# 클래스명 : Cat
# 인스턴스 변수 : name, age

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


def test_prob1():

    missy = Cat("Missy", 3)
    lucky = Cat("Lucky", 5)

    print(missy)
    print(lucky)

    print(missy.getName())
    print(missy.getAge())
    
    missy.setName("Mimi")
    missy.setAge(4)

    print(missy)


if __name__ == "__main__":
    test_prob1()