import tkinter as tk

# 사각형 깜빡거리는 함수
def blink_rectangle(canvas, rectangle, blink_speed):
    fill_color = 'green'
    empty_color = ''

    def blink():
        current_color = canvas.itemcget(rectangle, "fill")
        next_color = empty_color if current_color == fill_color else fill_color
        canvas.itemconfig(rectangle, fill=next_color)
        root.after(int(1000 / blink_speed), blink)  # 1000ms = 1s

    blink()

# 메인 윈도우 생성
root = tk.Tk()
root.title("사각형 깜빡거리기")

# 캔버스 생성
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# 사각형들 생성 및 배치
rectangle_top = canvas.create_rectangle(400, 50, 600, 250, fill='', outline='green', width=5)
rectangle_bottom = canvas.create_rectangle(400, 550, 600, 750, fill='', outline='green', width=5)
rectangle_left = canvas.create_rectangle(100, 300, 300, 500, fill='', outline='green', width=5)
rectangle_right = canvas.create_rectangle(700, 300, 900, 500, fill='', outline='green', width=5)

# 각각의 사각형을 깜빡거리는 함수 호출
blink_rectangle(canvas, rectangle_top, 17)
blink_rectangle(canvas, rectangle_bottom, 31)
blink_rectangle(canvas, rectangle_left, 47)
blink_rectangle(canvas, rectangle_right, 63)

# GUI 루프 시작
root.mainloop()
