import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = transition_matrix
        self.states = states
        self.current_state = np.random.choice(self.states)

    def next_state(self):
        index = self.states.index(self.current_state)
        self.current_state = np.random.choice(
            self.states, p=self.transition_matrix[index]
        )
        return self.current_state

    def simulate(self, steps):
        history = [self.current_state]
        for _ in range(steps):
            history.append(self.next_state())
        return history

    def analyze_sequence(self, history):
        state_counts = {state: 0 for state in self.states}
        state_streaks = {state: [] for state in self.states}
        current_streak = {state: 0 for state in self.states}
        
        for i, state in enumerate(history):
            state_counts[state] += 1
            for s in self.states:
                if s == state:
                    current_streak[s] += 1
                else:
                    if current_streak[s] > 0:
                        state_streaks[s].append(current_streak[s])
                    current_streak[s] = 0

        for s in self.states:
            if current_streak[s] > 0:
                state_streaks[s].append(current_streak[s])

        # 计算每个状态的出现频率
        total_steps = len(history)
        state_frequencies = {state: count / total_steps for state, count in state_counts.items()}
        
        # 输出分析结果
        print("\nStrategy Frequency:")
        for state, freq in state_frequencies.items():
            print(f"{state}: {freq:.2f}")

        print("\nStrategy Streaks (length of consecutive occurrences):")
        for state, streaks in state_streaks.items():
            print(f"{state}: {streaks}")

def main():
    # 马尔可夫链转移矩阵
    transition_matrix = [
        [0.6, 0.3, 0.1],  # Hawk -> [Hawk, Dove, Mixed]
        [0.4, 0.4, 0.2],  # Dove -> [Hawk, Dove, Mixed]
        [0.2, 0.5, 0.3],  # Mixed -> [Hawk, Dove, Mixed]
    ]
    states = ['Hawk', 'Dove', 'Mixed']

    # 创建马尔可夫链实例
    mc = MarkovChain(transition_matrix, states)

    # 模拟500步
    history = mc.simulate(500)

    # 分析策略序列
    mc.analyze_sequence(history)

if __name__ == "__main__":
    main()
