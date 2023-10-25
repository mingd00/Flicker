import tkinter as tk

# Tkinter 창 생성
root = tk.Tk()
root.geometry("1000x1000")  # 윈도우 크기를 600x400으로 설정
root.title("Tkinter 화면 전환 예제")

# 첫 번째 화면
frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(fill="both", expand=True)

label1 = tk.Label(frame1, text="보고싶은 위치를 선택하세요!", font=("Helvetica", 30))
label1.pack(pady=20)

# "동" 버튼 클릭 시 두 번째 화면을 표시하고 첫 번째 화면을 숨김
def east_button_click():
    frame1.pack_forget()  # 첫 번째 화면을 숨김
    frame2.pack(fill="both", expand=True)  # 두 번째 화면을 표시

east_button = tk.Button(frame1, text="동", command=east_button_click)
east_button.pack()

# "서" 버튼 클릭 시 두 번째 화면을 표시하고 첫 번째 화면을 숨김
def west_button_click():
    frame1.pack_forget()  # 첫 번째 화면을 숨김
    frame2.pack(fill="both", expand=True)  # 두 번째 화면을 표시

west_button = tk.Button(frame1, text="서", command=west_button_click)
west_button.pack()

# "남" 버튼 클릭 시 두 번째 화면을 표시하고 첫 번째 화면을 숨김
def south_button_click():
    frame1.pack_forget()  # 첫 번째 화면을 숨김
    frame2.pack(fill="both", expand=True)  # 두 번째 화면을 표시

south_button = tk.Button(frame1, text="남", command=south_button_click)
south_button.pack()

# "북" 버튼 클릭 시 두 번째 화면을 표시하고 첫 번째 화면을 숨김
def north_button_click():
    frame1.pack_forget()  # 첫 번째 화면을 숨김
    frame2.pack(fill="both", expand=True)  # 두 번째 화면을 표시

north_button = tk.Button(frame1, text="북", command=north_button_click)
north_button.pack()

# 두 번째 화면 (초기에는 숨김)
frame2 = tk.Frame(root, bg="lightgreen")
frame2.pack(fill="both", expand=True)
frame2.pack_forget()  # 초기에 숨김

label2 = tk.Label(frame2, text="두 번째 화면", font=("Helvetica", 16))
label2.pack(pady=20)

# "돌아가기" 버튼 클릭 시 두 번째 화면을 숨기고 첫 번째 화면을 표시
def return_button_click():
    frame2.pack_forget()  # 두 번째 화면을 숨김
    frame1.pack(fill="both", expand=True)  # 첫 번째 화면을 표시

return_button = tk.Button(frame2, text="돌아가기", command=return_button_click)
return_button.pack()

root.mainloop()
