"""
Exercise 2: Understanding Nash Equilibrium

Nash Equilibrium is a central concept in game theory, named after John Nash.
It's a strategy profile where no player can improve their payoff by unilaterally
changing their strategy (assuming others keep their strategies fixed).

In this exercise, you'll implement a general Nash Equilibrium finder for 2-player games.

TODO: Complete the functions to find all Nash Equilibria in a game.
"""


def find_best_response_player1(player2_action, payoff_matrix):
    """
    Find player 1's best response to player 2's action.

    Args:
        player2_action: The action chosen by player 2
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        The action that maximizes player 1's payoff, given player 2's action

    TODO: Implement this function.
    """
    # Get all possible actions for player 1
    all_actions_p1 = set()
    for (a1, a2) in payoff_matrix.keys():
        all_actions_p1.add(a1)

    # TODO: Find the action that gives player 1 the highest payoff
    best_action = None
    best_payoff = float('-inf')

    for action in all_actions_p1:
        if (action, player2_action) in payoff_matrix:
            payoff = payoff_matrix[(action, player2_action)][0]
            if payoff > best_payoff:
                best_payoff = payoff
                best_action = action

    return best_action


def find_best_response_player2(player1_action, payoff_matrix):
    """
    Find player 2's best response to player 1's action.

    Args:
        player1_action: The action chosen by player 1
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        The action that maximizes player 2's payoff, given player 1's action

    TODO: Implement this function.
    """
    all_actions_p2 = set()
    for (a1, a2) in payoff_matrix.keys():
        all_actions_p2.add(a2)

    # TODO: Find the action that gives player 2 the highest payoff
    best_action = None
    best_payoff = float('-inf')

    for action in all_actions_p2:
        if (player1_action, action) in payoff_matrix:
            payoff = payoff_matrix[(player1_action, action)][1]
            if payoff > best_payoff:
                best_payoff = payoff
                best_action = action

    return best_action


def find_all_nash_equilibria(payoff_matrix):
    """
    Find all pure strategy Nash Equilibria in a 2-player game.

    A strategy profile (a1, a2) is a Nash Equilibrium if:
    - a1 is a best response to a2 (for player 1)
    - a2 is a best response to a1 (for player 2)

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        A list of tuples representing all Nash Equilibria

    TODO: Implement this function.
    HINT: Check every strategy profile to see if it's a Nash Equilibrium.
    """
    equilibria = []

    # TODO: Iterate through all strategy profiles and check if each is a Nash Equilibrium
    for (a1, a2) in payoff_matrix.keys():
        # Check if a1 is best response to a2
        br1 = find_best_response_player1(a2, payoff_matrix)
        # Check if a2 is best response to a1
        br2 = find_best_response_player2(a1, payoff_matrix)

        if br1 == a1 and br2 == a2:
            equilibria.append((a1, a2))

    return equilibria


def analyze_coordination_game():
    """
    Analyze the Battle of the Sexes game, which has multiple Nash Equilibria.

    Story: A couple wants to go out together. He prefers football, she prefers opera.
    But both prefer being together over being apart.

    Payoffs:
              Opera    Football
    Opera     (2, 1)   (0, 0)
    Football  (0, 0)   (1, 2)

    TODO: Create the payoff matrix and return it.
    """
    # TODO: Create and return the payoff matrix
    payoff = {
        ('Opera', 'Opera'): (2, 1),
        ('Opera', 'Football'): (0, 0),
        ('Football', 'Opera'): (0, 0),
        ('Football', 'Football'): (1, 2),
    }
    return payoff


def test_solution():
    """Test function - Do not modify."""
    # Test with Prisoner's Dilemma
    pd_payoff = {
        ('C', 'C'): (-1, -1),
        ('C', 'D'): (-5, 0),
        ('D', 'C'): (0, -5),
        ('D', 'D'): (-3, -3),
    }

    nash_pd = find_all_nash_equilibria(pd_payoff)
    assert len(nash_pd) == 1, "Prisoner's Dilemma should have exactly 1 Nash Equilibrium"
    assert ('D', 'D') in nash_pd, "Nash Equilibrium should be (D, D)"

    # Test with Battle of the Sexes
    bos_payoff = analyze_coordination_game()
    nash_bos = find_all_nash_equilibria(bos_payoff)
    assert len(nash_bos) == 2, "Battle of the Sexes should have exactly 2 Nash Equilibria"
    assert ('Opera', 'Opera') in nash_bos, "('Opera', 'Opera') should be a Nash Equilibrium"
    assert ('Football', 'Football') in nash_bos, "('Football', 'Football') should be a Nash Equilibrium"

    print("Great! You've successfully found Nash Equilibria!")
    print(f"Prisoner's Dilemma has {len(nash_pd)} Nash Equilibrium: {nash_pd}")
    print(f"Battle of the Sexes has {len(nash_bos)} Nash Equilibria: {nash_bos}")
    print("\nKey insight: Games can have 0, 1, or multiple Nash Equilibria!")

    return True


if __name__ == '__main__':
    test_solution()
