import json
import importlib
import time
from actions import add_name, delete_name, show_name, load_names


while True:
    json_list = load_names()
    try:
        choose_manage = int(input("\t输入“1“”登记新学生\n\t输入“2”移除现有学生\n\t输入“3”显示现有学生\n\t输入“4”退回主界面\n"))
    except ValueError:
        print("\n\t错误，请重新输入\n")
    else:
        if choose_manage == 1:
            new_name = input("登记新学生:")
            add_name(new_name)
        elif choose_manage == 2:
            if not json_list:
                print("\n\t名单为空，请先添加学生\n")
            else:
                deleted_name = input("\t删除学生:")
                delete_name(deleted_name)
        elif choose_manage == 3:
            if not json_list:
                print("\n\t名单为空，请先添加学生\n")
            else:
                show_name()
        elif choose_manage == 4:
            break
        else:
            print("\n\t错误，请重新输入\n")
            time.sleep(0.5)

