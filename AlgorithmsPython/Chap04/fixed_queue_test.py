from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ["入队", "出队", "查看", "查找", "转存", "结束"])


def select_menu() -> Menu:
    s = [f"({m.value}) {m.name}" for m in Menu]
    while True:
        print(*s, sep=" ", end="")
        n = int(input(":"))
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)
while True:
    print(f"当前数据个数:{len(q)}/{q.capacity}")
    menu = select_menu()

    if menu == Menu.入队:
        x = int(input("数据:"))
        try:
            q.enqueue(x)
        except FixedQueue.Full:
            print("队列已满")
    elif menu == Menu.出队:
        try:
            x = q.dequeue()
            # print(f"出队的数据为{x}")
            print("出队的数据为{}".format(x))
        except FixedQueue.Empty:
            print("队列已空")

    elif menu == Menu.查看:
        try:
            x = q.peek()
            print(f"查看的队头数据为{x}")
        except FixedQueue.Empty:
            print("队列为空")
    elif menu == Menu.查找:
        x = int(input("值:"))
        if x in q:
            print(f"包含{q.count(x)}个数据,起始位置为{q.find(x)}")
        else:
            print("队列中不存在该值")
    elif menu == Menu.转存:
        q.dump()
    else:
        break
