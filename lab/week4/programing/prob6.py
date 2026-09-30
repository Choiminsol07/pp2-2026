# 작성자: 최민솔
# 작성일: 2026.09.30
# 문제: Person 클래스를 작성하시오.

# 클래스: Person
# 인스턴스 변수: name, mobile, office, email

class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        return f"Person(name={self.name}, mobile={self.mobile}, office={self.office}, email={self.email})"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMobile(self, mobile):
        self.mobile = mobile

    def getMobile(self):
        return self.mobile

    def setOffice(self, office):
        self.office = office

    def getOffice(self):
        return self.office

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email


def test_prob2():
    p1 = Person("Choi", office="1234567", email="cms070811cms@naver.com")
    p2 = Person("Min", office="2345678")
    p2.setEmail("cms070811cms@gmail.com")

    print(p1)
    print(p2)


if __name__ == "__main__":
    test_prob2()
