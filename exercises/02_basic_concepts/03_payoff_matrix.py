"""
Exercise 6: Working with Payoff Matrices

Payoff matrices are the fundamental tool for representing games.
In this exercise, you'll learn to manipulate and analyze them.

TODO: Implement functions for payoff matrix operations.
"""

import numpy as np


def create_matrix_form(payoff_dict, player=1):
    """
    Convert a payoff dictionary to a matrix (numpy array).

    Args:
        payoff_dict: Dictionary mapping (action1, action2) -> (payoff1, payoff2)
        player: Which player's payoffs to extract (1 or 2)

    Returns:
        tuple: (matrix, row_actions, col_actions)
               matrix is a 2D numpy array
               row_actions is a list of player 1's actions
               col_actions is a list of player 2's actions

    TODO: Implement the conversion.
    """
    # Get all unique actions
    actions1 = sorted(set(a1 for (a1, a2) in payoff_dict.keys()))
    actions2 = sorted(set(a2 for (a1, a2) in payoff_dict.keys()))

    # TODO: Create the matrix
    rows = len(actions1)
    cols = len(actions2)
    matrix = np.zeros((rows, cols))

    for i, a1 in enumerate(actions1):
        for j, a2 in enumerate(actions2):
            if (a1, a2) in payoff_dict:
                if player == 1:
                    matrix[i, j] = payoff_dict[(a1, a2)][0]
                else:
                    matrix[i, j] = payoff_dict[(a1, a2)][1]

    return matrix, actions1, actions2


def find_best_responses_matrix(payoff_matrix):
    """
    Find best response for each player for each opponent action.

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        Tuple of two dictionaries:
        - br1: maps player 2's action -> player 1's best response(s)
        - br2: maps player 1's action -> player 2's best response(s)

    TODO: Implement best response finder.
    """
    actions1 = sorted(set(a1 for (a1, a2) in payoff_matrix.keys()))
    actions2 = sorted(set(a2 for (a1, a2) in payoff_matrix.keys()))

    br1 = {}  # Player 1's best responses
    br2 = {}  # Player 2's best responses

    # TODO: Find best responses for player 1 (for each action of player 2)
    for a2 in actions2:
        best_payoff = float('-inf')
        best_actions = []

        for a1 in actions1:
            payoff = payoff_matrix[(a1, a2)][0]
            if payoff > best_payoff:
                best_payoff = payoff
                best_actions = [a1]
            elif payoff == best_payoff:
                best_actions.append(a1)

        br1[a2] = best_actions

    # TODO: Find best responses for player 2 (for each action of player 1)
    for a1 in actions1:
        best_payoff = float('-inf')
        best_actions = []

        for a2 in actions2:
            payoff = payoff_matrix[(a1, a2)][1]
            if payoff > best_payoff:
                best_payoff = payoff
                best_actions = [a2]
            elif payoff == best_payoff:
                best_actions.append(a2)

        br2[a1] = best_actions

    return br1, br2


def visualize_best_responses(payoff_matrix):
    """
    Create a string visualization showing best responses with asterisks.

    For each cell, mark with * if it's a best response for the row player,
    and ^ if it's a best response for the column player.

    TODO: Implement visualization.
    """
    br1, br2 = find_best_responses_matrix(payoff_matrix)

    actions1 = sorted(set(a1 for (a1, a2) in payoff_matrix.keys()))
    actions2 = sorted(set(a2 for (a1, a2) in payoff_matrix.keys()))

    # TODO: Create visualization
    result = []
    result.append("Payoff Matrix (* = best response for row player, ^ = best response for col player):\n")

    # Header
    header = "        "
    for a2 in actions2:
        header += f"{a2:>10}"
    result.append(header)

    # Rows
    for a1 in actions1:
        row = f"{a1:>6}  "
        for a2 in actions2:
            p1, p2 = payoff_matrix[(a1, a2)]
            markers = ""
            if a1 in br1[a2]:
                markers += "*"
            if a2 in br2[a1]:
                markers += "^"

            cell = f"({p1},{p2}){markers}"
            row += f"{cell:>10}"
        result.append(row)

    return "\n".join(result)


