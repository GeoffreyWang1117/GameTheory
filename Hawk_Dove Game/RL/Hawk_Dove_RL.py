import numpy as np
import matplotlib.pyplot as plt

# 定义策略
HAWK = 0
DOVE = 1
STRATEGIES = [HAWK, DOVE]

# Q-Learning参数
ALPHA = 0.1  # 学习率
GAMMA = 0.95  # 折扣因子
EPSILON = 0.1  # 探索率

# 初始化策略
initial_hawk_fraction = 0.5  # 初始鹰的比例
initial_dove_fraction = 0.5  # 初始鸽的比例

# 确保比例之和为1
if initial_hawk_fraction + initial_dove_fraction != 1:
    raise ValueError("Initial Hawk and Dove fractions must sum to 1.")


class Individual:
    def __init__(self, strategy, num_strategies):
        self.strategy = strategy  # 初始策略
        self.q_table = np.zeros(num_strategies)  # 初始化Q表

    def choose_action(self):
        # 返回策略的整数索引
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
    def __init__(self, size, initial_hawk_fraction, initial_dove_fraction):
        strategies = ([HAWK] * int(size * initial_hawk_fraction) +
                      [DOVE] * int(size * initial_dove_fraction))
        self.individuals = [Individual(strategy, len(STRATEGIES)) for strategy in strategies]

    def evolve(self, V, C, mutation_rate, num_generations):
        hawk_fractions = []
        dove_fractions = []

        for gen in range(num_generations):
            hawk_fractions.append(sum(1 for ind in self.individuals if ind.strategy == HAWK) / len(self.individuals))
            dove_fractions.append(sum(1 for ind in self.individuals if ind.strategy == DOVE) / len(self.individuals))

            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent, action_self, action_opponent = self.individuals[i].play(opponent, V, C)

                next_max_q_self = np.max(self.individuals[i].q_table)
                self.individuals[i].update_q_value(action_self, payoff_self, next_max_q_self)

                if np.random.rand() < mutation_rate:
                    self.individuals[i].strategy = np.random.choice(STRATEGIES)

        return hawk_fractions, dove_fractions

def main():
    V = 50  # 资源价值
    C = 100  # 打斗代价
    population_size = 100  # 群体规模
    initial_hawk_fraction = 0.5  # 初始鹰的比例
    initial_dove_fraction = 0.5  # 初始鸽的比例
    num_generations = 1000  # 模拟的代数
    mutation_rate = 0.01  # 突变率

    population = Population(population_size, initial_hawk_fraction, initial_dove_fraction)
    hawk_fractions, dove_fractions = population.evolve(V, C, mutation_rate, num_generations)

    # 绘制结果
    plt.plot(hawk_fractions, label='Hawk Fraction')
    plt.plot(dove_fractions, label='Dove Fraction')
    plt.xlabel('Generation')
    plt.ylabel('Strategy Fractions')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
