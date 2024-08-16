from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ["添加", "删除", "查找", "转存", "结束"])


def select_menu() -> Menu:
    """菜单选择"""
    s = [f"({m.value}) {m.name}" for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(":"))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)
while True:
    menu = select_menu()
    if menu == Menu.添加:
        key = int(input("关键字:"))
        value = input("值:")
        if not hash.add(key, value):
            print("添加失败")
    elif menu == Menu.删除:
        key = int(input("关键字:"))
        if not hash.remove(key):
            print("删除失败")
    elif menu == Menu.查找:
        key = int(input("关键字:"))
        t = hash.search(key)
        if t is not None:
            print(f"该关键字的值为{t}")
        else:
            print("没有找到匹配的数据")
    elif menu == Menu.转存:
        hash.dump()
    else:
        break
