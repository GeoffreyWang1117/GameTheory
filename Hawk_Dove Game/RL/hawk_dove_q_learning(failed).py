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

class Individual:
    def __init__(self, strategy, num_strategies):
        self.strategy = strategy
        self.q_table = np.random.rand(num_strategies) * 10  # 初始化Q表为随机值

    def choose_action(self):
        if np.random.rand() < EPSILON:
            return np.random.choice(STRATEGIES)
        else:
            return np.argmax(self.q_table)

    def update_q_value(self, action, reward, next_max_q):
        if action is None:
            raise ValueError("Action cannot be None")

        action = int(action)

        print(f"Updating Q-value for action: {action}, reward: {reward}, next_max_q: {next_max_q}")
        print(f"Q-table before update: {self.q_table}")
        print(f"Q-table length: {len(self.q_table)}")
        print(f"Action type: {type(action)}, Q-table type: {type(self.q_table)}, Reward type: {type(reward)}")

        if 0 <= action < len(self.q_table):
            self.q_table[action] += ALPHA * (reward + GAMMA * next_max_q - self.q_table[action])
            print(f"Q-table after update: {self.q_table}")
        else:
            print(f"Invalid action index: {action}, expected between 0 and {len(self.q_table)-1}")
            raise ValueError("Invalid action index")

    def play(self, opponent, V, C, available_resource):
        # 即使资源耗尽，也返回默认策略选择
        action_self = self.choose_action()
        action_opponent = opponent.choose_action()

        if available_resource <= 0:
            print(f"No available resources, but continuing with default actions: {action_self}, {action_opponent}")
            return 0, 0, action_self, action_opponent

        if action_self == MIXED:
            action_self = np.random.choice([HAWK, DOVE])
        if action_opponent == MIXED:
            action_opponent = np.random.choice([HAWK, DOVE])

        print(f"action_self: {action_self}, action_opponent: {action_opponent}")

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
        strategies = (['Hawk'] * int(size * initial_hawk_fraction) +
                      ['Dove'] * int(size * initial_dove_fraction) +
                      ['Mixed'] * int(size * initial_mixed_fraction))
        self.individuals = [Individual(strategy, len(STRATEGIES)) for strategy in strategies]

    def evolve(self, V, C, mutation_rate, num_generations, initial_resource, renewable_resource_percent, non_renewable_resource_percent, renewable_recovery_amount):
        hawk_fractions = []
        dove_fractions = []
        mixed_fractions = []
        renewable_resources = initial_resource * renewable_resource_percent
        non_renewable_resources = initial_resource * non_renewable_resource_percent
        resources = []  # 记录每一代剩余资源

        for gen in range(num_generations):
            hawk_fractions.append(sum(1 for ind in self.individuals if ind.strategy == HAWK) / len(self.individuals))
            dove_fractions.append(sum(1 for ind in self.individuals if ind.strategy == DOVE) / len(self.individuals))
            mixed_fractions.append(sum(1 for ind in self.individuals if ind.strategy == MIXED) / len(self.individuals))

            total_resources = renewable_resources + non_renewable_resources

            for i in range(len(self.individuals)):
                opponent = np.random.choice(self.individuals)
                payoff_self, payoff_opponent, action_self, action_opponent = self.individuals[i].play(opponent, V, C, total_resources)

                # 确保更新Q值时传递的是整数索引
                next_max_q_self = np.max(self.individuals[i].q_table)
                next_max_q_opponent = np.max(opponent.q_table)
                self.individuals[i].update_q_value(action_self, payoff_self, next_max_q_self)
                opponent.update_q_value(action_opponent, payoff_opponent, next_max_q_opponent)

                # 更新资源
                total_payoff = payoff_self + payoff_opponent
                if total_payoff > 0:
                    if non_renewable_resources >= total_payoff:
                        non_renewable_resources -= total_payoff
                    else:
                        total_payoff -= non_renewable_resources
                        non_renewable_resources = 0
                        renewable_resources -= total_payoff

            # 确保每一代都进行资源恢复
            renewable_resources = min(renewable_resources + renewable_recovery_amount, initial_resource * renewable_resource_percent)

            resources.append(total_resources)

        return hawk_fractions, dove_fractions, mixed_fractions, resources


def main():
    V = 50
    C = 100
    population_size = 100
    initial_hawk_fraction = 0.1
    initial_dove_fraction = 0.7
    initial_mixed_fraction = 0.2
    num_generations = 1000
    mutation_rate = 0.05
    initial_resource = 1000
    renewable_resource_percent = 0.7
    renewable_recovery_amount = 300  # 可再生资源每一代都恢复

    population = Population(population_size, initial_hawk_fraction, initial_dove_fraction, initial_mixed_fraction)
    hawk_fractions, dove_fractions, mixed_fractions, resources = population.evolve(
        V, C, mutation_rate, num_generations, initial_resource, renewable_resource_percent,
        1 - renewable_resource_percent, renewable_recovery_amount
    )

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

if __name__ == "__main__":
    main()
