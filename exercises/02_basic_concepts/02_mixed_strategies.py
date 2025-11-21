"""
Exercise 5: Mixed Strategies

A mixed strategy is a probability distribution over pure strategies.
Instead of always choosing the same action, a player randomizes.

For example, in Rock-Paper-Scissors, the optimal strategy is to play
each option with probability 1/3.

TODO: Implement functions to work with mixed strategies.
"""

import random


class MixedStrategy:
    """Represents a mixed strategy as a probability distribution over actions."""

    def __init__(self, probabilities):
        """
        Initialize a mixed strategy.

        Args:
            probabilities: Dictionary mapping actions to probabilities
                          Example: {'H': 0.6, 'T': 0.4}

        TODO: Validate that probabilities sum to 1.0 (within small tolerance).
        """
        self.probabilities = probabilities

        # TODO: Validate that probabilities sum to approximately 1.0
        total = sum(probabilities.values())
        assert abs(total - 1.0) < 0.0001, f"Probabilities must sum to 1.0, got {total}"

    def sample(self):
        """
        Sample an action according to the probability distribution.

        Returns:
            A randomly chosen action according to the probabilities

        TODO: Implement random sampling.
        HINT: Use random.random() and iterate through probabilities.
        """
        # TODO: Implement sampling
        r = random.random()
        cumulative = 0.0

        for action, prob in self.probabilities.items():
            cumulative += prob
            if r < cumulative:
                return action

        # Fallback (should not reach here if probabilities sum to 1)
        return list(self.probabilities.keys())[-1]


def expected_payoff(strategy1, strategy2, payoff_matrix, player):
    """
    Calculate expected payoff for a player given both players' mixed strategies.

    Args:
        strategy1: MixedStrategy for player 1
        strategy2: MixedStrategy for player 2
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)
        player: 1 or 2

    Returns:
        Expected payoff for the specified player

    TODO: Implement expected payoff calculation.
    HINT: Sum over all action pairs, weighted by their joint probability.
    """
    # TODO: Calculate expected payoff
    expected = 0.0

    for a1, prob1 in strategy1.probabilities.items():
        for a2, prob2 in strategy2.probabilities.items():
            joint_prob = prob1 * prob2
            if player == 1:
                payoff = payoff_matrix[(a1, a2)][0]
            else:
                payoff = payoff_matrix[(a1, a2)][1]

            expected += joint_prob * payoff

    return expected


def find_mixed_strategy_equilibrium_matching_pennies():
    """
    Find the mixed strategy Nash Equilibrium for Matching Pennies.

    In Matching Pennies:
    - Player 1 wants to match
    - Player 2 wants to mismatch

    The equilibrium is for both players to play 50-50.

    TODO: Return the equilibrium mixed strategies for both players.
    """
    # TODO: Create the equilibrium mixed strategies
    strategy1 = MixedStrategy({'H': 0.5, 'T': 0.5})
    strategy2 = MixedStrategy({'H': 0.5, 'T': 0.5})

    return strategy1, strategy2


def find_mixed_strategy_equilibrium_rock_paper_scissors():
    """
    Find the mixed strategy Nash Equilibrium for Rock-Paper-Scissors.

    By symmetry, each action should be played with equal probability.

    TODO: Return the equilibrium mixed strategy.
    """
    # TODO: Create the equilibrium mixed strategy
    strategy = MixedStrategy({'R': 1/3, 'P': 1/3, 'S': 1/3})
    return strategy


def is_best_response_to(strategy1, strategy2, payoff_matrix, player):
    """
    Check if strategy1 is a best response to strategy2 for the given player.

    A strategy is a best response if no other strategy gives higher expected payoff.

    Args:
        strategy1: MixedStrategy being tested
        strategy2: Opponent's MixedStrategy
        payoff_matrix: The game's payoff matrix
        player: 1 or 2

    Returns:
        True if strategy1 is a best response to strategy2

    TODO: Implement best response check for mixed strategies.
    HINT: It's sufficient to check if any pure strategy gives higher payoff.
    """
    current_payoff = expected_payoff(strategy1, strategy2, payoff_matrix, player)

    # TODO: Check if any pure strategy gives higher expected payoff
    actions = list(strategy1.probabilities.keys())

    for action in actions:
        # Create a pure strategy (probability 1 for this action)
        pure_strategy = MixedStrategy({a: (1.0 if a == action else 0.0) for a in actions})

        if player == 1:
            alternative_payoff = expected_payoff(pure_strategy, strategy2, payoff_matrix, 1)
        else:
            alternative_payoff = expected_payoff(strategy1, pure_strategy, payoff_matrix, 2)

        if alternative_payoff > current_payoff + 0.0001:  # Small tolerance for floating point
            return False

    return True


def test_solution():
    """Test function - Do not modify."""
    # Test mixed strategy creation and sampling
    ms = MixedStrategy({'H': 0.7, 'T': 0.3})
    samples = [ms.sample() for _ in range(1000)]
    h_count = samples.count('H')
    assert 650 < h_count < 750, "Sampling should be close to 70% H"

    # Test expected payoff
    payoff_matrix = {
        ('H', 'H'): (1, -1),
        ('H', 'T'): (-1, 1),
        ('T', 'H'): (-1, 1),
        ('T', 'T'): (1, -1),
    }

    s1 = MixedStrategy({'H': 0.5, 'T': 0.5})
    s2 = MixedStrategy({'H': 0.5, 'T': 0.5})

    ep1 = expected_payoff(s1, s2, payoff_matrix, 1)
    ep2 = expected_payoff(s1, s2, payoff_matrix, 2)

    assert abs(ep1) < 0.0001, "Expected payoff should be 0 for both in equilibrium"
    assert abs(ep2) < 0.0001, "Expected payoff should be 0 for both in equilibrium"

    # Test equilibrium
    eq1, eq2 = find_mixed_strategy_equilibrium_matching_pennies()
    assert is_best_response_to(eq1, eq2, payoff_matrix, 1), "Should be best response"
    assert is_best_response_to(eq2, eq1, payoff_matrix, 2), "Should be best response"

    # Test RPS
    rps_payoff = {
        ('R', 'R'): (0, 0), ('R', 'P'): (-1, 1), ('R', 'S'): (1, -1),
        ('P', 'R'): (1, -1), ('P', 'P'): (0, 0), ('P', 'S'): (-1, 1),
        ('S', 'R'): (-1, 1), ('S', 'P'): (1, -1), ('S', 'S'): (0, 0),
    }

    rps_eq = find_mixed_strategy_equilibrium_rock_paper_scissors()
    ep_rps = expected_payoff(rps_eq, rps_eq, rps_payoff, 1)
    assert abs(ep_rps) < 0.0001, "RPS equilibrium should give payoff 0"

    print("Excellent! You understand mixed strategies!")
    print("\nKey insights:")
    print("1. Mixed strategies allow us to find equilibria in games with no pure strategy equilibrium")
    print("2. In equilibrium, a player must be indifferent between all actions in their support")
    print("3. Randomization can be optimal even with complete information!")

    return True


if __name__ == '__main__':
    test_solution()
