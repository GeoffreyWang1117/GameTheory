import numpy as np
import matplotlib.pyplot as plt

# 定义游戏参数
V = 50  # 资源的价值
C = 70  # 鹰之间打斗的代价

# 初始条件
initial_hawk_fraction = 0.5  # 初始鹰的比例
num_generations = 100  # 演化的代数

# 定义适应度函数
def fitness(hawk_fraction):
    dove_fraction = 1 - hawk_fraction

    # 鹰的预期收益
    hawk_payoff = (hawk_fraction * (V - C) / 2) + (dove_fraction * V)

    # 鸽的预期收益
    dove_payoff = (hawk_fraction * 0) + (dove_fraction * V / 2)

    return hawk_payoff, dove_payoff

# 模拟演化
hawk_fractions = [initial_hawk_fraction]

for _ in range(num_generations):
    current_hawk_fraction = hawk_fractions[-1]
    
    hawk_fitness, dove_fitness = fitness(current_hawk_fraction)
    
    # 更新鹰的比例
    new_hawk_fraction = current_hawk_fraction * hawk_fitness / (
        current_hawk_fraction * hawk_fitness + (1 - current_hawk_fraction) * dove_fitness
    )
    
    hawk_fractions.append(new_hawk_fraction)

# 绘制结果
plt.plot(hawk_fractions, label='Hawk Fraction')
plt.xlabel('Generation')
plt.ylabel('Fraction of Hawks')
plt.title('Evolution of Hawk and Dove Strategies')
plt.legend()
plt.show()
