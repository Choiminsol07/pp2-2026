# 작성자: 최민솔
# 작성일: 2026.09.30
# 문제: 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성하시오.

#클래스: PhoneBook
#인스턴스 변수: contacts

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def __str__(self):
        return str(self.contacts)

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "name": name,
            "mobile": mobile,
            "office": office,
            "email": email
        }


def test_prob3():
    phone_book = PhoneBook()

    phone_book.add(
        "Choi",
        mobile="010-6751-2808",
        office="02-1234-5678",
        email="kim070811cms@naver.com"
    )

    phone_book.add(
        "Min",
        mobile="010-2345-6789",
        email="park070811cms@gmail.com"
    )

    print(phone_book)


if __name__ == "__main__":
    test_prob3()
