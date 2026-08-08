import random
import json


def load_names():
    """从文件读取学生名单"""
    with open("name_list.json", "r", encoding="utf-8") as f:
        return json.load(f)


def roll_call(names):
    """从names里随机抽取一个并返还"""
    roll_name = random.choice(names)
    return roll_name


def deng_ji(new_name):
    """在json文件中新增一个学生名并保存"""
    with open("name_list.json","r",encoding = "utf-8") as f:
        json_list = json.load(f)
    json_list.append(new_name)
    json_list.sort()
    with open("name_list.json","w",encoding = "utf-8") as f:
        json.dump(json_list,f, ensure_ascii = False, indent = 2)


def delete(delete_name):
    """从json文件中删除输入的学生名并重新保存"""
    with open("name_list.json","r",encoding = "utf-8") as f:
        json_list = json.load(f)
    if delete_name in json_list:
        json_list.remove(delete_name)
    else:
        print(f"学生{delete_name}不在名单中")
    with open("name_list.json","w",encoding = "utf-8") as f:
        json.dump(json_list,f, ensure_ascii = False, indent = 2)


def show():
    """遍历json文件中的学生名"""
    with open("name_list.json","r",encoding = "utf-8") as f:
        json_list = json.load(f)
    for name in json_list:
        print(name)
    print("已展示所有学生")
