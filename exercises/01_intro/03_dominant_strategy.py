"""
Exercise 3: Dominant Strategies

A dominant strategy is a strategy that is always better than any other strategy,
regardless of what the opponent does.

Types:
- Strictly dominant: ALWAYS gives a strictly better payoff
- Weakly dominant: ALWAYS gives at least as good a payoff, and sometimes better

If both players have dominant strategies, the game is very easy to solve!

TODO: Implement functions to detect dominant strategies.
"""


def get_player_actions(payoff_matrix, player):
    """
    Get all possible actions for a player.

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)
        player: 1 or 2

    Returns:
        Set of all possible actions for the specified player
    """
    actions = set()
    for (a1, a2) in payoff_matrix.keys():
        if player == 1:
            actions.add(a1)
        else:
            actions.add(a2)
    return actions


def is_strictly_dominant(action, player, payoff_matrix):
    """
    Check if an action is strictly dominant for a player.

    An action is strictly dominant if it gives a STRICTLY better payoff than
    any other action, regardless of what the opponent does.

    Args:
        action: The action to check
        player: 1 or 2
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        True if the action is strictly dominant, False otherwise

    TODO: Implement this function.
    HINT: Compare the action with all other actions against every opponent action.
    """
    player_actions = get_player_actions(payoff_matrix, player)
    other_actions = player_actions - {action}

    if not other_actions:
        return False

    # Get all opponent actions
    opponent_actions = get_player_actions(payoff_matrix, 3 - player)

    # TODO: For each opponent action, check if 'action' gives strictly better payoff
    # than all other actions

    for opp_action in opponent_actions:
        # Get payoff for the candidate dominant strategy
        if player == 1:
            candidate_payoff = payoff_matrix[(action, opp_action)][0]
        else:
            candidate_payoff = payoff_matrix[(opp_action, action)][1]

        # Check if any other action gives >= payoff
        for other_action in other_actions:
            if player == 1:
                other_payoff = payoff_matrix[(other_action, opp_action)][0]
            else:
                other_payoff = payoff_matrix[(opp_action, other_action)][1]

            if other_payoff >= candidate_payoff:
                return False

    return True


def is_weakly_dominant(action, player, payoff_matrix):
    """
    Check if an action is weakly dominant for a player.

    An action is weakly dominant if it gives at least as good a payoff as
    any other action for ALL opponent actions, and strictly better for at least one.

    Args:
        action: The action to check
        player: 1 or 2
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        True if the action is weakly dominant, False otherwise

    TODO: Implement this function.
    """
    player_actions = get_player_actions(payoff_matrix, player)
    other_actions = player_actions - {action}

    if not other_actions:
        return False

    opponent_actions = get_player_actions(payoff_matrix, 3 - player)

    strictly_better_for_at_least_one = False

    # TODO: Check weak dominance conditions
    for opp_action in opponent_actions:
        if player == 1:
            candidate_payoff = payoff_matrix[(action, opp_action)][0]
        else:
            candidate_payoff = payoff_matrix[(opp_action, action)][1]

        for other_action in other_actions:
            if player == 1:
                other_payoff = payoff_matrix[(other_action, opp_action)][0]
            else:
                other_payoff = payoff_matrix[(opp_action, other_action)][1]

            if other_payoff > candidate_payoff:
                return False
            elif candidate_payoff > other_payoff:
                strictly_better_for_at_least_one = True

    return strictly_better_for_at_least_one


def find_dominant_strategy_equilibrium(payoff_matrix):
    """
    Find the dominant strategy equilibrium if it exists.

    Returns:
        Tuple (action1, action2) if both players have dominant strategies, None otherwise

    TODO: Implement this function.
    """
    # TODO: Find dominant strategies for both players
    p1_dominant = None
    p2_dominant = None

    for action in get_player_actions(payoff_matrix, 1):
        if is_strictly_dominant(action, 1, payoff_matrix) or is_weakly_dominant(action, 1, payoff_matrix):
            p1_dominant = action
            break

    for action in get_player_actions(payoff_matrix, 2):
        if is_strictly_dominant(action, 2, payoff_matrix) or is_weakly_dominant(action, 2, payoff_matrix):
            p2_dominant = action
            break

    if p1_dominant and p2_dominant:
        return (p1_dominant, p2_dominant)
    return None


def test_solution():
    """Test function - Do not modify."""
    # Test with Prisoner's Dilemma (has strictly dominant strategies)
    pd_payoff = {
        ('C', 'C'): (-1, -1),
        ('C', 'D'): (-5, 0),
        ('D', 'C'): (0, -5),
        ('D', 'D'): (-3, -3),
    }

    assert is_strictly_dominant('D', 1, pd_payoff) == True, "D should be strictly dominant for P1"
    assert is_strictly_dominant('C', 1, pd_payoff) == False, "C should not be strictly dominant for P1"
    assert is_strictly_dominant('D', 2, pd_payoff) == True, "D should be strictly dominant for P2"

    dse = find_dominant_strategy_equilibrium(pd_payoff)
    assert dse == ('D', 'D'), "Dominant strategy equilibrium should be (D, D)"

    # Test with Battle of the Sexes (no dominant strategies)
    bos_payoff = {
        ('Opera', 'Opera'): (2, 1),
        ('Opera', 'Football'): (0, 0),
        ('Football', 'Opera'): (0, 0),
        ('Football', 'Football'): (1, 2),
    }

    assert is_strictly_dominant('Opera', 1, bos_payoff) == False, "No dominant strategy in BoS"
    dse_bos = find_dominant_strategy_equilibrium(bos_payoff)
    assert dse_bos is None, "Battle of the Sexes has no dominant strategy equilibrium"

    print("Excellent! You understand dominant strategies!")
    print("\nKey insights:")
    print("1. Dominant strategy equilibria are very stable")
    print("2. In the Prisoner's Dilemma, 'Defect' dominates 'Cooperate' for both players")
    print("3. Not all games have dominant strategies (e.g., Battle of the Sexes)")

    return True


if __name__ == '__main__':
    test_solution()
