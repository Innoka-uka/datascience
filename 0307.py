# 汉诺塔问题的递归解决方案
def hanoi(n, source, target, med):
    """
    递归解决汉诺塔问题
    : n: 盘子的数量
    : source: 初始柱子
    : target: 目标柱子
    : med: 辅助柱子
    """
    if n == 1:
        print(f"Move {source} to {target}")
        i=1
    else:
        # 将 n-1 个盘子从 source 移动到 med，使用 target 作为辅助
        a=hanoi(n-1, source, med, target)
        # 将第 n 个盘子从 source 移动到 target
        print(f"Move {source} to {target}")
        # 将 n-1 个盘子从 med 移动到 target，使用 source 作为辅助
        b=hanoi(n-1, med, target, source)
        i=a+b+1
    return i

def solve_hanoi(n):
    print(f"解决 {n} 个盘子的汉诺塔问题：")
    total_steps=hanoi(n, 'A', 'B', 'C')
    print(f"总共需要 {total_steps} 步。")

n = int(input("请输入盘子的数量："))
solve_hanoi(n)
