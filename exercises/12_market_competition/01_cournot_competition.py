"""
Exercise: Cournot Competition
==============================

Cournot competition models oligopolistic markets where firms simultaneously
choose quantities. The market price adjusts based on total quantity supplied.

Named after Antoine Augustin Cournot (1838), this is one of the foundational
models of industrial organization.

Learning Objectives:
- Understand quantity competition
- Find Cournot-Nash equilibrium
- Analyze market power and deadweight loss
- Compare to perfect competition and monopoly

Key Concepts:
- Strategic quantity choice
- Residual demand
- Best response functions
- Market clearing price
- Welfare analysis
"""

from typing import List, Tuple, Callable
import numpy as np


def cournot_best_response(opponent_quantity: float, demand_func: Callable,
                          cost_func: Callable) -> float:
    """
    Calculate a firm's best response to opponent's quantity choice.

    The firm maximizes profit: π = P(Q) × q - C(q)
    where Q = q + q_opponent is total quantity

    Args:
        opponent_quantity: Quantity chosen by opponent
        demand_func: P(Q) - inverse demand function
        cost_func: C(q) - cost function

    Returns:
        Optimal quantity to produce
    """
    # TODO: Find quantity that maximizes profit given opponent's quantity
    # Take derivative of profit with respect to q and set to 0:
    # d/dq [P(q + q_opp) × q - C(q)] = 0
    # For linear demand P = a - b*Q and cost C = c*q:
    # P(Q) + q × P'(Q) = MC
    # (a - b(q + q_opp)) - b*q = c
    # Solving: q* = (a - c - b*q_opp) / (2b)
    pass


def find_cournot_equilibrium(num_firms: int, demand_params: Tuple[float, float],
                             cost_params: Tuple[float, float]) -> Dict:
    """
    Find symmetric Cournot-Nash equilibrium.

    Args:
        num_firms: Number of firms (n)
        demand_params: (a, b) where P = a - b*Q
        cost_params: (c, f) where C(q) = c*q + f (marginal cost c, fixed cost f)

    Returns:
        Dictionary with equilibrium quantities, price, and profits
    """
    # TODO: Find Cournot equilibrium
    # In symmetric equilibrium, all firms choose the same quantity q*
    # Each firm's FOC: a - b*(n*q*) - b*q* = c
    # Simplifying: a - b*(n+1)*q* = c
    # Solution: q* = (a - c) / (b*(n+1))
    # Price: P* = a - b*n*q*
    # Profit per firm: π* = (P* - c)*q* - f
    # Return: {'quantity_per_firm': q*, 'price': P*, 'profit_per_firm': π*, 'total_quantity': n*q*}
    pass


def compare_market_structures(demand_params: Tuple[float, float],
                              cost_params: Tuple[float, float]) -> Dict:
    """
    Compare perfect competition, monopoly, and Cournot duopoly.

    Args:
        demand_params: (a, b) for P = a - b*Q
        cost_params: (c, f) for C(q) = c*q + f

    Returns:
        Dictionary with outcomes under each market structure
    """
    # TODO: Calculate equilibrium for three market structures:
    #
    # 1. Perfect Competition: P = MC
    #    a - b*Q = c  =>  Q_pc = (a-c)/b, P_pc = c, π = 0
    #
    # 2. Monopoly: MR = MC
    #    MR = a - 2b*Q = c  =>  Q_m = (a-c)/(2b), P_m = (a+c)/2
    #
    # 3. Duopoly (n=2): Use find_cournot_equilibrium
    #
    # Return: {
    #   'perfect_competition': {'Q': ..., 'P': ..., 'total_profit': ...},
    #   'monopoly': {'Q': ..., 'P': ..., 'profit': ...},
    #   'duopoly': {'Q': ..., 'P': ..., 'profit_per_firm': ...}
    # }
    pass


def calculate_welfare(quantity: float, price: float, marginal_cost: float,
                     demand_params: Tuple[float, float]) -> Dict[str, float]:
    """
    Calculate consumer surplus, producer surplus, and deadweight loss.

    Args:
        quantity: Equilibrium quantity
        price: Equilibrium price
        marginal_cost: Constant marginal cost
        demand_params: (a, b) for P = a - b*Q

    Returns:
        Dictionary with CS, PS, total welfare, and DWL
    """
    # TODO: Calculate welfare measures
    # Consumer Surplus: CS = (1/2) * (P_max - P) * Q = (1/2) * (a - P) * Q
    # Producer Surplus: PS = (P - MC) * Q (ignoring fixed costs)
    # Total Welfare: W = CS + PS
    # Competitive quantity: Q_c = (a - c) / b
    # Deadweight Loss: DWL = (1/2) * (P - MC) * (Q_c - Q)
    # Return: {'consumer_surplus': CS, 'producer_surplus': PS, 'total_welfare': W, 'deadweight_loss': DWL}
    pass


