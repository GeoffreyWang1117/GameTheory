"""
Exercise 1: The Prisoner's Dilemma

The Prisoner's Dilemma is the most famous game in game theory. Two prisoners are
arrested and interrogated separately. Each has two choices: Cooperate (stay silent)
or Defect (betray the other).

Payoff structure:
- Both cooperate: Each gets -1 year
- Both defect: Each gets -3 years
- One defects, one cooperates: Defector gets 0 years, cooperator gets -5 years

The dilemma: Individual rationality leads to a worse outcome for both!

TODO: Complete the functions below to implement the Prisoner's Dilemma game.
"""


def create_payoff_matrix():
    """
    Create and return the payoff matrix for the Prisoner's Dilemma.

    Return a dictionary where:
    - Keys are tuples (player1_action, player2_action)
    - Values are tuples (player1_payoff, player2_payoff)
    - Actions: 'C' for Cooperate, 'D' for Defect

    Example: payoff[('C', 'D')] = (-5, 0) means if P1 cooperates and P2 defects,
             P1 gets -5 and P2 gets 0

    TODO: Fill in the payoff values according to the game description above.
    """
    payoff = {
        ('C', 'C'): (-1, -1),  # Both cooperate
        ('C', 'D'): (-5, 0),   # P1 cooperates, P2 defects
        ('D', 'C'): (0, -5),   # P1 defects, P2 cooperates
        ('D', 'D'): (-3, -3),  # Both defect
    }
    return payoff


def find_nash_equilibrium(payoff_matrix):
    """
    Find the Nash Equilibrium of the Prisoner's Dilemma.

    A Nash Equilibrium is a strategy profile where no player can improve their
    payoff by unilaterally changing their strategy.

    Args:
        payoff_matrix: The payoff matrix dictionary

    Returns:
        A tuple (player1_action, player2_action) representing the Nash Equilibrium

    TODO: Implement logic to find and return the Nash Equilibrium.
    HINT: Check each strategy profile to see if either player wants to deviate.
    """
    # TODO: Replace this with your implementation
    # For each possible outcome, check if any player wants to deviate

    for (a1, a2), (p1, p2) in payoff_matrix.items():
        # Check if player 1 wants to deviate
        player1_wants_to_deviate = False
        for alt_action in ['C', 'D']:
            if alt_action != a1:
                alt_payoff = payoff_matrix[(alt_action, a2)][0]
                if alt_payoff > p1:
                    player1_wants_to_deviate = True
                    break

        # Check if player 2 wants to deviate
        player2_wants_to_deviate = False
        for alt_action in ['C', 'D']:
            if alt_action != a2:
                alt_payoff = payoff_matrix[(a1, alt_action)][1]
                if alt_payoff > p2:
                    player2_wants_to_deviate = True
                    break

        # If neither wants to deviate, it's a Nash Equilibrium
        if not player1_wants_to_deviate and not player2_wants_to_deviate:
            return (a1, a2)

    return None


def is_pareto_optimal(outcome, payoff_matrix):
    """
    Check if an outcome is Pareto optimal.

    An outcome is Pareto optimal if there's no other outcome that makes
    at least one player better off without making anyone worse off.

    Args:
        outcome: A tuple (player1_action, player2_action)
        payoff_matrix: The payoff matrix dictionary

    Returns:
        True if the outcome is Pareto optimal, False otherwise

    TODO: Implement the Pareto optimality check.
    HINT: Compare the outcome with all other outcomes in the payoff matrix.
    """
    current_payoff = payoff_matrix[outcome]

    # TODO: Implement your logic here
    for other_outcome, other_payoff in payoff_matrix.items():
        if other_outcome == outcome:
            continue

        # Check if other_outcome Pareto dominates current outcome
        # (at least one player better off, no player worse off)
        p1_better = other_payoff[0] > current_payoff[0]
        p2_better = other_payoff[1] > current_payoff[1]
        p1_not_worse = other_payoff[0] >= current_payoff[0]
        p2_not_worse = other_payoff[1] >= current_payoff[1]

        if (p1_better or p2_better) and p1_not_worse and p2_not_worse:
            return False

    return True


def test_solution():
    """Test function - Do not modify."""
    payoff = create_payoff_matrix()

    # Test payoff matrix
    assert payoff[('C', 'C')] == (-1, -1), "Incorrect payoff for (C, C)"
    assert payoff[('D', 'D')] == (-3, -3), "Incorrect payoff for (D, D)"
    assert payoff[('C', 'D')] == (-5, 0), "Incorrect payoff for (C, D)"
    assert payoff[('D', 'C')] == (0, -5), "Incorrect payoff for (D, C)"

    # Test Nash Equilibrium
    nash = find_nash_equilibrium(payoff)
    assert nash == ('D', 'D'), f"Expected Nash Equilibrium to be ('D', 'D'), got {nash}"

    # Test Pareto optimality
    assert is_pareto_optimal(('C', 'C'), payoff) == True, "('C', 'C') should be Pareto optimal"
    assert is_pareto_optimal(('D', 'D'), payoff) == False, "('D', 'D') should not be Pareto optimal"

    print("The Prisoner's Dilemma illustrates a key insight:")
    print("The Nash Equilibrium (D, D) is NOT Pareto optimal!")
    print("Both players would be better off cooperating, but individual rationality leads to defection.")

    return True


if __name__ == '__main__':
    test_solution()
