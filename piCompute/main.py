from decimal import Decimal, getcontext
# 莱布尼兹公式计算圆周率 π
# π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

def pi_leibniz(iterations=1000000):
    pi_over_4 = 0.0
    for i in range(iterations):
        term = (-1) ** i / (2 * i + 1)
        pi_over_4 += term
    pi = pi_over_4 * 4
    return round(pi, 7)  # 保留7位小数


def pi_chudnovsky(precision=30):
    # 设置计算精度，比需要的20位多留10位避免误差
    getcontext().prec = precision + 10

    # Chudnovsky算法核心公式
    C = Decimal(426880) * Decimal(10005).sqrt()
    L = Decimal(13591409)
    X = Decimal(1)
    M = Decimal(1)
    K = Decimal(6)
    S = L

    for k in range(10):  # 迭代10次就能远超20位精度
        M = M * (K ** 3 - 16 * K) // (k + 1) ** 3
        L += Decimal(545140134)
        X *= Decimal(-262537412640768000)
        term = M * L / X
        S += term
        K += 12

    pi = C / S
    # 四舍五入到20位小数
    return round(pi, precision)

# 调用函数
pi_7 = pi_leibniz(1000000)
print(f"莱布尼兹公式计算的π（保留7位小数）：{pi_7}")

# 调用函数，计算20位小数
pi_20 = pi_chudnovsky(20)
print(f"Chudnovsky算法计算的π（20位小数）：{pi_20}")