def cournot_with_asymmetric_costs(cost1: float, cost2: float,
                                  demand_params: Tuple[float, float]) -> Dict:
    """
    Find Cournot equilibrium with asymmetric costs.

    Args:
        cost1, cost2: Marginal costs for firms 1 and 2
        demand_params: (a, b) for P = a - b*Q

    Returns:
        Equilibrium quantities for each firm
    """
    # TODO: Solve for asymmetric Cournot equilibrium
    # Firm 1 FOC: a - b*(q1 + q2) - b*q1 = c1
    # Firm 2 FOC: a - b*(q1 + q2) - b*q2 = c2
    # Solving system:
    # q1* = (a - 2*c1 + c2) / (3*b)
    # q2* = (a - 2*c2 + c1) / (3*b)
    # More efficient firm produces more
    # Return: {'firm1_quantity': q1*, 'firm2_quantity': q2*, 'price': P*, 'firm1_profit': π1*, 'firm2_profit': π2*}
    pass


# Test functions
def test_best_response():
    """Test best response calculation."""
    # Linear demand: P = 100 - Q, Cost: C = 10*q
    demand = lambda Q: 100 - Q
    cost = lambda q: 10 * q

    # If opponent produces 30, what's my best response?
    q_best = cournot_best_response(30, demand, cost)

    # Best response: q = (100 - 10 - 30) / 2 = 30
    assert q_best is not None
    assert abs(q_best - 30) < 0.01, f"Expected 30, got {q_best}"
    print(f"✓ Best response to q=30: {q_best:.2f}")


def test_cournot_equilibrium():
    """Test Cournot equilibrium finding."""
    # P = 100 - Q, MC = 10
    result = find_cournot_equilibrium(
        num_firms=2,
        demand_params=(100, 1),
        cost_params=(10, 0)
    )

    assert result is not None
    q_per_firm = result['quantity_per_firm']
    price = result['price']

    # q* = (100 - 10) / (1 * 3) = 30
    # P* = 100 - 2*30 = 40
    assert abs(q_per_firm - 30) < 0.01
    assert abs(price - 40) < 0.01

    print(f"✓ Duopoly equilibrium: q={q_per_firm:.2f}, P={price:.2f}")


def test_market_comparison():
    """Test comparison of market structures."""
    comparison = compare_market_structures(
        demand_params=(100, 1),
        cost_params=(10, 0)
    )

    assert comparison is not None
    assert 'perfect_competition' in comparison
    assert 'monopoly' in comparison
    assert 'duopoly' in comparison

    pc_q = comparison['perfect_competition']['Q']
    m_q = comparison['monopoly']['Q']
    d_q = comparison['duopoly']['Q']

    # Q_pc = 90 > Q_duopoly = 60 > Q_monopoly = 45
    assert pc_q > d_q > m_q, "Quantity ordering incorrect"

    print(f"✓ Market structure comparison:")
    print(f"  Perfect competition: Q={pc_q:.2f}")
    print(f"  Duopoly: Q={d_q:.2f}")
    print(f"  Monopoly: Q={m_q:.2f}")


def test_welfare():
    """Test welfare calculations."""
    welfare = calculate_welfare(
        quantity=60,
        price=40,
        marginal_cost=10,
        demand_params=(100, 1)
    )

    assert welfare is not None
    assert 'consumer_surplus' in welfare
    assert 'producer_surplus' in welfare
    assert 'deadweight_loss' in welfare

    print(f"✓ Welfare analysis (Duopoly):")
    print(f"  Consumer Surplus: {welfare['consumer_surplus']:.2f}")
    print(f"  Producer Surplus: {welfare['producer_surplus']:.2f}")
    print(f"  Deadweight Loss: {welfare['deadweight_loss']:.2f}")


def test_asymmetric_costs():
    """Test asymmetric cost Cournot."""
    result = cournot_with_asymmetric_costs(
        cost1=10,
        cost2=20,
        demand_params=(100, 1)
    )

    assert result is not None
    q1 = result['firm1_quantity']
    q2 = result['firm2_quantity']

    # Lower cost firm produces more
    assert q1 > q2, "Lower cost firm should produce more"

    # q1 = (100 - 20 + 20) / 3 = 33.33
    # q2 = (100 - 40 + 10) / 3 = 23.33
    assert abs(q1 - 33.33) < 0.1
    assert abs(q2 - 23.33) < 0.1

    print(f"✓ Asymmetric costs: Low-cost firm q={q1:.2f}, High-cost firm q={q2:.2f}")


if __name__ == "__main__":
    print("\n=== Cournot Competition Tests ===\n")
    test_best_response()
    test_cournot_equilibrium()
    test_market_comparison()
    test_welfare()
    test_asymmetric_costs()
    print("\n🎉 All tests passed! You understand Cournot competition!")

    print("\n=== Key Insights ===")
    print("• Cournot: firms compete in quantities, price adjusts")
    print("• Equilibrium quantity between monopoly and perfect competition")
    print("• More firms → lower price, higher quantity (closer to competition)")
    print("• Best response slopes down: if rival produces more, I produce less")
    print("• Asymmetric costs: efficient firms gain market share")
    print("• Cournot competition creates deadweight loss (market power)")
