import json
import importlib
import time
from actions import add_name, delete_name, show_name, load_names, delete_all


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
            print(f"已添加新学生{new_name}")
        elif choose_manage == 2:
            if not json_list:
                print("\n\t名单为空，请先添加学生\n")
            else:
                deleted_name = input("\t删除学生(输入“delete all”删除名单内全部学生):")
                if deleted_name == "delete all":
                    delete_all()
                    print("已删除名单内所有学生")
                else:
                    delete_name(deleted_name)
                    print(f"已删除学生{deleted_name}")
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

