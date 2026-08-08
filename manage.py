from pathlib import Path
import json
import importlib

while True:
    choose_manage = input("\t输入“1“”登记新学生\n\t输入“2”移除现有学生\n\t输入“3”显示现有学生")
    if choose_manage == 1:
        action = importlib.import_module("action")
    elif choose_manage == 2:
        action = importlib.import_module("action")
    elif choose_manage == 3:
        action = importlib.import_module("action")
    else:
        print("错误，请重新输入\n")
        time.sleep(0.5)
