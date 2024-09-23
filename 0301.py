import math

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

if __name__ == "__main__":
    a = int(input("请输入一个整数: "))
    if is_prime(a):
        print(f"{a} 是质数")
    else:
        print(f"{a} 不是质数")