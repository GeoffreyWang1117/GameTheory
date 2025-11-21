"""
Exercise 20: Nash Bargaining Solution

The Nash bargaining solution is an axiomatic approach to solving bargaining problems.
Two players must agree on how to divide a surplus. If they disagree, both get a
disagreement payoff.

Nash's solution maximizes the product of utility gains: (u1 - d1) * (u2 - d2)

This satisfies key axioms: Pareto optimality, symmetry, independence of irrelevant
alternatives, and invariance to affine transformations.

TODO: Implement Nash bargaining solution.
"""

import numpy as np


def nash_bargaining_solution(feasible_set, disagreement_point):
    """
    Find the Nash bargaining solution.

    The solution maximizes: (u1 - d1) * (u2 - d2)
    subject to: (u1, u2) is in the feasible set
               u1 >= d1, u2 >= d2

    Args:
        feasible_set: List of (u1, u2) tuples representing feasible outcomes
        disagreement_point: Tuple (d1, d2) of disagreement payoffs

    Returns:
        Tuple (u1, u2) representing the Nash bargaining solution

    TODO: Implement Nash bargaining solution.
    """
    d1, d2 = disagreement_point

    best_outcome = None
    best_product = -float('inf')

    # TODO: Find outcome that maximizes (u1-d1) * (u2-d2)
    for u1, u2 in feasible_set:
        # Check individual rationality
        if u1 < d1 or u2 < d2:
            continue

        # Calculate Nash product
        product = (u1 - d1) * (u2 - d2)

        if product > best_product:
            best_product = product
            best_outcome = (u1, u2)

    return best_outcome


def nash_bargaining_linear(total_surplus, disagreement_point, weights=(1, 1)):
    """
    Nash bargaining for linear utility with transferable surplus.

    With symmetric players and linear utility, the solution splits
    surplus equally: each gets disagreement payoff plus half of surplus.

    Args:
        total_surplus: Total amount to be divided
        disagreement_point: Tuple (d1, d2)
        weights: Bargaining power weights (default equal)

    Returns:
        Tuple (payoff1, payoff2)

    TODO: Calculate Nash bargaining solution with weights.
    """
    d1, d2 = disagreement_point
    w1, w2 = weights

    # Available surplus after disagreement payoffs
    available_surplus = total_surplus - d1 - d2

    if available_surplus < 0:
        return disagreement_point

    # TODO: Weighted Nash solution
    # With weights, solution is: d_i + w_i/(w_1 + w_2) * surplus
    total_weight = w1 + w2

    payoff1 = d1 + (w1 / total_weight) * available_surplus
    payoff2 = d2 + (w2 / total_weight) * available_surplus

    return (payoff1, payoff2)


def check_nash_axioms(solution, feasible_set, disagreement_point):
    """
    Verify that a solution satisfies Nash bargaining axioms.

    Axioms:
    1. Individual rationality: u_i >= d_i
    2. Pareto optimality: No other feasible outcome is better for both
    3. Symmetry: If problem is symmetric, solution is symmetric

    Args:
        solution: Proposed solution (u1, u2)
        feasible_set: List of feasible outcomes
        disagreement_point: (d1, d2)

    Returns:
        Dictionary of axiom checks

    TODO: Check each axiom.
    """
    u1, u2 = solution
    d1, d2 = disagreement_point

    results = {}

    # TODO: Check individual rationality
    results['individual_rationality'] = (u1 >= d1 - 0.001 and u2 >= d2 - 0.001)

    # TODO: Check Pareto optimality
    is_pareto_optimal = True
    for v1, v2 in feasible_set:
        # Check if (v1, v2) Pareto dominates (u1, u2)
        if (v1 > u1 + 0.001 and v2 >= u2 - 0.001) or \
           (v1 >= u1 - 0.001 and v2 > u2 + 0.001):
            is_pareto_optimal = False
            break

    results['pareto_optimality'] = is_pareto_optimal

    # TODO: Check symmetry (if disagreement point is symmetric)
    if abs(d1 - d2) < 0.001:
        # Check if feasible set is symmetric
        is_symmetric_problem = True
        for v1, v2 in feasible_set:
            if (v2, v1) not in feasible_set and abs(v1-v2) > 0.001:
                is_symmetric_problem = False
                break

        if is_symmetric_problem:
            results['symmetry'] = abs(u1 - u2) < 0.001
        else:
            results['symmetry'] = None  # Problem not symmetric
    else:
        results['symmetry'] = None  # Problem not symmetric

    return results


def split_the_dollar(dollars=10, disagreement=(0, 0)):
    """
    Classic 'split the dollar' problem.

    Two players bargain over splitting $10. If they agree on (x, y) where
    x + y <= 10, they get that. Otherwise both get 0.

    Args:
        dollars: Amount to split
        disagreement: Disagreement payoffs

    Returns:
        Nash bargaining solution

    TODO: Solve the split-the-dollar problem.
    """
    # Generate feasible set (all splits that sum to at most dollars)
    feasible_set = []

    # TODO: Create feasible set
    # With continuous splitting, Nash solution is to split equally
    # For discrete: enumerate all possible splits

    step = 0.1
    x = 0
    while x <= dollars:
        y = 0
        while y <= dollars - x:
            feasible_set.append((x, y))
            y += step
        x += step

    solution = nash_bargaining_solution(feasible_set, disagreement)

    return solution


def test_solution():
    """Test function - Do not modify."""
    # Test simple case
    feasible = [(0, 10), (2, 8), (4, 6), (5, 5), (6, 4), (8, 2), (10, 0)]
    disagreement = (0, 0)

    solution = nash_bargaining_solution(feasible, disagreement)
    print(f"Nash bargaining solution: {solution}")

    # Should be (5, 5) for symmetric case
    assert solution == (5, 5), f"Expected (5, 5), got {solution}"

    # Test with different disagreement point
    disagreement2 = (2, 1)
    solution2 = nash_bargaining_solution(feasible, disagreement2)
    print(f"With disagreement (2, 1): {solution2}")

    # Solution should still be feasible and individually rational
    assert solution2[0] >= 2 and solution2[1] >= 1

    # Test linear case
    linear_solution = nash_bargaining_linear(100, (10, 20))
    print(f"Linear Nash solution for surplus 100: {linear_solution}")

    # Should split available surplus (70) equally
    assert abs(linear_solution[0] - 45) < 1, f"Expected ~45, got {linear_solution[0]}"
    assert abs(linear_solution[1] - 55) < 1, f"Expected ~55, got {linear_solution[1]}"

    # Test with unequal bargaining power
    weighted = nash_bargaining_linear(100, (0, 0), weights=(2, 1))
    print(f"Weighted Nash solution (2:1): {weighted}")
    assert weighted[0] > weighted[1], "Player 1 should get more with higher weight"

    # Check axioms
    axioms = check_nash_axioms((5, 5), feasible, (0, 0))
    print(f"\nAxiom verification: {axioms}")
    assert axioms['individual_rationality'] == True
    assert axioms['pareto_optimality'] == True

    print("\nKey insights:")
    print("1. Nash bargaining solution is unique and fair")
    print("2. Maximizes product of utility gains")
    print("3. With equal bargaining power, splits surplus equally")
    print("4. Satisfies desirable axioms: Pareto optimality, symmetry, IIA")

    return True


if __name__ == '__main__':
    test_solution()
