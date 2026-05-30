from pynput.keyboard import Key, Controller, Listener
from time import sleep

keyboard = Controller()

running = True

def on_press(key):
    global running
    if key == Key.space:
        print("\n🛑 紧急停止！按空格键已生效")
        running = False
        return False
    return True

# 启动监听器
listener = Listener(on_press=on_press)
listener.daemon = True
listener.start()

print("=" * 50)
print("⚠️  安全提示")
print("=" * 50)
print("1. 请先打开【记事本】窗口")
print("2. 点击记事本让光标闪烁")
print("3. 5秒后开始自动输入")
print("4. 按【空格键】可随时停止")
print("=" * 50)

sleep(5)

print("🚀 开始发送...")

for i in range(10):  # 测试阶段可以用 range(20)
    if not running:
        break
    
    keyboard.type('这是一条脚本自动输入的信息')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(0.1)
    
    # 实时显示进度
    print(f"已发送 {i+1} 条", end="\r")

print("\n" + "=" * 50)
if running:
    print("✅ 全部发送完成")
else:
    print("🛑 已被用户中断")
print("=" * 50)