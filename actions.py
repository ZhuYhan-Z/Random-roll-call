import random
import json

def roll_call(names):
    """从names里随机抽取并输出到屏幕上"""
    roll_name = random.choice(names)
    print(roll_name)


def deng_ji():
    print("登记学生")
    name = input("名字:")
    num = int(input("学号:"))
    name_text = name
    num_text = num
    text = [name_text,num_text]
