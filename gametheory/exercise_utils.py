"""
Utility functions and helpers for exercises.

These are helper functions students can use in their solutions.
"""

import numpy as np
from typing import Dict, List, Tuple, Any


def print_payoff_matrix(payoff_dict: Dict[Tuple, Tuple], player: int = None):
    """
    Pretty-print a payoff matrix.

    Args:
        payoff_dict: Dictionary mapping (action1, action2) -> (payoff1, payoff2)
        player: If specified, only show this player's payoffs
    """
    # Get actions
    actions1 = sorted(set(a1 for (a1, a2) in payoff_dict.keys()))
    actions2 = sorted(set(a2 for (a1, a2) in payoff_dict.keys()))

    # Print header
    header = "       "
    for a2 in actions2:
        header += f"{str(a2):>10}"
    print(header)
    print("-" * len(header))

    # Print rows
    for a1 in actions1:
        row = f"{str(a1):>5}  "
        for a2 in actions2:
            if (a1, a2) in payoff_dict:
                p1, p2 = payoff_dict[(a1, a2)]
                if player == 1:
                    cell = f"{p1:>10.2f}"
                elif player == 2:
                    cell = f"{p2:>10.2f}"
                else:
                    cell = f"({p1:.1f},{p2:.1f})"
                row += f"{cell:>10}"
            else:
                row += " "*10
        print(row)


def create_matrix_from_dict(payoff_dict: Dict[Tuple, Tuple], player: int = 1):
    """
    Convert payoff dictionary to numpy matrix.

    Args:
        payoff_dict: Dictionary mapping (action1, action2) -> (payoff1, payoff2)
        player: Which player's payoffs to extract

    Returns:
        Tuple of (matrix, row_actions, col_actions)
    """
    actions1 = sorted(set(a1 for (a1, a2) in payoff_dict.keys()))
    actions2 = sorted(set(a2 for (a1, a2) in payoff_dict.keys()))

    matrix = np.zeros((len(actions1), len(actions2)))

    for i, a1 in enumerate(actions1):
        for j, a2 in enumerate(actions2):
            if (a1, a2) in payoff_dict:
                payoff = payoff_dict[(a1, a2)]
                matrix[i, j] = payoff[player - 1]

    return matrix, actions1, actions2


def simulate_random_play(strategy1, strategy2, payoff_matrix, rounds=100):
    """
    Simulate random play between two strategies.

    Args:
        strategy1, strategy2: Strategy objects with choose() and update() methods
        payoff_matrix: Payoff dictionary
        rounds: Number of rounds to play

    Returns:
        Tuple of (total_payoff1, total_payoff2, history)
    """
    total1 = 0
    total2 = 0
    history = []

    for _ in range(rounds):
        a1 = strategy1.choose()
        a2 = strategy2.choose()

        p1, p2 = payoff_matrix[(a1, a2)]
        total1 += p1
        total2 += p2

        history.append((a1, a2, p1, p2))

        if hasattr(strategy1, 'update'):
            strategy1.update(a2)
        if hasattr(strategy2, 'update'):
            strategy2.update(a1)

    return total1, total2, history


def check_nash_equilibrium(strategy_profile: Tuple, payoff_matrix: Dict,
                           actions1: List, actions2: List) -> bool:
    """
    Check if a strategy profile is a Nash equilibrium.

    Args:
        strategy_profile: Tuple (action1, action2)
        payoff_matrix: Payoff dictionary
        actions1, actions2: Lists of available actions

    Returns:
        True if strategy profile is Nash equilibrium
    """
    a1_star, a2_star = strategy_profile
    p1_star, p2_star = payoff_matrix[(a1_star, a2_star)]

    # Check if player 1 wants to deviate
    for a1 in actions1:
        if a1 != a1_star:
            p1_dev, _ = payoff_matrix[(a1, a2_star)]
            if p1_dev > p1_star:
                return False

    # Check if player 2 wants to deviate
    for a2 in actions2:
        if a2 != a2_star:
            _, p2_dev = payoff_matrix[(a1_star, a2)]
            if p2_dev > p2_star:
                return False

    return True


def plot_strategy_evolution(history: List, title: str = "Strategy Evolution"):
    """
    Plot how strategies evolve over time (requires matplotlib).

    Args:
        history: List of strategy distributions over time
        title: Plot title
    """
    try:
        import matplotlib.pyplot as plt

        history_array = np.array(history)

        plt.figure(figsize=(10, 6))
        for i in range(history_array.shape[1]):
            plt.plot(history_array[:, i], label=f'Action {i}')

        plt.xlabel('Round')
        plt.ylabel('Probability')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    except ImportError:
        print("Matplotlib not available for plotting")


class SimpleStrategy:
    """Base class for simple strategies."""

    def __init__(self, name: str):
        self.name = name
        self.history = []
        self.opponent_history = []

    def choose(self):
        """Choose an action."""
        raise NotImplementedError

    def update(self, opponent_action):
        """Update based on opponent's action."""
        self.opponent_history.append(opponent_action)

    def reset(self):
        """Reset strategy state."""
        self.history = []
        self.opponent_history = []


# Common game payoff matrices for quick reference
PRISONERS_DILEMMA = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

BATTLE_OF_SEXES = {
    ('O', 'O'): (2, 1),
    ('O', 'F'): (0, 0),
    ('F', 'O'): (0, 0),
    ('F', 'F'): (1, 2),
}

STAG_HUNT = {
    ('S', 'S'): (5, 5),
    ('S', 'R'): (0, 3),
    ('R', 'S'): (3, 0),
    ('R', 'R'): (3, 3),
}

MATCHING_PENNIES = {
    ('H', 'H'): (1, -1),
    ('H', 'T'): (-1, 1),
    ('T', 'H'): (-1, 1),
    ('T', 'T'): (1, -1),
}


if __name__ == '__main__':
    # Demo usage
    print("Game Theory Exercise Utilities")
    print("=" * 50)

    print("\nPrisoner's Dilemma:")
    print_payoff_matrix(PRISONERS_DILEMMA)

    print("\nBattle of the Sexes:")
    print_payoff_matrix(BATTLE_OF_SEXES)

    print("\nChecking Nash equilibrium in Prisoner's Dilemma:")
    is_nash = check_nash_equilibrium(('D', 'D'), PRISONERS_DILEMMA, ['C', 'D'], ['C', 'D'])
    print(f"  (D, D) is Nash equilibrium: {is_nash}")
