from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ["向头部插入", "向尾部插入", "删除头节点", "删除尾节点",
                     "显示当前节点", "当前节点向后移动", "删除当前节点", "全部删除",
                     "查找", "成员判断", "显示所有节点", "遍历", "结束"])


def select_Menu() -> Menu:
    """选择菜单"""
    s = [f'({m.value}) {m.name}' for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(":"))
        if 1 <= n <= len(Menu):
            return Menu(n)


lst = LinkedList()
while True:
    menu = select_Menu()
    if menu == Menu.向头部插入:
        lst.add_first(int(input("值:")))
    elif menu == Menu.向尾部插入:
        lst.add_last(int(input("值:")))
    elif menu == Menu.删除头节点:
        lst.remove_first()
    elif menu == Menu.删除尾节点:
        lst.remove_last()
    elif menu == Menu.显示当前节点:
        lst.print_current_node()
    elif menu == Menu.当前节点向后移动:
        lst.next()
    elif menu == Menu.删除当前节点:
        lst.remove_current_node()
    elif menu == Menu.全部删除:
        lst.clear()
    elif menu == Menu.查找:
        pos = lst.search(int(input("值:")))
        if pos >= 0:
            print(f"等于该值的数据位于表中第{pos + 1}位")
        else:
            print("没有符号条件的数据")
    elif menu == Menu.成员判断:
        print("等于该值的数据" + ("存在." if int(input("值:")) in lst else "不存在."))
    elif menu == Menu.显示所有节点:
        lst.print()
    elif menu == Menu.遍历:
        for e in lst:
            print(e)
    else:
        break
