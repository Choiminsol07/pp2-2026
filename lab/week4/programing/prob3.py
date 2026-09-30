# 작성자: 최민솔
# 작성일: 2026.9.30
# 문제: 클래스를 작성하여 상자의 부피를 계산한다.

# 클래스명 : Box
# 인스턴스 변수: length, height, depth



class Box:

    def __init__(self, l, h, d):
        self.length = l
        self.height = h
        self.depth = d

    def __str__(self):
        return f"({self.length}, {self.height}, {self.depth})"

    def setLength(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setDepth(self, depth):
        self.depth = depth

    def getDepth(self):
        return self.depth


def test_prob3():

    b1 = Box(100, 100, 100)

    print(b1)

    volume = (
        b1.getHeight()
        * b1.getLength()
        * b1.getDepth()
    )

    print("상자의 부피는", volume)


if __name__ == "__main__":
    test_prob3()
