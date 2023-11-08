import tkinter as tk

# 전역 변수로 canvas와 버튼 위젯 정의
canvas = None
east_button = None
west_button = None
south_button = None
north_button = None

# Tkinter 창 생성
root = tk.Tk()
root.geometry("1000x1000")  # 윈도우 크기
root.title("FothKind Filcker")

# 사각형 생성 함수
def create_rectangle(canvas, x1, y1, x2, y2):
    ans = canvas.create_rectangle(x1, y1, x2, y2, fill='', outline='green', width=5)
    return ans
    
# 사각형 깜빡거리는 함수
def blink_rectangle(rectangle, blink_speed, canvas):
    fill_color = 'green'
    empty_color = ''

    def blink():
        nonlocal fill_color, empty_color
        current_color = canvas.itemcget(rectangle, "fill")
        next_color = empty_color if current_color == fill_color else fill_color
        canvas.itemconfig(rectangle, fill=next_color)
        canvas.after(int(1000 / blink_speed), blink)  # 1000ms = 1s

    blink()  # 첫 깜빡임 시작


# 캔버스 생성 함수
def create_canvas(frame, x1, y1, x2, y2, second):
    canvas = tk.Canvas(frame, width=1200, height=1000)
    canvas.pack()
    rectangle = create_rectangle(canvas, x1, y1, x2, y2)
    blink_rectangle(rectangle, second, canvas)

# 첫 번째 화면
frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(fill="both", expand=True)

label1 = tk.Label(frame1, text="보고싶은 위치를 선택하세요!", font=("Helvetica", 30))
label1.pack(pady=20)

# 동쪽 화면 (초기에는 숨김)
east_frame = tk.Frame(root, bg="lightgreen")
east_frame.pack(fill="both", expand=True)
east_frame.pack_forget()  # 초기에 숨김

east_label = tk.Label(east_frame, text="동쪽 화면", font=("Helvetica", 16))
east_label.pack(pady=20)

# 서쪽 화면 (초기에는 숨김)
west_frame = tk.Frame(root, bg="lightgreen")
west_frame.pack(fill="both", expand=True)
west_frame.pack_forget()  # 초기에 숨김

west_label = tk.Label(west_frame, text="서쪽 화면", font=("Helvetica", 16))
west_label.pack(pady=20)

# 남쪽 화면 (초기에는 숨김)
south_frame = tk.Frame(root, bg="lightgreen")
south_frame.pack(fill="both", expand=True)
south_frame.pack_forget()  # 초기에 숨김

south_label = tk.Label(south_frame, text="남쪽 화면", font=("Helvetica", 16))
south_label.pack(pady=20)

# 북쪽 화면 (초기에는 숨김)
north_frame = tk.Frame(root, bg="lightgreen")
north_frame.pack(fill="both", expand=True)
north_frame.pack_forget()  # 초기에 숨김

north_label = tk.Label(north_frame, text="북쪽 화면", font=("Helvetica", 16))
north_label.pack(pady=20)

# 사각형 생성
create_canvas(north_frame, 500, 50, 700, 250, 17)
create_canvas(south_frame, 500, 600, 700, 800, 31)
create_canvas(west_frame, 10, 300, 210, 500, 47)
create_canvas(east_frame, 990, 300, 1190, 500, 63)

# 화면 전환 함수
def show_frame(frame):
    frame1.pack_forget()
    frame.pack(fill="both", expand=True)  # 선택한 프레임을 보여줌

# 동서남북 버튼 생성 함수
def forthkind_button_create(forthkind_button, text, frame, location):
    forthkind_button = tk.Button(frame1, text=text, command=lambda: show_frame(frame))
    forthkind_button.config(width=10, height=2)  # 버튼 크기 설정
    forthkind_button.place(relx=0.5, rely=location, anchor=tk.CENTER)  # 버튼 위치 설정
    
forthkind_button_create(east_button, '동', east_frame, 0.3)
forthkind_button_create(west_button, '서', west_frame, 0.4)
forthkind_button_create(east_button, '남', south_frame, 0.5)
forthkind_button_create(east_button, '북', north_frame, 0.6)

# 첫화면으로 돌아가기
def show_frame1():
    east_frame.pack_forget()
    west_frame.pack_forget()
    south_frame.pack_forget()
    north_frame.pack_forget()
    frame1.pack(fill="both", expand=True)

# 돌아가기 버튼 생성 함수
def return_button_create(frame):
    return_button = tk.Button(frame, text="돌아가기", command=show_frame1)
    return_button.config(width=10, height=2)  # 버튼 크기 설정
    return_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # 버튼 위치 설정
    
return_button_create(east_frame)
return_button_create(west_frame)
return_button_create(south_frame)
return_button_create(north_frame)

root.mainloop()
