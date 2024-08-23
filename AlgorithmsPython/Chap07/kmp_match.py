def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0] * (len(pat) + 1)

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    return pt - pp if pp == len(pat) else -1


if __name__ == '__main__':
    s1 = input("文本串:")
    s2 = input("模式串:")

    idx = kmp_match(s1, s2)
    if idx == -1:
        print("文本串中不包含模式串")
    else:
        print(f"第{(idx + 1)}个字符串匹配成功")
