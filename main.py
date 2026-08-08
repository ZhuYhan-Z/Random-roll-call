import time
import importlib

print("\t欢迎来到随机点名系统")
while True: 
    choose = int(input("\t输入“1”开始点名\n\t输入“2”管理名单\n\t输入“3”退出:\n"))
    if choose == 1:
        action = importlib.import_module("action")
    elif choose == 2:
        importlib.import_module("manage")
    elif choose == 3:
        print("再见\n")
        break
    else:
        print("错误，请重新输入\n")
        time.sleep(0.5)
