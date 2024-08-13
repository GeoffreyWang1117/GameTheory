import numpy as np
import matplotlib.pyplot as plt

# 定义演化博弈函数
def hawk_dove_game_advanced(V, C, initial_hawk_fraction=0.5, num_generations=100, mutation_rate=0.01):
    """
    运行进阶版鹰鸽博弈模型，并展示鹰的比例如何随时间演化。

    参数:
    V - 资源的价值
    C - 打斗的代价
    initial_hawk_fraction - 初始鹰的比例
    num_generations - 演化的代数
    mutation_rate - 突变率，允许新的策略出现
    """
    
    # 初始化鹰和鸽的比例
    hawk_fraction = initial_hawk_fraction
    dove_fraction = 1 - hawk_fraction

    hawk_fractions = [hawk_fraction]

    for _ in range(num_generations):
        # 计算适应度
        hawk_payoff = (hawk_fraction * (V - C) / 2) + (dove_fraction * V)
        dove_payoff = (hawk_fraction * 0) + (dove_fraction * V / 2)

        # 更新策略比例
        hawk_fraction = (hawk_fraction * hawk_payoff) / (
            hawk_fraction * hawk_payoff + dove_fraction * dove_payoff)
        dove_fraction = 1 - hawk_fraction

        # 突变机制
        hawk_fraction += mutation_rate * (np.random.rand() - 0.5)
        hawk_fraction = np.clip(hawk_fraction, 0, 1)
        dove_fraction = 1 - hawk_fraction

        hawk_fractions.append(hawk_fraction)

    # 绘制结果
    plt.plot(hawk_fractions, label=f'Hawk Fraction (V={V}, C={C}, Mutation Rate={mutation_rate})')
    plt.xlabel('Generation')
    plt.ylabel('Fraction of Hawks')
    plt.title('Advanced Evolution of Hawk and Dove Strategies')
    plt.legend()
    plt.show()

def main():
    # 获取用户输入
    V = float(input("请输入资源的价值 V: "))
    C = float(input("请输入打斗的代价 C: "))
    initial_hawk_fraction = float(input("请输入初始鹰的比例 (0-1): "))
    num_generations = int(input("请输入模拟的代数: "))
    mutation_rate = float(input("请输入突变率 (0-1): "))

    # 运行博弈模拟
    hawk_dove_game_advanced(V, C, initial_hawk_fraction, num_generations, mutation_rate)

if __name__ == "__main__":
    main()
