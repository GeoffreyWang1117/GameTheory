import numpy as np
import matplotlib.pyplot as plt

# 定义策略
HAWK = 0
DOVE = 1
MIXED = 2
STRATEGIES = [HAWK, DOVE, MIXED]

# Q-Learning参数
ALPHA = 0.1  # 学习率
GAMMA = 0.95  # 折扣因子
EPSILON = 0.1  # 探索率
MUTATION_RATE = 0.01  # 突变率

class Individual:
    def __init__(self, strategy, num_strategies):
        self.strategy = strategy  # 初始策略
        self.q_table = np.zeros(num_strategies)  # 初始化Q表

    def choose_action(self):
        # 混合策略时，按Q值的比例选择鹰或鸽
        if self.strategy == MIXED:
            hawk_q = max(self.q_table[HAWK], 0)  # 确保Q值为非负数
            dove_q = max(self.q_table[DOVE], 0)  # 确保Q值为非负数
            total_q = hawk_q + dove_q + 1e-6  # 避免除以零
            hawk_prob = hawk_q / total_q
            return np.random.choice([HAWK, DOVE], p=[hawk_prob, 1 - hawk_prob])
        
        # 普通策略
        if np.random.rand() < EPSILON:
            return np.random.choice(STRATEGIES)  # 返回整数索引
        else:
            return np.argmax(self.q_table)

    def update_q_value(self, action, reward, next_max_q):
        self.q_table[action] += ALPHA * (reward + GAMMA * next_max_q - self.q_table[action])

    def play(self, opponent, V, C):
        action_self = self.choose_action()
        action_opponent = opponent.choose_action()

        if action_self == HAWK and action_opponent == HAWK:
            return (V - C) / 2, (V - C) / 2, action_self, action_opponent
        elif action_self == HAWK and action_opponent == DOVE:
            return V, 0, action_self, action_opponent
        elif action_self == DOVE and action_opponent == HAWK:
            return 0, V, action_self, action_opponent
        elif action_self == DOVE and action_opponent == DOVE:
            return V / 2, V / 2, action_self, action_opponent
        else:
            return 0, 0, action_self, action_opponent

class Population:
    def __init__(self, size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction):
        strategies = ([HAWK] * int(size * initial_hawk_fraction) +
                      [DOVE] * int(size * initial_dove_fraction) +
                      [MIXED] * int(size * initial_mixed_fraction))
        self.individuals = [Individual(strategy, len(STRATEGIES)) for strategy in strategies]

    def normalize_strategies(self):
        hawks = sum(1 for ind in self.individuals if ind.strategy == HAWK)
        doves = sum(1 for ind in self.individuals if ind.strategy == DOVE)
        mixed = sum(1 for ind in self.individuals if ind.strategy == MIXED)
        
        total = hawks + doves + mixed
        
        # 计算新的比例
        hawk_fraction = hawks / total
        dove_fraction = doves / total
        mixed_fraction = mixed / total
        
        return hawk_fraction, dove_fraction, mixed_fraction

    def resample_strategies(self, hawk_fraction, dove_fraction, mixed_fraction):
        size = len(self.individuals)
        strategies = ([HAWK] * int(size * hawk_fraction) +
                      [DOVE] * int(size * dove_fraction) +
                      [MIXED] * int(size * mixed_fraction))
        
        # 如果人数有偏差，进行微调
        while len(strategies) < size:
            strategies.append(np.random.choice(STRATEGIES))
        while len(strategies) > size:
            strategies.pop()

        for i in range(size):
            self.individuals[i].strategy = strategies[i]

    def evolve(self, V, C, mutation_rate, num_generations):
        hawk_fractions = []
        dove_fractions = []
        mixed_fractions = []

        for gen in range(num_generations):
            hawk_fraction, dove_fraction, mixed_fraction = self.normalize_strategies()
            hawk_fractions.append(hawk_fraction)
            dove_fractions.append(dove_fraction)
            mixed_fractions.append(mixed_fraction)

            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent, action_self, action_opponent = self.individuals[i].play(opponent, V, C)

                next_max_q_self = np.max(self.individuals[i].q_table)
                self.individuals[i].update_q_value(action_self, payoff_self, next_max_q_self)

                # 发生突变
                if np.random.rand() < mutation_rate:
                    self.individuals[i].strategy = np.random.choice(STRATEGIES)

            # 每代结束后重新采样策略分布，确保比例和为1
            hawk_fraction, dove_fraction, mixed_fraction = self.normalize_strategies()
            self.resample_strategies(hawk_fraction, dove_fraction, mixed_fraction)

        return hawk_fractions, dove_fractions, mixed_fractions

def main():
    V = 50  # 资源价值
    C = 100  # 打斗代价
    population_size = 100  # 群体规模
    initial_hawk_fraction = 0.3  # 初始鹰的比例
    initial_dove_fraction = 0.3  # 初始鸽的比例
    initial_mixed_fraction = 0.4  # 初始混合策略的比例
    num_generations = 1000  # 模拟的代数
    mutation_rate = 0.01  # 突变率

    population = Population(population_size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction)
    hawk_fractions, dove_fractions, mixed_fractions = population.evolve(V, C, mutation_rate, num_generations)

    # 绘制结果
    plt.plot(hawk_fractions, label='Hawk Fraction')
    plt.plot(dove_fractions, label='Dove Fraction')
    plt.plot(mixed_fractions, label='Mixed Fraction')
    plt.xlabel('Generation')
    plt.ylabel('Strategy Fractions')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
