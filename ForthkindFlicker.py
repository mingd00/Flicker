import tkinter as tk

# 전역 변수로 canvas와 버튼 위젯 정의
canvas = None
east_button = None
west_button = None
south_button = None
north_button = None

# 사각형 깜빡거리는 함수
def blink_rectangle(rectangle, blink_speed):
    fill_color = 'green'
    empty_color = ''

    def blink():
        current_color = canvas.itemcget(rectangle, "fill")
        next_color = empty_color if current_color == fill_color else fill_color
        canvas.itemconfig(rectangle, fill=next_color)
        canvas.after(int(1000 / blink_speed), blink)  # 1000ms = 1s

    blink()

# 메인 윈도우 생성
root = tk.Tk()
root.title("사각형 깜빡거리기")

# 캔버스 생성
canvas = tk.Canvas(root, width=1200, height=1000)
canvas.pack()

# 사각형들 생성 및 배치
rectangle_top = canvas.create_rectangle(500, 50, 700, 250, fill='', outline='green', width=5)
rectangle_bottom = canvas.create_rectangle(500, 600, 700, 800, fill='', outline='green', width=5)
rectangle_left = canvas.create_rectangle(10, 300, 210, 500, fill='', outline='green', width=5)
rectangle_right = canvas.create_rectangle(990, 300, 1190, 500, fill='', outline='green', width=5)

# 각각의 사각형을 깜빡거리는 함수 호출
blink_rectangle(rectangle_top, 17)
blink_rectangle(rectangle_bottom, 31)
blink_rectangle(rectangle_left, 47)
blink_rectangle(rectangle_right, 63)

# GUI 루프 시작
root.mainloop()
