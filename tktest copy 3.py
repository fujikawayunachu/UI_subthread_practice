import tkinter as tk
import threading
import random

count = 10

# ハンドラ関数
def start():
    global count
    count = 100
    button_1['state'] = tk.DISABLED
    # 新しいスレッドを開始
    thread = threading.Thread(target=countdown)
    thread.start()

# カウントダウンの関数
def countdown():
    global count
    while True:
        # メインスレッドでUIを更新
        root.after(0, update_ui)
        count -= 1
        threading.Event().wait(1)
    button_1['state'] = tk.NORMAL

# UIの更新関数
def update_ui():
    global count
    random_number = generate_random_number()
    doubled_number = double_number(random_number)
    label_1['text'] = f"Count: {count}, Random: {random_number}, Doubled: {doubled_number}"

# 1～10の乱数を発生させる関数
def generate_random_number():
    return random.randint(1, 10)

# 乱数を2倍にする関数
def double_number(number):
    return number * 2

# トップレベルウインドウの生成

def main():
    global root ,label_1,button_1
    root = tk.Tk()
    root.title('スレッド')
    root.geometry('350x150')

    # Labelウィジェットの生成
    label_1 = tk.Label(root, text='10')
    label_1.pack(expand=True)

    # Buttonウィジェットの生成
    button_1 = tk.Button(root, text='START', command=start)
    button_1.pack(expand=True)

    root.mainloop()

main()