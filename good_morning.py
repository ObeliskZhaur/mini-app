import datetime
import tkinter as tk
from tkinter import messagebox

# 获取当前时间
now = datetime.datetime.now()
hour = now.hour

# 判断问候语
if 5 <= hour < 12:
    greeting = "早安 🌅"
elif 12 <= hour < 18:
    greeting = "午安 ☀️"
else:
    greeting = "晚安 🌙"

# 组合问候信息
message = f"{greeting}！今天有什么计划吗？\n（现在时间：{now.strftime('%Y-%m-%d %H:%M')}）"

# 弹出窗口
root = tk.Tk()
root.withdraw()
messagebox.showinfo("每日问候", message)

# 可选：记录到日志文件
with open("daily_greeting_log.txt", "a") as log:
    log.write(f"[{now}] {message}\n")
