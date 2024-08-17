from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ["进栈", "出栈", "查看", "查找", "转存", "结束"])


def select_menu() -> Menu:
    """菜单选择"""
    s = [f"({m.value}){m.name}" for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(":"))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(4)
while True:
    print(f"当前数据个数:{len(s)}/{s.capacity}")
    menu = select_menu()
    if menu == Menu.进栈:
        x = int(input("数据:"))
        try:
            s.push(x)
        except FixedStack.Full:
            print("栈已满")

    elif menu == Menu.出栈:
        try:
            x = s.pop()
            print(f"出栈的数据为{x}")
        except FixedStack.Empty:
            print("栈为空")
    elif menu == Menu.查看:
        try:
            x = s.peek()
            print(f"查看的栈顶数据为{x}")
        except FixedStack.Empty:
            print("栈为空")
    elif menu == Menu.查找:
        x = int(input("值:"))
        if x in s:
            print(f"包含{s.count(x)}数据,起始位置为{s.find(x)}")
        else:
            print("栈中不存在该值")
    elif menu == Menu.转存:
        s.dump()
    else:
        break
