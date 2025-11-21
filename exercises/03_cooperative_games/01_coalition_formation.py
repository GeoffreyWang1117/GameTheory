"""
Exercise 8: Coalition Formation

In cooperative games, players can form coalitions (groups) to achieve better outcomes.
The value of a coalition is what the coalition can achieve together.

Example: Three companies negotiating a merger.

TODO: Implement functions to analyze coalition formation.
"""

from itertools import combinations, chain


def powerset(iterable):
    """
    Generate all subsets (coalitions) of a set of players.

    Args:
        iterable: A set or list of players

    Returns:
        Iterator of all subsets

    Example: powerset([1,2]) -> (), (1,), (2,), (1,2)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def create_characteristic_function(players, values):
    """
    Create a characteristic function for a cooperative game.

    Args:
        players: List of player identifiers
        values: Dictionary mapping coalitions (tuples) -> values

    Returns:
        A characteristic function v(S) that returns the value of coalition S

    TODO: Implement validation and return the function.
    """
    # TODO: Validate that grand coalition is defined
    grand_coalition = tuple(sorted(players))
    if grand_coalition not in values:
        raise ValueError(f"Grand coalition {grand_coalition} must be defined")

    # Validate that empty coalition has value 0
    if () not in values:
        values[()] = 0

    def v(coalition):
        """Get the value of a coalition."""
        if not coalition:
            return 0
        coalition_tuple = tuple(sorted(coalition))
        return values.get(coalition_tuple, 0)

    return v


def is_superadditive(v, players):
    """
    Check if a cooperative game is superadditive.

    A game is superadditive if: v(S ∪ T) >= v(S) + v(T) for all disjoint S, T
    Meaning: coalitions weakly benefit from merging.

    Args:
        v: Characteristic function
        players: List of players

    Returns:
        True if the game is superadditive

    TODO: Implement superadditivity check.
    """
    # TODO: Check all pairs of disjoint coalitions
    all_coalitions = list(powerset(players))

    for S in all_coalitions:
        for T in all_coalitions:
            # Check if S and T are disjoint
            if not set(S).isdisjoint(set(T)):
                continue

            # Check superadditivity condition
            union = tuple(sorted(set(S) | set(T)))
            if v(union) < v(S) + v(T) - 0.0001:  # Small epsilon for floating point
                return False

    return True


def is_convex(v, players):
    """
    Check if a cooperative game is convex.

    A game is convex if: v(S ∪ T) + v(S ∩ T) >= v(S) + v(T) for all S, T
    Convex games have strong incentives for cooperation.

    Args:
        v: Characteristic function
        players: List of players

    Returns:
        True if the game is convex

    TODO: Implement convexity check.
    """
    all_coalitions = list(powerset(players))

    # TODO: Check convexity condition for all pairs
    for S in all_coalitions:
        for T in all_coalitions:
            union = tuple(sorted(set(S) | set(T)))
            intersection = tuple(sorted(set(S) & set(T)))

            lhs = v(union) + v(intersection)
            rhs = v(S) + v(T)

            if lhs < rhs - 0.0001:
                return False

    return True


def individual_rationality(allocation, v, players):
    """
    Check if an allocation is individually rational.

    An allocation is individually rational if each player gets at least
    what they can get alone: allocation[i] >= v({i})

    Args:
        allocation: Dictionary mapping player -> payoff
        v: Characteristic function
        players: List of players

    Returns:
        True if allocation is individually rational

    TODO: Implement individual rationality check.
    """
    # TODO: Check if each player gets at least their standalone value
    for player in players:
        if allocation[player] < v((player,)) - 0.0001:
            return False
    return True


def efficiency(allocation, v, players):
    """
    Check if an allocation is efficient.

    An allocation is efficient if it distributes exactly the value of
    the grand coalition: sum(allocation) = v(all players)

    Args:
        allocation: Dictionary mapping player -> payoff
        v: Characteristic function
        players: List of players

    Returns:
        True if allocation is efficient

    TODO: Implement efficiency check.
    """
    total = sum(allocation.values())
    grand_coalition_value = v(tuple(players))

    # TODO: Check if total allocation equals grand coalition value
    return abs(total - grand_coalition_value) < 0.0001


def test_solution():
    """Test function - Do not modify."""
    players = ['A', 'B', 'C']

    # Create a simple cooperative game
    values = {
        (): 0,
        ('A',): 10,
        ('B',): 10,
        ('C',): 10,
        ('A', 'B'): 25,
        ('A', 'C'): 25,
        ('B', 'C'): 25,
        ('A', 'B', 'C'): 45,
    }

    v = create_characteristic_function(players, values)

    # Test characteristic function
    assert v(('A',)) == 10
    assert v(('A', 'B', 'C')) == 45

    # Test superadditivity
    assert is_superadditive(v, players) == True, "This game should be superadditive"

    # Test individual rationality
    allocation1 = {'A': 15, 'B': 15, 'C': 15}
    assert individual_rationality(allocation1, v, players) == True

    allocation2 = {'A': 5, 'B': 20, 'C': 20}
    assert individual_rationality(allocation2, v, players) == False, "A gets less than standalone"

    # Test efficiency
    assert efficiency(allocation1, v, players) == True
    bad_allocation = {'A': 10, 'B': 10, 'C': 10}
    assert efficiency(bad_allocation, v, players) == False, "Doesn't use full grand coalition value"

    print("Great! You understand coalition formation!")
    print("\nKey concepts:")
    print("1. Characteristic function v(S): value of coalition S")
    print("2. Superadditivity: incentive to form larger coalitions")
    print("3. Individual rationality: players must benefit from joining")
    print("4. Efficiency: don't waste value from cooperation")

    return True


if __name__ == '__main__':
    test_solution()
