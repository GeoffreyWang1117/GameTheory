"""
Exercise: Stackelberg Leadership Model
======================================

The Stackelberg model analyzes sequential quantity competition where one firm
(the leader) moves first, and another firm (the follower) observes and responds.

This creates a first-mover advantage: the leader can commit to a quantity,
knowing the follower's reaction.

Learning Objectives:
- Understand sequential move advantages
- Apply backward induction to find SPNE
- Compare Stackelberg to Cournot outcomes
- Analyze commitment value

Key Concepts:
- Sequential moves vs simultaneous moves
- Subgame perfect Nash equilibrium (SPNE)
- First-mover advantage
- Credible commitment
- Backward induction
"""

from typing import Tuple, Dict, Callable
import numpy as np


def follower_best_response(leader_quantity: float, demand_params: Tuple[float, float],
                           follower_cost: float) -> float:
    """
    Calculate follower's optimal response to leader's quantity.

    The follower observes leader's quantity and optimizes:
    max_{q_f} (P(q_l + q_f) - c_f) * q_f

    Args:
        leader_quantity: Quantity already produced by leader
        demand_params: (a, b) where P = a - b*Q
        follower_cost: Follower's marginal cost

    Returns:
        Follower's optimal quantity
    """
    # TODO: Calculate follower's best response
    # Profit: π_f = (a - b*(q_l + q_f) - c_f) * q_f
    # FOC: a - b*q_l - 2*b*q_f - c_f = 0
    # Solving: q_f*(q_l) = (a - c_f - b*q_l) / (2*b)
    # This is the follower's reaction function
    pass


def leader_optimal_quantity(demand_params: Tuple[float, float],
                           leader_cost: float, follower_cost: float) -> float:
    """
    Calculate leader's optimal quantity anticipating follower's response.

    Leader maximizes profit knowing follower will react optimally:
    max_{q_l} (P(q_l + q_f*(q_l)) - c_l) * q_l

    Args:
        demand_params: (a, b) where P = a - b*Q
        leader_cost: Leader's marginal cost
        follower_cost: Follower's marginal cost

    Returns:
        Leader's optimal quantity
    """
    # TODO: Calculate leader's optimal quantity using backward induction
    # Step 1: Get follower's reaction function q_f(q_l)
    # Step 2: Substitute into leader's profit function
    # Step 3: Maximize over q_l
    #
    # Substituting q_f = (a - c_f - b*q_l)/(2b):
    # Total Q = q_l + (a - c_f - b*q_l)/(2b) = (a - c_f + b*q_l)/(2b)
    # P = a - b*Q = a - (a - c_f + b*q_l)/2 = (a + c_f - b*q_l)/2
    # π_l = ((a + c_f - b*q_l)/2 - c_l) * q_l
    # FOC: (a + c_f - 2*c_l)/2 - b*q_l = 0
    # Solution: q_l* = (a - 2*c_l + c_f) / (2*b)
    pass


def find_stackelberg_equilibrium(demand_params: Tuple[float, float],
                                leader_cost: float,
                                follower_cost: float) -> Dict:
    """
    Find Stackelberg equilibrium using backward induction.

    Args:
        demand_params: (a, b) where P = a - b*Q
        leader_cost: Leader's marginal cost
        follower_cost: Follower's marginal cost

    Returns:
        Dictionary with quantities, price, and profits
    """
    # TODO: Find Stackelberg equilibrium
    # 1. Calculate leader's optimal quantity
    # 2. Calculate follower's response to that quantity
    # 3. Calculate market price and profits
    # Return: {
    #   'leader_quantity': q_l*,
    #   'follower_quantity': q_f*,
    #   'price': P*,
    #   'leader_profit': π_l*,
    #   'follower_profit': π_f*,
    #   'total_quantity': Q*
    # }
    pass


def compare_stackelberg_cournot(demand_params: Tuple[float, float],
                               cost: float) -> Dict:
    """
    Compare Stackelberg and Cournot equilibria with symmetric costs.

    Args:
        demand_params: (a, b) where P = a - b*Q
        cost: Common marginal cost

    Returns:
        Comparison of outcomes
    """
    # TODO: Compare Stackelberg vs Cournot
    #
    # Cournot (symmetric):
    #   q_c = (a - c)/(3b) for each firm
    #   Q_c = 2*(a-c)/(3b)
    #   P_c = (a + 2c)/3
    #
    # Stackelberg (with c_l = c_f = c):
    #   q_l* = (a - c)/(2b)
    #   q_f* = (a - c)/(4b)
    #   Q_s = 3*(a-c)/(4b)
    #   P_s = (a + 3c)/4
    #
    # Compare: Q_s > Q_c, P_s < P_c
    # Leader produces more, follower produces less than in Cournot
    # Leader earns more profit than in Cournot (first-mover advantage)
    #
    # Return: {
    #   'stackelberg': {...},
    #   'cournot': {...},
    #   'leader_advantage': π_l_stackelberg - π_cournot
    # }
    pass


