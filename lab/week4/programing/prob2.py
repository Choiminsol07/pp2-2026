# 작성자 : 최민솔
# 작성일 : 2026.9.30
# 문제: 클래스를 작성하여 로켓의 위치를 관리한다.


# 클래스: Rocket
# 인스턴스 변수: x, y



class Rocket:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Rocket({self.x}, {self.y})"

    def moveUp(self):
        self.y += 1


def test_prob2():
    """prob2의 동작을 테스트한다."""

    myRocket = Rocket()

    print("로켓의 높이:", myRocket.y)

    myRocket.moveUp()

    print("로켓의 높이:", myRocket.y)


if __name__ == "__main__":
    test_prob2()
