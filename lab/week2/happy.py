# 생일축하 함수

def happybirthday(name:str) -> None:
    print("안녕하세요")
    print(name + "님의 생일을 축하드립니다.")
    return None

def test_happybirthday1() :
    happybirthday("민솔")
    happybirthday("영채")
    happybirthday("지연")
    happybirthday("윤빈")

def test_happybirthday2() :
    names = ["민솔", "영채", "지연", "윤빈"]
    for name in names:
        happybirthday(name)

def test_happybirthday3() :
    happybirthday(3.14)
    happybirthday(100)
    happybirthday([1,2,3])

if __name__ == "__main__":
    #test_happybirthday1()
    #test_happybirthday2()
    test_happybirthday3()
