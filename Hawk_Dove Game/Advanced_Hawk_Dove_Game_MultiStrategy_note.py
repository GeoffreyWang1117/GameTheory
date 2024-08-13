import numpy as np
import matplotlib.pyplot as plt

class Individual:
    def __init__(self, strategy):
        self.strategy = strategy  # 'Hawk', 'Dove' 或 'Mixed'（混合策略）

    def play(self, opponent, V, C):
        # 以下内容是与先前版本相比新增的功能
        if self.strategy == 'Mixed':
            # 如果自身策略为混合策略，随机选择鹰或鸽
            self_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return Individual(self_choice).play(opponent, V, C)
        elif opponent.strategy == 'Mixed':
            # 如果对手策略为混合策略，对手随机选择鹰或鸽
            opponent_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return self.play(Individual(opponent_choice), V, C)
        # 新增部分结束

        # 常规的策略交互部分（与先前版本相同）
        if self.strategy == 'Hawk' and opponent.strategy == 'Hawk':
            return (V - C) / 2, (V - C) / 2
        elif self.strategy == 'Hawk' and opponent.strategy == 'Dove':
            return V, 0
        elif self.strategy == 'Dove' and opponent.strategy == 'Hawk':
            return 0, V
        elif self.strategy == 'Dove' and opponent.strategy == 'Dove':
            return V / 2, V / 2
        else:
            # 防止没有返回值的情况，保证返回一个默认值
            return 0, 0

class Population:
    def __init__(self, size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction):
        # 在先前版本的基础上，增加了混合策略的初始化
        strategies = (['Hawk'] * int(size * initial_hawk_fraction) +
                      ['Dove'] * int(size * initial_dove_fraction) +
                      ['Mixed'] * int(size * initial_mixed_fraction))  # 增加了混合策略的比例
        self.individuals = [Individual(strategy) for strategy in strategies]

    def evolve(self, V, C, mutation_rate, num_generations):
        hawk_fractions = []
        dove_fractions = []
        mixed_fractions = []  # 新增，记录混合策略的比例变化

        for _ in range(num_generations):
            # 每一代中，个体与随机选择的对手进行交互
            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent = self.individuals[i].play(opponent, V, C)

                # 突变机制
                if np.random.rand() < mutation_rate:
                    # 在突变中，混合策略也被作为可能的选项
                    self.individuals[i].strategy = np.random.choice(['Hawk', 'Dove', 'Mixed'])

            # 计算当前策略的比例
            hawk_count = sum(1 for ind in self.individuals if ind.strategy == 'Hawk')
            dove_count = sum(1 for ind in self.individuals if ind.strategy == 'Dove')
            mixed_count = sum(1 for ind in self.individuals if ind.strategy == 'Mixed')  # 计算混合策略的数量

            hawk_fraction = hawk_count / len(self.individuals)
            dove_fraction = dove_count / len(self.individuals)
            mixed_fraction = mixed_count / len(self.individuals)  # 计算混合策略的比例

            hawk_fractions.append(hawk_fraction)
            dove_fractions.append(dove_fraction)
            mixed_fractions.append(mixed_fraction)  # 记录混合策略的比例变化

        # 绘制结果，包括三种策略的比例随代数的变化
        plt.plot(hawk_fractions, label='Hawk Fraction')
        plt.plot(dove_fractions, label='Dove Fraction')
        plt.plot(mixed_fractions, label='Mixed Fraction')  # 增加混合策略的比例变化
        plt.xlabel('Generation')
        plt.ylabel('Strategy Fractions')
        plt.title('Evolution of Hawk, Dove, and Mixed Strategies')
        plt.legend()
        plt.show()

def main():
    # 获取用户输入
    V = float(input("请输入资源的价值 V: "))
    C = float(input("请输入打斗的代价 C: "))
    population_size = int(input("请输入群体规模: "))
    initial_hawk_fraction = float(input("请输入初始鹰的比例 (0-1): "))
    initial_dove_fraction = float(input("请输入初始鸽的比例 (0-1): "))
    initial_mixed_fraction = float(input("请输入初始混合策略的比例 (0-1): "))  # 新增混合策略比例的输入
    num_generations = int(input("请输入模拟的代数: "))
    mutation_rate = float(input("请输入突变率 (0-1): "))

    # 初始化群体并运行模拟
    population = Population(population_size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction)
    population.evolve(V, C, mutation_rate, num_generations)

if __name__ == "__main__":
    main()
