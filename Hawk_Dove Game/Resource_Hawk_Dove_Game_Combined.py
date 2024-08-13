import numpy as np
import matplotlib.pyplot as plt

class Individual:
    def __init__(self, strategy):
        self.strategy = strategy  # 'Hawk', 'Dove' 或 'Mixed'

    def play(self, opponent, V, C, available_resource):
        if available_resource <= 0:
            return 0, 0  # 没有资源时，双方收益为0

        if self.strategy == 'Mixed':
            self_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return Individual(self_choice).play(opponent, V, C, available_resource)
        elif opponent.strategy == 'Mixed':
            opponent_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return self.play(Individual(opponent_choice), V, C, available_resource)

        if self.strategy == 'Hawk' and opponent.strategy == 'Hawk':
            return (V - C) / 2, (V - C) / 2
        elif self.strategy == 'Hawk' and opponent.strategy == 'Dove':
            return V, 0
        elif self.strategy == 'Dove' and opponent.strategy == 'Hawk':
            return 0, V
        elif self.strategy == 'Dove' and opponent.strategy == 'Dove':
            return V / 2, V / 2
        else:
            return 0, 0

class Population:
    def __init__(self, size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction):
        strategies = (['Hawk'] * int(size * initial_hawk_fraction) +
                      ['Dove'] * int(size * initial_dove_fraction) +
                      ['Mixed'] * int(size * initial_mixed_fraction))
        self.individuals = [Individual(strategy) for strategy in strategies]

    def evolve(self, V, C, mutation_rate, num_generations, initial_resource, renewable_resource_percent, non_renewable_resource_percent):
        hawk_fractions = []
        dove_fractions = []
        mixed_fractions = []
        renewable_resources = initial_resource * renewable_resource_percent
        non_renewable_resources = initial_resource * non_renewable_resource_percent

        for gen in range(num_generations):
            hawk_fractions.append(sum(1 for ind in self.individuals if ind.strategy == 'Hawk') / len(self.individuals))
            dove_fractions.append(sum(1 for ind in self.individuals if ind.strategy == 'Dove') / len(self.individuals))
            mixed_fractions.append(sum(1 for ind in self.individuals if ind.strategy == 'Mixed') / len(self.individuals))

            total_resources = renewable_resources + non_renewable_resources
            if total_resources <= 0:
                total_resources = 0

            resources = []  # 记录每一代剩余资源

            # 每一代中，个体与随机选择的对手进行交互
            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent = self.individuals[i].play(opponent, V, C, total_resources)

                # 更新资源数量
                total_payoff = payoff_self + payoff_opponent
                if total_payoff > 0:
                    if non_renewable_resources >= total_payoff:
                        non_renewable_resources -= total_payoff
                    else:
                        total_payoff -= non_renewable_resources
                        non_renewable_resources = 0
                        renewable_resources -= total_payoff

                resources.append(total_resources)

                # 突变机制
                if np.random.rand() < mutation_rate:
                    self.individuals[i].strategy = np.random.choice(['Hawk', 'Dove', 'Mixed'])

            # 更新可再生资源
            renewable_resources = min(renewable_resources + initial_resource * renewable_resource_percent * 0.1, initial_resource * renewable_resource_percent)

        # 绘制结果
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))
        axs[0].plot(hawk_fractions, label='Hawk Fraction')
        axs[0].plot(dove_fractions, label='Dove Fraction')
        axs[0].plot(mixed_fractions, label='Mixed Fraction')
        axs[0].set_xlabel('Generation')
        axs[0].set_ylabel('Strategy Fractions')
        axs[0].legend()

        axs[1].plot(resources, label='Available Resources')
        axs[1].set_xlabel('Generation')
        axs[1].set_ylabel('Resources')
        axs[1].legend()

        plt.tight_layout()
        plt.show()

def main():
    # 获取用户输入
    V = float(input("请输入资源的价值 V: "))
    C = float(input("请输入打斗的代价 C: "))
    population_size = int(input("请输入群体规模: "))
    initial_hawk_fraction = float(input("请输入初始鹰的比例 (0-1): "))
    initial_dove_fraction = float(input("请输入初始鸽的比例 (0-1): "))
    initial_mixed_fraction = float(input("请输入初始混合策略的比例 (0-1): "))
    num_generations = int(input("请输入模拟的代数: "))
    mutation_rate = float(input("请输入突变率 (0-1): "))
    initial_resource = float(input("请输入初始资源量: "))
    renewable_resource_percent = float(input("请输入可再生资源比例 (0-1): "))
    non_renewable_resource_percent = 1 - renewable_resource_percent  # 不可再生资源比例

    # 初始化群体并运行模拟
    population = Population(population_size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction)
    population.evolve(V, C, mutation_rate, num_generations, initial_resource, renewable_resource_percent, non_renewable_resource_percent)

if __name__ == "__main__":
    main()
