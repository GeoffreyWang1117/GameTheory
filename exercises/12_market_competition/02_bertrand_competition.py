"""
Exercise: Bertrand Competition
===============================

Bertrand competition models oligopolistic markets where firms simultaneously
choose prices. Consumers buy from the lowest-priced firm.

The Bertrand Paradox: with just two firms and homogeneous products, price
competition drives price to marginal cost (competitive outcome).

Learning Objectives:
- Understand price competition dynamics
- Discover the Bertrand Paradox
- Analyze product differentiation effects
- Compare Bertrand and Cournot outcomes

Key Concepts:
- Strategic price choice
- Undercutting incentives
- Bertrand Paradox
- Product differentiation
- Capacity constraints
"""

from typing import Tuple, Dict, Callable
import numpy as np


def bertrand_best_response(opponent_price: float, marginal_cost: float,
                           product_differentiation: float = 0) -> float:
    """
    Calculate best response price in Bertrand competition.

    With homogeneous products:
    - If p_opponent > MC: set p = p_opponent - ε (slightly undercut)
    - If p_opponent = MC: set p = MC (no profitable deviation)
    - If p_opponent < MC: set any p >= MC (don't produce at loss)

    With differentiated products (using linear demand):
    - Demand: q_i = a - b*p_i + d*p_j (d = differentiation parameter)
    - Best response has interior solution

    Args:
        opponent_price: Price set by opponent
        marginal_cost: Constant marginal cost
        product_differentiation: 0 for homogeneous, >0 for differentiated

    Returns:
        Optimal price to set
    """
    # TODO: Calculate best response price
    # If product_differentiation == 0 (homogeneous):
    #   - If opponent_price > marginal_cost: return opponent_price - 0.01 (undercut)
    #   - Else: return marginal_cost
    # If product_differentiation > 0 (differentiated):
    #   - Use best response formula from demand function
    #   - For q_i = a - b*p_i + d*p_j: BR_i(p_j) = (a + d*p_j + b*c) / (2*b)
    pass


def find_bertrand_equilibrium(num_firms: int, marginal_cost: float,
                              product_type: str = 'homogeneous') -> Dict:
    """
    Find Bertrand-Nash equilibrium.

    Args:
        num_firms: Number of competing firms
        marginal_cost: Constant marginal cost (same for all firms)
        product_type: 'homogeneous' or 'differentiated'

    Returns:
        Dictionary with equilibrium prices and profits
    """
    # TODO: Find Bertrand equilibrium
    # Homogeneous products:
    #   - All firms set p* = MC
    #   - Profits are zero
    #   - This is the Bertrand Paradox!
    #
    # Differentiated products (assume symmetric):
    #   - Use best response functions
    #   - In symmetric equilibrium: p* = BR(p*)
    #   - Solve for p*
    #
    # Return: {'price': p*, 'profit_per_firm': π*, 'total_quantity': Q}
    pass


def bertrand_with_capacity_constraints(capacity1: float, capacity2: float,
                                      demand_at_mc: float, marginal_cost: float,
                                      market_demand: Callable) -> Dict:
    """
    Analyze Bertrand competition with capacity constraints.

    Capacity constraints can restore market power even with price competition.
    If total capacity < competitive demand, prices rise above MC.

    Args:
        capacity1, capacity2: Production capacities
        demand_at_mc: Total demand at price = MC
        marginal_cost: Constant marginal cost
        market_demand: Demand function D(p)

    Returns:
        Equilibrium prices and quantities
    """
    # TODO: Analyze Bertrand with capacity constraints
    # If K1 + K2 >= D(MC): standard Bertrand (p = MC)
    # If K1 + K2 < D(MC): price rises above MC
    # The firm with spare capacity can charge higher price
    # Residual demand for high-price firm: D(p) - K_low_price_firm
    # Return: {'firm1_price': p1, 'firm2_price': p2, 'firm1_quantity': q1, 'firm2_quantity': q2}
    pass


def differentiated_bertrand(differentiation: float, marginal_cost: float,
                           demand_params: Dict) -> Dict:
    """
    Find equilibrium in differentiated Bertrand competition.

    Demand for firm i: q_i = a - b*p_i + d*p_j
    where d measures substitutability (d=0: independent, d→b: perfect substitutes)

    Args:
        differentiation: Parameter d (cross-price effect)
        marginal_cost: Constant MC
        demand_params: {'a': intercept, 'b': own-price coefficient}

    Returns:
        Symmetric equilibrium prices and quantities
    """
    # TODO: Solve for symmetric Bertrand equilibrium with differentiation
    # Profit: π_i = (p_i - c) * (a - b*p_i + d*p_j)
    # FOC: a - 2*b*p_i + d*p_j + b*c = 0
    # In symmetric equilibrium p_i = p_j = p*:
    # a - 2*b*p* + d*p* + b*c = 0
    # p* = (a + b*c) / (2*b - d)
    # As d → b (more substitutable), p* → c (Bertrand paradox limit)
    # As d → 0 (independent), p* → (a/b + c)/2 (monopoly pricing)
    # Return: {'price': p*, 'quantity_per_firm': q*, 'profit_per_firm': π*, 'markup': p* - c}
    pass


