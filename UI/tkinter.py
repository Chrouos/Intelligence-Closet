# import os
# print(os.getcwd())  # 一開的環境在 ../

import tkinter as tk

# 環境設定
window = tk.Tk()             # 定義一個視窗 變數名稱叫: window
window.title('Lobby')        # 設定標題名稱: Lobby

width = 1500
height = 800
window.geometry("1500x800")  # 設定視窗大小

div_size = 200
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='blue')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='orange')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='green')

div1.grid(column=0, row=0, rowspan=2)
div2.grid(column=1, row=0)
div3.grid(column=1, row=1)


# weather.pack()

# 最後顯示設定
# window.attributes('-fullscreen', True)   # 全螢幕顯示
window.mainloop()           # 主視窗迴圈顯示

