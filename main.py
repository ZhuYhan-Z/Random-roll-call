import runpy
import json
import time
import importlib
from actions import roll_call, load_names

print("\t欢迎来到随机点名系统")
while True:
    choose = int(input("\t输入“1”开始点名\n\t输入“2”管理名单\n\t输入“3”退出:\n"))
    if choose == 1:
        name_list = load_names()
        roll_name = roll_call(name_list)
        print(roll_name)
    elif choose == 2:
        runpy.run_module("manage")
    elif choose == 3:
        print("再见\n")
        break
    else:
        print("错误，请重新输入\n")
        time.sleep(0.5)
