#window 생성 

# from tkinter import * # tkinter 모듈을 포함시키는 것
import tkinter as tk

window = tk.Tk() # Tk 클래스의 객체가 생성되면서 화면에 하나의 윈도우가 생성
window.title("Hello 최민솔") # window의 제목
window.geometry("400x200") # window의 크기

label = tk.Label(window, text="Hello , GUI") # window에 label을 생성
label.pack() # 앞에서 만든 라벨을 창 안에 배치해서 화면에 보이게 하는 코드

window.mainloop() # 창을 계속 열어 두고, 버튼 클릭 같은 사용자 입력을 기다리는 GUI 실행 루프