def iterated_elimination_of_dominated_strategies(payoff_matrix):
    """
    Perform iterated elimination of strictly dominated strategies.

    A strategy is strictly dominated if there exists another strategy that
    always gives a strictly better payoff, regardless of opponent's action.

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        Dictionary with dominated strategies eliminated

    TODO: Implement IEDS (Iterated Elimination of Dominated Strategies).
    """
    remaining = dict(payoff_matrix)

    changed = True
    while changed:
        changed = False

        actions1 = set(a1 for (a1, a2) in remaining.keys())
        actions2 = set(a2 for (a1, a2) in remaining.keys())

        # Check for dominated strategies for player 1
        for a1 in list(actions1):
            for a1_alt in actions1:
                if a1 == a1_alt:
                    continue

                # Check if a1 is strictly dominated by a1_alt
                dominated = True
                strictly_better_for_at_least_one = False

                for a2 in actions2:
                    if (a1, a2) not in remaining or (a1_alt, a2) not in remaining:
                        continue

                    payoff_a1 = remaining[(a1, a2)][0]
                    payoff_a1_alt = remaining[(a1_alt, a2)][0]

                    if payoff_a1_alt <= payoff_a1:
                        dominated = False
                        break
                    if payoff_a1_alt > payoff_a1:
                        strictly_better_for_at_least_one = True

                if dominated and strictly_better_for_at_least_one:
                    # Remove a1
                    remaining = {k: v for k, v in remaining.items() if k[0] != a1}
                    changed = True
                    break

        # Check for dominated strategies for player 2
        actions1 = set(a1 for (a1, a2) in remaining.keys())
        actions2 = set(a2 for (a1, a2) in remaining.keys())

        for a2 in list(actions2):
            for a2_alt in actions2:
                if a2 == a2_alt:
                    continue

                # Check if a2 is strictly dominated by a2_alt
                dominated = True
                strictly_better_for_at_least_one = False

                for a1 in actions1:
                    if (a1, a2) not in remaining or (a1, a2_alt) not in remaining:
                        continue

                    payoff_a2 = remaining[(a1, a2)][1]
                    payoff_a2_alt = remaining[(a1, a2_alt)][1]

                    if payoff_a2_alt <= payoff_a2:
                        dominated = False
                        break
                    if payoff_a2_alt > payoff_a2:
                        strictly_better_for_at_least_one = True

                if dominated and strictly_better_for_at_least_one:
                    # Remove a2
                    remaining = {k: v for k, v in remaining.items() if k[1] != a2}
                    changed = True
                    break

    return remaining


def test_solution():
    """Test function - Do not modify."""
    payoff = {
        ('U', 'L'): (3, 1),
        ('U', 'R'): (0, 0),
        ('M', 'L'): (1, 0),
        ('M', 'R'): (2, 3),
        ('D', 'L'): (0, 2),
        ('D', 'R'): (1, 1),
    }

    # Test matrix conversion
    matrix1, rows, cols = create_matrix_form(payoff, player=1)
    assert matrix1.shape == (3, 2), "Matrix should be 3x2"
    assert rows == ['D', 'M', 'U'], f"Rows should be ['D', 'M', 'U'], got {rows}"

    # Test best responses
    br1, br2 = find_best_responses_matrix(payoff)
    assert 'U' in br1['L'], "U should be a best response to L"
    assert 'M' in br1['R'], "M should be a best response to R"

    # Test visualization
    viz = visualize_best_responses(payoff)
    assert '*' in viz, "Visualization should mark best responses"
    print("\n" + viz + "\n")

    # Test IEDS
    game_with_dominated = {
        ('A', 'X'): (1, 1),
        ('A', 'Y'): (0, 0),
        ('B', 'X'): (2, 0),
        ('B', 'Y'): (1, 2),
        ('C', 'X'): (0, 1),
        ('C', 'Y'): (0, 1),
    }

    reduced = iterated_elimination_of_dominated_strategies(game_with_dominated)
    actions1_remaining = set(a1 for (a1, a2) in reduced.keys())

    # C is dominated by both A and B, should be eliminated
    assert 'C' not in actions1_remaining, "C should be eliminated (dominated)"

    print("Excellent! You can now work with payoff matrices!")
    print("\nKey insights:")
    print("1. Payoff matrices provide a clear representation of strategic interactions")
    print("2. Best response analysis helps identify Nash Equilibria")
    print("3. IEDS can simplify games by eliminating irrational strategies")

    return True


if __name__ == '__main__':
    test_solution()
