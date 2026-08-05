from pynput.mouse import Controller, Button
import pynput.keyboard
from time import sleep
import random

mouse = Controller()
keyboard = pynput.keyboard.Controller()
running = True

def on_press(key):
    global running
    if key == pynput.keyboard.Key.space:
        print("\n🛑 紧急停止！按空格键已生效")
        running = False
        return False
    return True

# 启动键盘监听
listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

print("5秒后即将启动脚本，请做好准备，按下空格可结束")
for i in range(5, 0, -1):
    print(f"倒计时: {i}  ", end="\r")
    sleep(1)
print("脚本已启动！          ")

mouse.press(Button.left)
minute = 60
hour = 3600

sleep_time = 20*minute
# 主循环
while running:
    # 等待 1 小时（3600秒），但每1秒检查一次 running 状态
    for _ in range(sleep_time):  # 1小时 = 3600秒
        sleep(1)
        if not running:
            break
    
    if not running:
        break
    
    # 模拟人类操作：短暂松开鼠标
    mouse.release(Button.left)
    sleep(random.uniform(0.2, 0.5))  # 随机间隔
    
    # 发送消息
    keyboard.press(pynput.keyboard.KeyCode.from_char("t"))
    keyboard.release(pynput.keyboard.KeyCode.from_char("t"))
    sleep(0.1)  # 等待聊天框打开
    
    keyboard.type(f"我正在挂机刷石头，每{sleep_time/60}分钟宏就会播报一次这个消息")
    sleep(0.1)
    
    keyboard.press(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.enter)
    sleep(0.5)  # 等待消息发送完成
    
    # 继续按住左键
    mouse.press(Button.left)

# 清理
mouse.release(Button.left)
print("脚本已停止")