from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ["插入", "删除", "查找", "转存", "关键字范围", "结束"])


def select_menu() -> Menu:
    s = [f"({m.value}) {m.name}" for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(":"))
        if 1 <= n <= len(Menu):
            return Menu(n)


tree = BinarySearchTree()
while True:
    menu = select_menu()
    if menu == Menu.插入:
        key = int(input("关键字:"))
        val = input("值")
        if not tree.add(key, val):
            print("插入失败")
    elif menu == Menu.删除:
        key = int(input("关键字:"))
        tree.remove(key)
    elif menu == Menu.查找:
        key = int(input("关键字:"))
        t = tree.search(key)
        if t is not None:
            print(f"关键字的值为{t}")
        else:
            print("没有符合条件的数据")
    elif menu == Menu.转存:
        tree.dump()
    elif menu == Menu.关键字范围:
        print(f"最小关键字 = {tree.min_key()}")
        print(f"最大关键字 = {tree.max_key()}")
    else:
        break