def welfare_comparison(demand_params: Tuple[float, float], cost: float) -> Dict:
    """
    Compare consumer and total welfare in Stackelberg vs Cournot.

    Args:
        demand_params: (a, b) where P = a - b*Q
        cost: Marginal cost

    Returns:
        Welfare metrics for both market structures
    """
    # TODO: Calculate and compare welfare
    # Consumer Surplus: CS = (1/2) * (a - P) * Q
    # Producer Surplus: PS = sum of profits
    # Total Welfare: W = CS + PS
    #
    # Stackelberg produces more than Cournot:
    # → Higher consumer surplus
    # → Higher total welfare (closer to competitive)
    # → But asymmetric producer profits
    #
    # Return: {
    #   'stackelberg_cs': ...,
    #   'cournot_cs': ...,
    #   'stackelberg_welfare': ...,
    #   'cournot_welfare': ...
    # }
    pass


def value_of_commitment(demand_params: Tuple[float, float], cost: float) -> float:
    """
    Calculate the value of being able to commit (first-mover advantage).

    Args:
        demand_params: (a, b) where P = a - b*Q
        cost: Marginal cost

    Returns:
        Additional profit from moving first
    """
    # TODO: Calculate commitment value
    # Value = π_leader - π_cournot_firm
    # This measures how much a firm would pay to move first
    pass


# Test functions
def test_follower_response():
    """Test follower's best response calculation."""
    # P = 100 - Q, follower cost = 10
    q_f = follower_best_response(
        leader_quantity=40,
        demand_params=(100, 1),
        follower_cost=10
    )

    # q_f = (100 - 10 - 40) / 2 = 25
    assert q_f is not None
    assert abs(q_f - 25) < 0.01, f"Expected 25, got {q_f}"
    print(f"✓ Follower response to q_l=40: {q_f:.2f}")


def test_stackelberg_equilibrium():
    """Test Stackelberg equilibrium."""
    result = find_stackelberg_equilibrium(
        demand_params=(100, 1),
        leader_cost=10,
        follower_cost=10
    )

    assert result is not None
    q_l = result['leader_quantity']
    q_f = result['follower_quantity']

    # q_l* = (100 - 20 + 10) / 2 = 45
    # q_f* = (100 - 10 - 45) / 2 = 22.5
    assert abs(q_l - 45) < 0.01
    assert abs(q_f - 22.5) < 0.01

    # Leader produces more than follower
    assert q_l > q_f

    print(f"✓ Stackelberg equilibrium: Leader={q_l:.2f}, Follower={q_f:.2f}")
    print(f"  Price={result['price']:.2f}, Leader profit={result['leader_profit']:.2f}")


def test_stackelberg_vs_cournot():
    """Test comparison with Cournot."""
    comparison = compare_stackelberg_cournot(
        demand_params=(100, 1),
        cost=10
    )

    assert comparison is not None

    s_total_q = comparison['stackelberg']['total_quantity']
    c_total_q = comparison['cournot']['total_quantity']

    # Stackelberg produces more total quantity
    assert s_total_q > c_total_q

    leader_advantage = comparison['leader_advantage']
    # Leader earns more than in Cournot
    assert leader_advantage > 0

    print(f"✓ Stackelberg vs Cournot:")
    print(f"  Stackelberg Q: {s_total_q:.2f}")
    print(f"  Cournot Q: {c_total_q:.2f}")
    print(f"  First-mover advantage: {leader_advantage:.2f}")


def test_welfare():
    """Test welfare comparison."""
    welfare = welfare_comparison(
        demand_params=(100, 1),
        cost=10
    )

    assert welfare is not None

    s_cs = welfare['stackelberg_cs']
    c_cs = welfare['cournot_cs']

    # Stackelberg has higher consumer surplus (lower price)
    assert s_cs > c_cs

    print(f"✓ Welfare comparison:")
    print(f"  Stackelberg CS: {s_cs:.2f}")
    print(f"  Cournot CS: {c_cs:.2f}")


def test_commitment_value():
    """Test value of commitment."""
    value = value_of_commitment(
        demand_params=(100, 1),
        cost=10
    )

    assert value is not None
    assert value > 0  # First-mover advantage is positive

    print(f"✓ Value of commitment (first-mover advantage): {value:.2f}")


if __name__ == "__main__":
    print("\n=== Stackelberg Leadership Tests ===\n")
    test_follower_response()
    test_stackelberg_equilibrium()
    test_stackelberg_vs_cournot()
    test_welfare()
    test_commitment_value()
    print("\n🎉 All tests passed! You understand Stackelberg competition!")

    print("\n=== Key Insights ===")
    print("• Stackelberg: sequential moves create first-mover advantage")
    print("• Leader commits to higher quantity than in Cournot")
    print("• Follower produces less (reacts to leader's large quantity)")
    print("• Total output higher → price lower than Cournot")
    print("• Leader earns more profit than in simultaneous Cournot")
    print("• Backward induction finds subgame perfect equilibrium")
    print("• Commitment has value in strategic settings")
