from Solution1 import Solution1


def main():
    # 输入
    haystacks = ["sadbutsad", "leetcode"]
    needles = ["sad", "leeto"]
    # 期望输出
    expectedSub = [0, -1]

    # 调用
    solution = Solution1()
    for i, haystack in enumerate(haystacks):
        k = solution.strStr(haystack, needles[i])
        assert k == expectedSub[i]


if __name__ == '__main__':
    main()