def compare_bertrand_cournot(demand_params: Tuple[float, float],
                             marginal_cost: float, num_firms: int = 2) -> Dict:
    """
    Compare Bertrand and Cournot competition outcomes.

    Args:
        demand_params: (a, b) for P = a - b*Q
        marginal_cost: Constant MC
        num_firms: Number of firms

    Returns:
        Comparison of prices, quantities, and profits
    """
    # TODO: Compare Bertrand and Cournot
    # Bertrand (homogeneous): p = MC, π = 0
    # Cournot: p > MC, π > 0
    # Bertrand is more competitive!
    #
    # Intuition: Price competition is fiercer than quantity competition
    # With quantities, increasing output lowers market price (strategic substitute)
    # With prices, lowering price steals all customers (discontinuous demand)
    #
    # Return: {
    #   'bertrand': {'price': ..., 'total_quantity': ..., 'profit_per_firm': ...},
    #   'cournot': {'price': ..., 'total_quantity': ..., 'profit_per_firm': ...}
    # }
    pass


# Test functions
def test_bertrand_homogeneous():
    """Test Bertrand paradox."""
    result = find_bertrand_equilibrium(
        num_firms=2,
        marginal_cost=10,
        product_type='homogeneous'
    )

    assert result is not None
    price = result['price']
    profit = result['profit_per_firm']

    # Bertrand paradox: p = MC, π = 0
    assert abs(price - 10) < 0.01, "Price should equal MC"
    assert abs(profit - 0) < 0.01, "Profits should be zero"

    print(f"✓ Bertrand (homogeneous): P={price:.2f}, π={profit:.2f} (Paradox!)")


def test_best_response():
    """Test best response function."""
    # Homogeneous products
    br = bertrand_best_response(opponent_price=15, marginal_cost=10,
                                product_differentiation=0)

    # Should undercut opponent
    assert br < 15 and br >= 10

    print(f"✓ Best response to p=15: {br:.2f}")


def test_differentiated_bertrand():
    """Test differentiated products Bertrand."""
    result = differentiated_bertrand(
        differentiation=0.5,
        marginal_cost=10,
        demand_params={'a': 100, 'b': 1}
    )

    assert result is not None
    price = result['price']
    markup = result['markup']

    # With differentiation, price > MC
    assert price > 10, "Price should exceed MC with differentiation"

    print(f"✓ Differentiated Bertrand: P={price:.2f}, markup={markup:.2f}")


def test_capacity_constraints():
    """Test Bertrand with capacity constraints."""
    demand = lambda p: max(0, 100 - p)

    result = bertrand_with_capacity_constraints(
        capacity1=30,
        capacity2=30,
        demand_at_mc=90,  # D(10) = 90
        marginal_cost=10,
        market_demand=demand
    )

    assert result is not None

    # Total capacity (60) < demand at MC (90)
    # So price should rise above MC
    prices = [result.get('firm1_price', 10), result.get('firm2_price', 10)]

    print(f"✓ Capacity-constrained Bertrand: Prices={prices}")


def test_bertrand_vs_cournot():
    """Test comparison with Cournot."""
    comparison = compare_bertrand_cournot(
        demand_params=(100, 1),
        marginal_cost=10,
        num_firms=2
    )

    assert comparison is not None
    bertrand_price = comparison['bertrand']['price']
    cournot_price = comparison['cournot']['price']

    # Bertrand price should be lower
    assert bertrand_price <= cournot_price

    print(f"✓ Bertrand vs Cournot:")
    print(f"  Bertrand: P={bertrand_price:.2f}")
    print(f"  Cournot: P={cournot_price:.2f}")


if __name__ == "__main__":
    print("\n=== Bertrand Competition Tests ===\n")
    test_bertrand_homogeneous()
    test_best_response()
    test_differentiated_bertrand()
    test_capacity_constraints()
    test_bertrand_vs_cournot()
    print("\n🎉 All tests passed! You understand Bertrand competition!")

    print("\n=== Key Insights ===")
    print("• Bertrand Paradox: 2 firms + price competition = competitive outcome")
    print("• Price competition is fiercer than quantity competition")
    print("• Product differentiation softens price competition")
    print("• Capacity constraints can restore market power")
    print("• Bertrand predicts lower prices than Cournot")
    print("• Real markets often have elements of both models")
