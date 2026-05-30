from time import sleep
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Listener

mouse = Controller()

running = True

def on_press(key):
    global running
    if key == Key.space:
        print("\n🛑 紧急停止！按空格键已生效")
        running = False
        return False
    return True

c = input("左键or右键？(left/right): ").strip().lower()
if c == "left" or c == "l" or c == "左":
    mouse_button = Button.left
elif c == "right" or c == "r" or c == "右":
    mouse_button = Button.right

t = float(input("请输入点击间隔（单位秒，输入0为1帧间隔）：").strip())

listener = Listener(on_press=on_press)
listener.daemon = True
listener.start()

print("=" * 50)
print("⚠️  安全提示")
print("连点器即将启动，请做好准备！")
print("按下【空格键】可随时停止")
print("=" * 50)

for i in range(5, 0, -1):
    print(i, end="\r")
    sleep(1)
print(0, end="\r")

while running:
    mouse.press(mouse_button)
    mouse.release(mouse_button)
    sleep(t)