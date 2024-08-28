def quick_sort_iterative(array):
    # 使用列表模拟栈，初始时将整个数组的范围压入栈
    stack = [(0, len(array) - 1)]

    # 当栈不为空时，继续处理子数组
    while stack:
        # 弹出栈中的一个子数组范围
        start, end = stack.pop()

        # 如果子数组的范围无效（即只有一个或零个元素），跳过
        if start >= end:
            continue

        # 选择基准值，通常选择中间元素
        pivot = array[(start + end) // 2]

        # 初始化左右指针
        left, right = start, end

        # 分区操作：将数组分为小于基准值和大于基准值的两部分
        while left <= right:
            # 左指针向右移动，直到找到一个不小于基准值的元素
            while array[left] < pivot:
                left += 1
            # 右指针向左移动，直到找到一个不大于基准值的元素
            while array[right] > pivot:
                right -= 1
            # 如果左右指针未交错，交换这两个元素的位置
            if left <= right:
                array[left], array[right] = array[right], array[left]
                # 移动指针
                left += 1
                right -= 1

        # 将分区后的左右子数组范围压入栈中
        stack.append((start, right))  # 处理左边部分
        stack.append((left, end))  # 处理右边部分

    return array


# 示例用法
ls = [1, 5, 10, 8, 9, 2, 34, 5]
print(quick_sort_iterative(ls))
