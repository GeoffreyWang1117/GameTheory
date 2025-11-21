"""
Exercise 7: Coordination Games

Coordination games are games where players benefit from choosing the same action
or coordinating their choices. These games often have multiple Nash Equilibria.

Examples:
- Battle of the Sexes
- Stag Hunt
- Driving conventions (which side of the road)

TODO: Analyze various coordination games.
"""


def battle_of_sexes():
    """
    Create the Battle of the Sexes game.

    A couple wants to go out together. He prefers football (F), she prefers opera (O).
    But both prefer being together over being apart.

    Payoffs:
              O     F
        O   (2,1) (0,0)
        F   (0,0) (1,2)

    TODO: Return the payoff matrix.
    """
    return {
        ('O', 'O'): (2, 1),
        ('O', 'F'): (0, 0),
        ('F', 'O'): (0, 0),
        ('F', 'F'): (1, 2),
    }


def stag_hunt():
    """
    Create the Stag Hunt game.

    Two hunters can either hunt a stag (S) together (requires cooperation)
    or hunt rabbits (R) individually.

    Payoffs:
              S     R
        S   (5,5) (0,3)
        R   (3,0) (3,3)

    Stag hunting gives the best outcome but requires coordination.
    Rabbit hunting is safer but gives lower payoff.

    TODO: Return the payoff matrix.
    """
    return {
        ('S', 'S'): (5, 5),
        ('S', 'R'): (0, 3),
        ('R', 'S'): (3, 0),
        ('R', 'R'): (3, 3),
    }


def find_pareto_optimal_outcomes(payoff_matrix):
    """
    Find all Pareto optimal outcomes.

    An outcome is Pareto optimal if no other outcome makes at least one player
    better off without making anyone worse off.

    Args:
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        List of Pareto optimal outcomes

    TODO: Implement Pareto optimality finder.
    """
    pareto_optimal = []

    # TODO: Check each outcome
    for outcome, payoff in payoff_matrix.items():
        is_dominated = False

        for other_outcome, other_payoff in payoff_matrix.items():
            if outcome == other_outcome:
                continue

            # Check if other_outcome Pareto dominates outcome
            p1_better = other_payoff[0] > payoff[0]
            p2_better = other_payoff[1] > payoff[1]
            p1_not_worse = other_payoff[0] >= payoff[0]
            p2_not_worse = other_payoff[1] >= payoff[1]

            if (p1_better or p2_better) and p1_not_worse and p2_not_worse:
                is_dominated = True
                break

        if not is_dominated:
            pareto_optimal.append(outcome)

    return pareto_optimal


def payoff_dominance(outcome1, outcome2, payoff_matrix):
    """
    Compare two Nash Equilibria by payoff dominance.

    Outcome1 payoff-dominates outcome2 if both players get higher payoffs in outcome1.

    Args:
        outcome1: Tuple (action1, action2)
        outcome2: Tuple (action1, action2)
        payoff_matrix: The payoff matrix

    Returns:
        1 if outcome1 payoff-dominates outcome2
        -1 if outcome2 payoff-dominates outcome1
        0 if neither dominates

    TODO: Implement payoff dominance comparison.
    """
    p1_1, p2_1 = payoff_matrix[outcome1]
    p1_2, p2_2 = payoff_matrix[outcome2]

    # TODO: Compare payoffs
    if p1_1 > p1_2 and p2_1 > p2_2:
        return 1
    elif p1_2 > p1_1 and p2_2 > p2_1:
        return -1
    else:
        return 0


def risk_dominance_2x2(outcome1, outcome2, payoff_matrix):
    """
    Compare two Nash Equilibria by risk dominance (for 2x2 games).

    In a 2x2 game, outcome1 risk-dominates outcome2 if the product of the
    deviations from outcome1 is larger than from outcome2.

    Risk dominance captures which equilibrium has a larger "basin of attraction".

    Args:
        outcome1: Tuple (action1, action2)
        outcome2: Tuple (action1, action2)
        payoff_matrix: The payoff matrix (must be 2x2)

    Returns:
        1 if outcome1 risk-dominates outcome2
        -1 if outcome2 risk-dominates outcome1
        0 if equal

    TODO: Implement risk dominance for 2x2 games.
    """
    # Get payoffs at each equilibrium
    p1_eq1, p2_eq1 = payoff_matrix[outcome1]
    p1_eq2, p2_eq2 = payoff_matrix[outcome2]

    # Get deviation payoffs
    # If deviating from outcome1
    dev1_action1, dev1_action2 = outcome2
    p1_dev1 = payoff_matrix[(dev1_action1, outcome1[1])][0]
    p2_dev1 = payoff_matrix[(outcome1[0], dev1_action2)][1]

    # Loss from deviating from outcome1
    loss1_p1 = p1_eq1 - p1_dev1
    loss1_p2 = p2_eq1 - p2_dev1

    # If deviating from outcome2
    dev2_action1, dev2_action2 = outcome1
    p1_dev2 = payoff_matrix[(dev2_action1, outcome2[1])][0]
    p2_dev2 = payoff_matrix[(outcome2[0], dev2_action2)][1]

    # Loss from deviating from outcome2
    loss2_p1 = p1_eq2 - p1_dev2
    loss2_p2 = p2_eq2 - p2_dev2

    # Product of losses (risk)
    risk1 = loss1_p1 * loss1_p2
    risk2 = loss2_p1 * loss2_p2

    # TODO: Compare risk products
    if risk1 > risk2:
        return 1
    elif risk2 > risk1:
        return -1
    else:
        return 0


def test_solution():
    """Test function - Do not modify."""
    bos = battle_of_sexes()
    sh = stag_hunt()

    # Test Pareto optimality
    pareto_bos = find_pareto_optimal_outcomes(bos)
    assert len(pareto_bos) == 2, "Battle of Sexes should have 2 Pareto optimal outcomes"
    assert ('O', 'O') in pareto_bos and ('F', 'F') in pareto_bos

    pareto_sh = find_pareto_optimal_outcomes(sh)
    assert ('S', 'S') in pareto_sh, "(S,S) should be Pareto optimal"

    # Test payoff dominance
    pd_bos = payoff_dominance(('O', 'O'), ('F', 'F'), bos)
    assert pd_bos == 0, "Neither equilibrium payoff-dominates in BoS"

    pd_sh = payoff_dominance(('S', 'S'), ('R', 'R'), sh)
    assert pd_sh == 1, "(S,S) should payoff-dominate (R,R)"

    # Test risk dominance
    rd_sh = risk_dominance_2x2(('S', 'S'), ('R', 'R'), sh)
    assert rd_sh == -1, "(R,R) should risk-dominate (S,S) in standard Stag Hunt"

    print("Great! You understand coordination games!")
    print("\nKey insights:")
    print("1. Coordination games have multiple Nash Equilibria")
    print("2. Payoff dominance: Which equilibrium gives higher payoffs to all?")
    print("3. Risk dominance: Which equilibrium is 'safer' or more robust?")
    print("4. In Stag Hunt: (S,S) is payoff-dominant but (R,R) is risk-dominant!")

    return True


if __name__ == '__main__':
    test_solution()
