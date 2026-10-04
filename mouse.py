from time import sleep
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Listener
from random import uniform

mouse = Controller()

running = True
ext = False

def on_press(key):
    global running
    global ext
    if key == Key.alt_l:
        if running:
            running = False
            print("\n🛑 紧急停止！")
        else:
            running = True
            print("\n重新开始")
    if key == Key.tab:
        print("bye bye了您嘞")
        running = False
        ext = True
        return False
    return True

c = input("左键or右键？(left/right): ").strip().lower()
if c == "left" or c == "l" or c == "左":
    mouse_button = Button.left
elif c == "right" or c == "r" or c == "右":
    mouse_button = Button.right

t = float(input("请输入点击间隔（单位秒不要小于0.05）：").strip())

listener = Listener(on_press=on_press)
listener.daemon = True
listener.start()

print("=" * 50)
print("⚠️  安全提示")
print("连点器即将启动，请做好准备！")
print("按下左Alt可随时停止,再次按左Alt启动，按下tab彻底结束")
print("=" * 50)

for i in range(5, 0, -1):
    print(i, end="\r")
    sleep(1)
print(0, end="\r")

while True:
    while running:
        mouse.press(mouse_button)
        sleep(uniform(0.01,0.03))
        mouse.release(mouse_button)
        sleep(uniform(t-0.05,t+0.06))
    sleep(0.05)
    if ext:
        break