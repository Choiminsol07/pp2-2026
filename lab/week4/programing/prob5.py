# 작성자: 최민솔
# 작성일: 2026.09.30
# 문제: Triangle 클래스를 작성하시오.

# 클래스: Triangle
# 인스턴스 변수: angle1, angle2, angle3


class Triangle:
    def __init__(self, a1, a2, a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3

    def __str__(self):
        return f"Triangle({self.angle1}, {self.angle2}, {self.angle3})"

    def setAngle1(self, angle):
        self.angle1 = angle

    def setAngle2(self, angle):
        self.angle2 = angle

    def setAngle3(self, angle):
        self.angle3 = angle

    def getAngle1(self):
        return self.angle1

    def getAngle2(self):
        return self.angle2

    def getAngle3(self):
        return self.angle3

    def checkAngles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


def test_prob1():
    triangle = Triangle(90, 30, 60)
    print(triangle)
    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob1()
