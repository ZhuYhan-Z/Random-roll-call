import json
import importlib
import time
from actions import deng_ji, delete, show
while True:
    choose_manage = int(input("\t输入“1“”登记新学生\n\t输入“2”移除现有学生\n\t输入“3”显示现有学生\n\t输入“4”退回主界面\n"))
    if choose_manage == 1:
        new_name = input("登记新学生:")
        deng_ji(new_name)
    elif choose_manage == 2:
        delete_name = input("删除学生:")
        delete(delete_name)
    elif choose_manage == 3:
        show()
    elif choose_manage == 4:
        break
    else:
        print("错误，请重新输入\n")
        time.sleep(0.5)

