import time
import runpy

print("欢迎来到随机点名系统")
x = 1
while x == 1: 
    choose = int(input("输入“1”开始点名 输入“2”管理名单 输入“3”退出:\n"))
    if choose == 1:
        x = 2
        runpy.run_path("dian_ming.py")
    elif choose == 2:
        x = 2
        runpy.run_path("deng_ji.py")
    elif choose == 3:
        exit()
    else:
        x = 1
    if x == 2:
        break
    else:
        print("错误，请重新输入")
        time.sleep(0.5)
        continue
