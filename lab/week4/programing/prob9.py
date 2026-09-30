# 작성자: 최민솔
# 작성일: 2026.9.30
# 문제: turtle을 이용해서 거북이 2개를 만든다. 각각 다른 방향으로 움직이도록 한다.

# 작성자: 최민솔
# 작성일: 2026.9.30
# 문제: 09
# 해결하기 위한 설계: turtle 객체를 2개 만들고 각각 다른 방향으로 이동시킨다.

import turtle


def test_prob9():
    lee = turtle.Turtle()
    kim = turtle.Turtle()

    lee.shape("turtle")
    kim.shape("turtle")

    lee.penup()
    lee.goto(-200, 100)
    lee.pendown()

    lee.forward(80)
    lee.right(90)
    lee.forward(30)
    lee.left(90)
    lee.forward(170)
    lee.right(90)
    lee.forward(30)
    lee.left(90)
    lee.forward(100)

    kim.penup()
    kim.goto(200, -100)
    kim.pendown()

    kim.backward(100)
    kim.left(90)
    kim.forward(30)
    kim.right(90)
    kim.backward(170)
    kim.left(90)
    kim.forward(30)
    kim.right(90)
    kim.backward(80)

    turtle.done()


if __name__ == "__main__":
    test_prob9()
