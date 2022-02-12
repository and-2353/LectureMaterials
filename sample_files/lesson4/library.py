import math

print(math.pi)  # 定数の利用
print(math.cos(0.5))  # 関数の利用

# ----------------------------------------

import time

print(time.time()) # 現在時刻を表示(Unix時間という形式です)
time.sleep(2)  # 2秒間停止
print(time.time())  # 現在時刻を表示

# -----------------------------------------

from time import time, sleep

print(time()) # 現在時刻を表示(Unix時間という形式です)
sleep(2)  # 2秒間停止
print(time())  # 現在時刻を表示