import runpy
import os
import json
import time
import importlib
from actions import roll_call, load_names


#自动创建空名单
if not os.path.exists("name_list.json"):
    with open("name_list.json", "w", encoding="utf-8") as f:
        json.dump([], f)
    print("已自动创建name_list.json")
#进入主界面
print("\n\t欢迎来到随机点名系统\n")
while True:
    try:
        choose = int(input("\t输入“1”开始点名\n\t输入“2”管理名单\n\t输入“3”退出:\n"))
    except ValueError:
        print("\n\t错误，请重新输入 \n")
    else:
        if choose == 1:
            name_list = load_names()
            if not name_list:
                print("\n\t名单为空，请先添加学生\n")
            else:
                roll_name = roll_call(name_list)
                print(roll_name)
        elif choose == 2:
            runpy.run_module("manage")
        elif choose == 3:
            print("\t再见\n")
            break
        else:
            print("\n\t错误，请重新输入\n")
            time.sleep(0.5)
