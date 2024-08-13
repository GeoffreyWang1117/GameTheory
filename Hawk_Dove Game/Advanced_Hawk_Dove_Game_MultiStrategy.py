import numpy as np
import matplotlib.pyplot as plt

class Individual:
    def __init__(self, strategy):
        self.strategy = strategy  # 'Hawk', 'Dove' or 'Mixed'

    def play(self, opponent, V, C):
        if self.strategy == 'Hawk' and opponent.strategy == 'Hawk':
            return (V - C) / 2, (V - C) / 2
        elif self.strategy == 'Hawk' and opponent.strategy == 'Dove':
            return V, 0
        elif self.strategy == 'Dove' and opponent.strategy == 'Hawk':
            return 0, V
        elif self.strategy == 'Dove' and opponent.strategy == 'Dove':
            return V / 2, V / 2
        elif self.strategy == 'Mixed':
            # 混合策略，根据一定概率选择鹰或鸽策略
            self_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return Individual(self_choice).play(opponent, V, C)
        elif opponent.strategy == 'Mixed':
            # 对手为混合策略
            opponent_choice = np.random.choice(['Hawk', 'Dove'], p=[0.5, 0.5])
            return self.play(Individual(opponent_choice), V, C)
        else:
            # 防止没有返回值的情况，保证返回一个默认值
            return 0, 0

class Population:
    def __init__(self, size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction):
        strategies = (['Hawk'] * int(size * initial_hawk_fraction) +
                      ['Dove'] * int(size * initial_dove_fraction) +
                      ['Mixed'] * int(size * initial_mixed_fraction))
        self.individuals = [Individual(strategy) for strategy in strategies]

    def evolve(self, V, C, mutation_rate, num_generations):
        hawk_fractions = []
        dove_fractions = []
        mixed_fractions = []

        for _ in range(num_generations):
            # Pairwise interactions
            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent = self.individuals[i].play(opponent, V, C)

                # 突变机制
                if np.random.rand() < mutation_rate:
                    self.individuals[i].strategy = np.random.choice(['Hawk', 'Dove', 'Mixed'])

            # Calculate current strategy fractions
            hawk_count = sum(1 for ind in self.individuals if ind.strategy == 'Hawk')
            dove_count = sum(1 for ind in self.individuals if ind.strategy == 'Dove')
            mixed_count = sum(1 for ind in self.individuals if ind.strategy == 'Mixed')

            hawk_fraction = hawk_count / len(self.individuals)
            dove_fraction = dove_count / len(self.individuals)
            mixed_fraction = mixed_count / len(self.individuals)

            hawk_fractions.append(hawk_fraction)
            dove_fractions.append(dove_fraction)
            mixed_fractions.append(mixed_fraction)

        # Plot results
        plt.plot(hawk_fractions, label='Hawk Fraction')
        plt.plot(dove_fractions, label='Dove Fraction')
        plt.plot(mixed_fractions, label='Mixed Fraction')
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
    initial_mixed_fraction = float(input("请输入初始混合策略的比例 (0-1): "))
    num_generations = int(input("请输入模拟的代数: "))
    mutation_rate = float(input("请输入突变率 (0-1): "))

    # 初始化群体并运行模拟
    population = Population(population_size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction)
    population.evolve(V, C, mutation_rate, num_generations)

if __name__ == "__main__":
    main()
