"""
Exercise 9: The Shapley Value

The Shapley value is a solution concept that assigns a unique payoff to each player
in a cooperative game, based on their marginal contributions to all possible coalitions.

Named after Lloyd Shapley (Nobel Prize 2012), it satisfies several fairness axioms.

TODO: Implement the Shapley value calculation.
"""

from itertools import permutations
import math


def marginal_contribution(player, coalition, v):
    """
    Calculate a player's marginal contribution to a coalition.

    Marginal contribution = v(S ∪ {i}) - v(S)
    i.e., how much value does adding player i to coalition S create?

    Args:
        player: The player to evaluate
        coalition: The existing coalition (as a tuple or set)
        v: Characteristic function

    Returns:
        The marginal contribution value

    TODO: Implement marginal contribution calculation.
    """
    # TODO: Calculate v(coalition + player) - v(coalition)
    coalition_with_player = tuple(sorted(set(coalition) | {player}))
    coalition_without_player = tuple(sorted(set(coalition) - {player}))

    return v(coalition_with_player) - v(coalition_without_player)


def shapley_value_formula(player, v, players):
    """
    Calculate the Shapley value for a player using the formula:

    φᵢ(v) = Σ |S|!(n-|S|-1)!/n! * [v(S ∪ {i}) - v(S)]

    where the sum is over all coalitions S that don't contain player i.

    Args:
        player: The player to calculate Shapley value for
        v: Characteristic function
        players: List of all players

    Returns:
        The Shapley value for the player

    TODO: Implement the Shapley value formula.
    """
    from itertools import combinations

    n = len(players)
    shapley = 0.0

    # Get all players except the target player
    other_players = [p for p in players if p != player]

    # TODO: Sum over all coalitions not containing the player
    for size in range(len(other_players) + 1):
        for coalition in combinations(other_players, size):
            # Calculate weight
            s = len(coalition)
            weight = math.factorial(s) * math.factorial(n - s - 1) / math.factorial(n)

            # Calculate marginal contribution
            mc = marginal_contribution(player, coalition, v)

            shapley += weight * mc

    return shapley


def shapley_value_permutation(player, v, players):
    """
    Calculate Shapley value using the permutation method:
    Average marginal contribution across all orderings of players.

    For each permutation, player i's contribution is v(predecessors ∪ {i}) - v(predecessors)

    Args:
        player: The player to calculate Shapley value for
        v: Characteristic function
        players: List of all players

    Returns:
        The Shapley value for the player

    TODO: Implement using the permutation method.
    """
    total = 0.0
    count = 0

    # TODO: Iterate through all permutations
    for perm in permutations(players):
        # Find position of player in this permutation
        idx = perm.index(player)

        # Get predecessors (players before this player in the ordering)
        predecessors = perm[:idx]

        # Calculate marginal contribution
        mc = marginal_contribution(player, predecessors, v)

        total += mc
        count += 1

    return total / count if count > 0 else 0.0


def calculate_all_shapley_values(v, players):
    """
    Calculate Shapley values for all players.

    Args:
        v: Characteristic function
        players: List of all players

    Returns:
        Dictionary mapping player -> Shapley value

    TODO: Calculate Shapley values for all players.
    """
    # TODO: Calculate Shapley value for each player
    shapley_values = {}

    for player in players:
        shapley_values[player] = shapley_value_formula(player, v, players)

    return shapley_values


def verify_shapley_axioms(shapley_values, v, players):
    """
    Verify that the Shapley value satisfies its defining axioms.

    1. Efficiency: Sum of payoffs equals v(grand coalition)
    2. Symmetry: Symmetric players get equal payoffs
    3. Dummy player: A player who contributes 0 gets 0
    4. Additivity: Shapley value is linear

    Args:
        shapley_values: Dictionary of Shapley values
        v: Characteristic function
        players: List of players

    Returns:
        Dictionary of axiom check results

    TODO: Implement axiom verification.
    """
    results = {}

    # TODO: Check efficiency
    total = sum(shapley_values.values())
    grand_value = v(tuple(players))
    results['efficiency'] = abs(total - grand_value) < 0.0001

    # Check dummy player (if any player always contributes 0)
    results['dummy'] = True  # Simplified check
    for player in players:
        # Check if player is dummy (contributes 0 to all coalitions)
        is_dummy = True
        from itertools import combinations
        for size in range(len(players)):
            for coalition in combinations([p for p in players if p != player], size):
                mc = marginal_contribution(player, coalition, v)
                if abs(mc) > 0.0001:
                    is_dummy = False
                    break
            if not is_dummy:
                break

        # If player is dummy, they should get 0
        if is_dummy and abs(shapley_values[player]) > 0.0001:
            results['dummy'] = False

    return results


def test_solution():
    """Test function - Do not modify."""
    # Create a simple 3-player game
    players = ['A', 'B', 'C']

    values = {
        (): 0,
        ('A',): 6,
        ('B',): 6,
        ('C',): 0,
        ('A', 'B'): 12,
        ('A', 'C'): 6,
        ('B', 'C'): 6,
        ('A', 'B', 'C'): 18,
    }

    def v(coalition):
        if not coalition:
            return 0
        return values.get(tuple(sorted(coalition)), 0)

    # Test marginal contribution
    mc = marginal_contribution('C', ('A', 'B'), v)
    assert abs(mc - 6) < 0.001, f"Expected MC of 6, got {mc}"

    # Calculate Shapley values using both methods
    sv_formula = shapley_value_formula('A', v, players)
    sv_perm = shapley_value_permutation('A', v, players)

    # Both methods should give same result
    assert abs(sv_formula - sv_perm) < 0.001, "Two methods should give same result"

    # Calculate all Shapley values
    shapley_values = calculate_all_shapley_values(v, players)

    print("\nShapley Values:")
    for player, value in shapley_values.items():
        print(f"  Player {player}: {value:.2f}")

    # Verify axioms
    axioms = verify_shapley_axioms(shapley_values, v, players)
    assert axioms['efficiency'] == True, "Should satisfy efficiency"

    # Check that C (dummy player) gets less than A or B
    assert shapley_values['C'] < shapley_values['A'], "Dummy player should get less"

    print("\nKey insights:")
    print("1. Shapley value rewards players based on marginal contributions")
    print("2. It's the unique solution satisfying efficiency, symmetry, dummy, and additivity")
    print("3. Player C contributes less and gets lower Shapley value")

    return True


if __name__ == '__main__':
    test_solution()
