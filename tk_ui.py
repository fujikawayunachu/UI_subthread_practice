import tkinter as tk
import threading
import random

count = 10
random_number = 0
doubled_number = 0

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
    while count > 0:
        count -= 1
        # サブスレッドでランダム生成と2倍にする関数を実行
        random_thread = threading.Thread(target=update_random_and_double)
        random_thread.start()
        random_thread.join()
        # メインスレッドでUIを更新
        root.after(0, update_ui)
        print(f"Main Thread: count={count}")
        threading.Event().wait(1)
    button_1['state'] = tk.NORMAL

# 乱数生成と2倍にする関数の呼び出し
def update_random_and_double():
    global random_number, doubled_number
    random_number = generate_random_number()
    doubled_number = double_number(random_number)
    print(f"Sub Thread: random_number={random_number}, doubled_number={doubled_number}")

# UIの更新関数
def update_ui():
    global count, random_number, doubled_number
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
