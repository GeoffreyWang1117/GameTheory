"""
Exercise 10: The Core

The core is the set of allocations where no coalition has an incentive to deviate.
An allocation is in the core if no coalition can do better by breaking away.

Formally: allocation x is in the core if:
- Σ xᵢ = v(N) (efficiency)
- For all coalitions S: Σᵢ∈S xᵢ >= v(S) (coalitional rationality)

TODO: Implement functions to find and analyze the core.
"""

from itertools import combinations


def is_in_core(allocation, v, players):
    """
    Check if an allocation is in the core.

    Args:
        allocation: Dictionary mapping player -> payoff
        v: Characteristic function
        players: List of players

    Returns:
        Tuple (is_in_core, blocking_coalition)
        blocking_coalition is None if in core, otherwise the coalition that blocks

    TODO: Implement core membership check.
    """
    # Check efficiency
    total = sum(allocation.values())
    grand_value = v(tuple(players))

    if abs(total - grand_value) > 0.0001:
        return False, None

    # TODO: Check if any coalition wants to deviate
    for size in range(1, len(players) + 1):
        for coalition in combinations(players, size):
            coalition_value = v(coalition)
            coalition_allocation = sum(allocation[p] for p in coalition)

            # If coalition gets less than it can achieve alone, it blocks
            if coalition_allocation < coalition_value - 0.0001:
                return False, coalition

    return True, None


def find_core_constraints(v, players):
    """
    Generate all constraints that define the core as a linear program.

    The core is defined by:
    1. Σ xᵢ = v(N) (efficiency)
    2. Σᵢ∈S xᵢ >= v(S) for all S ⊆ N (coalitional rationality)

    Args:
        v: Characteristic function
        players: List of players

    Returns:
        List of constraints as tuples (coalition, minimum_value)

    TODO: Generate all core constraints.
    """
    constraints = []

    # TODO: Add constraint for each coalition
    for size in range(1, len(players) + 1):
        for coalition in combinations(players, size):
            value = v(coalition)
            constraints.append((coalition, value))

    return constraints


def is_core_nonempty_balanced_game(v, players):
    """
    Check if a game is balanced (equivalent to having non-empty core).

    A game is balanced if the grand coalition is always optimal.
    By the Bondareva-Shapley theorem, a game has non-empty core iff it's balanced.

    Simplified check: For superadditive games, check if grand coalition
    gives at least as much as any partition.

    Args:
        v: Characteristic function
        players: List of players

    Returns:
        True if core is likely non-empty

    TODO: Implement simplified balancedness check.
    """
    grand_value = v(tuple(players))

    # Simple necessary condition: check all 2-partitions
    # TODO: For each way to split players into two groups,
    # check if v(S) + v(T) <= v(N)

    n = len(players)
    for size in range(1, n):
        for coalition1 in combinations(players, size):
            coalition2 = tuple(p for p in players if p not in coalition1)

            partition_value = v(coalition1) + v(coalition2)

            if partition_value > grand_value + 0.0001:
                return False

    return True


def core_allocation_example(v, players):
    """
    Try to find an allocation in the core.

    Strategy: Start with Shapley value and adjust if needed.

    Args:
        v: Characteristic function
        players: List of players

    Returns:
        Allocation in the core if found, None otherwise

    TODO: Attempt to construct a core allocation.
    """
    # Try Shapley value first
    from itertools import permutations
    import math

    def shapley_value(player):
        n = len(players)
        shapley = 0.0
        other_players = [p for p in players if p != player]

        for size in range(len(other_players) + 1):
            for coalition in combinations(other_players, size):
                s = len(coalition)
                weight = math.factorial(s) * math.factorial(n - s - 1) / math.factorial(n)

                coalition_with = tuple(sorted(set(coalition) | {player}))
                coalition_without = tuple(sorted(set(coalition)))

                mc = v(coalition_with) - v(coalition_without)
                shapley += weight * mc

        return shapley

    allocation = {player: shapley_value(player) for player in players}

    # Check if in core
    in_core, blocking = is_in_core(allocation, v, players)

    if in_core:
        return allocation

    # If Shapley value not in core, try equal split
    grand_value = v(tuple(players))
    equal_allocation = {player: grand_value / len(players) for player in players}

    in_core, _ = is_in_core(equal_allocation, v, players)
    if in_core:
        return equal_allocation

    return None


def test_solution():
    """Test function - Do not modify."""
    players = ['A', 'B', 'C']

    # Create a game with non-empty core
    values = {
        (): 0,
        ('A',): 0,
        ('B',): 0,
        ('C',): 0,
        ('A', 'B'): 30,
        ('A', 'C'): 30,
        ('B', 'C'): 40,
        ('A', 'B', 'C'): 60,
    }

    def v(coalition):
        if not coalition:
            return 0
        return values.get(tuple(sorted(coalition)), 0)

    # Test core membership
    allocation1 = {'A': 10, 'B': 20, 'C': 30}
    in_core, blocking = is_in_core(allocation1, v, players)
    assert in_core == True, f"Allocation should be in core, blocking: {blocking}"

    allocation2 = {'A': 5, 'B': 5, 'C': 50}
    in_core, blocking = is_in_core(allocation2, v, players)
    assert in_core == False, "A and B together would block this allocation"
    assert 'A' in blocking and 'B' in blocking, "Should be blocked by A and B"

    # Test core constraints
    constraints = find_core_constraints(v, players)
    assert len(constraints) > 0, "Should have constraints"

    # Test example allocation
    core_alloc = core_allocation_example(v, players)
    if core_alloc:
        in_core, _ = is_in_core(core_alloc, v, players)
        assert in_core == True, "Example allocation should be in core"
        print(f"\nCore allocation found: {core_alloc}")

    print("\nKey insights about the Core:")
    print("1. Core = set of stable allocations (no coalition wants to deviate)")
    print("2. Core can be empty, have one point, or be a region")
    print("3. Shapley value may or may not be in the core")
    print("4. Core balances efficiency with coalitional stability")

    return True


if __name__ == '__main__':
    test_solution()
