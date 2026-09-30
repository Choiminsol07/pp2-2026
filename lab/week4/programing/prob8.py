# 작성자: 최민솔
# 작성일: 2026.9.30
# 문제: 클래스를 만들고 생성자에서 가사 리스트를 저장한다. sing() 함수에서 저장된 가사를 한 줄씩 출력한다.

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for lyric in self.lyrics:
            print(lyric)


def test_prob8():
    aSong = Song([
        "TWINKLE, twinkle, little star,",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky."
    ])
    aSong.sing()


if __name__ == "__main__":
    test_prob8()
