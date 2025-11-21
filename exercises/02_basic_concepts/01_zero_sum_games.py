"""
Exercise 4: Zero-Sum Games

A zero-sum game is one where the total payoff to all players sums to zero for every outcome.
One player's gain is exactly another player's loss.

Examples: Chess, poker, matching pennies

In zero-sum games, we can use the minimax theorem to find optimal mixed strategies.

TODO: Implement functions to analyze zero-sum games.
"""


def is_zero_sum_game(payoff_matrix):
    """
    Check if a game is zero-sum.

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        True if the game is zero-sum, False otherwise

    TODO: Implement this function.
    HINT: Check if payoff1 + payoff2 = 0 for all outcomes.
    """
    # TODO: Check if all payoffs sum to zero
    for (a1, a2), (p1, p2) in payoff_matrix.items():
        if abs(p1 + p2) > 0.0001:  # Use small epsilon for floating point comparison
            return False
    return True


def find_saddle_point(payoff_matrix):
    """
    Find the saddle point in a zero-sum game if it exists.

    A saddle point is an outcome that is simultaneously:
    - A maximum in its column (best for row player given column)
    - A minimum in its row (worst for column player given row)

    If a saddle point exists, it's a pure strategy Nash Equilibrium.

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> payoff1
                       (we only need player 1's payoff for zero-sum games)

    Returns:
        Tuple (action1, action2, value) if saddle point exists, None otherwise

    TODO: Implement saddle point detection.
    """
    # Get all actions
    actions_p1 = set()
    actions_p2 = set()
    for (a1, a2) in payoff_matrix.keys():
        actions_p1.add(a1)
        actions_p2.add(a2)

    # TODO: Find saddle point
    # For each outcome, check if it's a row min and column max

    for a1 in actions_p1:
        for a2 in actions_p2:
            value = payoff_matrix[(a1, a2)][0]

            # Check if it's minimum in its row (worst for p1 if p2 changes strategy)
            is_row_min = True
            for other_a2 in actions_p2:
                if payoff_matrix[(a1, other_a2)][0] < value:
                    is_row_min = False
                    break

            # Check if it's maximum in its column (best for p1 if p1 changes strategy)
            is_col_max = True
            for other_a1 in actions_p1:
                if payoff_matrix[(other_a1, a2)][0] > value:
                    is_col_max = False
                    break

            if is_row_min and is_col_max:
                return (a1, a2, value)

    return None


def matching_pennies_game():
    """
    Create the Matching Pennies game.

    Two players simultaneously show a penny. Each chooses Heads or Tails.
    - If they match, Player 1 wins (gets +1, Player 2 gets -1)
    - If they don't match, Player 2 wins (gets +1, Player 1 gets -1)

    TODO: Create and return the payoff matrix.
    """
    # TODO: Create the payoff matrix
    payoff = {
        ('H', 'H'): (1, -1),
        ('H', 'T'): (-1, 1),
        ('T', 'H'): (-1, 1),
        ('T', 'T'): (1, -1),
    }
    return payoff


def rock_paper_scissors_game():
    """
    Create the Rock-Paper-Scissors game.

    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock
    - Same choice = tie

    Winner gets +1, loser gets -1, tie gives 0 to both.

    TODO: Create and return the payoff matrix.
    """
    # TODO: Create the payoff matrix
    payoff = {
        ('R', 'R'): (0, 0),
        ('R', 'P'): (-1, 1),
        ('R', 'S'): (1, -1),
        ('P', 'R'): (1, -1),
        ('P', 'P'): (0, 0),
        ('P', 'S'): (-1, 1),
        ('S', 'R'): (-1, 1),
        ('S', 'P'): (1, -1),
        ('S', 'S'): (0, 0),
    }
    return payoff


def test_solution():
    """Test function - Do not modify."""
    # Test zero-sum detection
    pd_payoff = {
        ('C', 'C'): (-1, -1),
        ('C', 'D'): (-5, 0),
        ('D', 'C'): (0, -5),
        ('D', 'D'): (-3, -3),
    }
    assert is_zero_sum_game(pd_payoff) == False, "Prisoner's Dilemma is not zero-sum"

    mp_payoff = matching_pennies_game()
    assert is_zero_sum_game(mp_payoff) == True, "Matching Pennies should be zero-sum"

    # Test saddle point
    saddle = find_saddle_point(mp_payoff)
    assert saddle is None, "Matching Pennies has no saddle point (no pure strategy equilibrium)"

    rps_payoff = rock_paper_scissors_game()
    assert is_zero_sum_game(rps_payoff) == True, "Rock-Paper-Scissors should be zero-sum"

    rps_saddle = find_saddle_point(rps_payoff)
    assert rps_saddle is None, "Rock-Paper-Scissors has no saddle point"

    # Test a game with saddle point
    game_with_saddle = {
        ('A', 'X'): (3, -3),
        ('A', 'Y'): (2, -2),
        ('B', 'X'): (1, -1),
        ('B', 'Y'): (4, -4),
    }
    saddle = find_saddle_point(game_with_saddle)
    assert saddle is not None, "This game should have a saddle point"
    assert saddle == ('A', 'Y', 2) or saddle == ('B', 'X', 1), f"Unexpected saddle point: {saddle}"

    print("Great work on zero-sum games!")
    print("\nKey insights:")
    print("1. Zero-sum games are purely competitive (one's gain = other's loss)")
    print("2. Not all zero-sum games have pure strategy equilibria (saddle points)")
    print("3. Games without saddle points require mixed strategies (randomization)")

    return True


if __name__ == '__main__':
    test_solution()
