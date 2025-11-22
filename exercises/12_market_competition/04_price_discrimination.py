"""
Exercise: Price Discrimination and Monopoly Pricing
===================================================

Price discrimination occurs when a firm charges different prices to different
customers or for different units of the same product.

Types of price discrimination:
- First-degree: Perfect discrimination (charge each customer their willingness to pay)
- Second-degree: Self-selection (quantity discounts, product versioning)
- Third-degree: Market segmentation (student discounts, regional pricing)

Learning Objectives:
- Understand monopoly pricing strategies
- Analyze different types of price discrimination
- Calculate optimal discriminatory prices
- Compare welfare effects

Key Concepts:
- Consumer surplus extraction
- Self-selection and screening
- Market segmentation
- Welfare effects of discrimination
- Two-part tariffs
"""

from typing import List, Dict, Tuple, Callable
import numpy as np


def uniform_monopoly_price(demand_func: Callable, marginal_cost: float,
                          price_range: Tuple[float, float]) -> Dict:
    """
    Find optimal uniform price for a monopolist.

    Monopolist sets single price to maximize profit:
    max_p (p - c) * D(p)

    Args:
        demand_func: D(p) returns quantity demanded at price p
        marginal_cost: Constant marginal cost
        price_range: (min_price, max_price) to search over

    Returns:
        Optimal price, quantity, and profit
    """
    # TODO: Find profit-maximizing price
    # For linear demand D(p) = a - b*p:
    # Revenue: R = p * (a - b*p) = a*p - b*p²
    # MR = a - 2*b*p
    # Set MR = MC: a - 2*b*p* = c
    # Optimal: p* = (a + b*c)/(2*b)
    #
    # For general demand, search over price_range
    # Return: {'price': p*, 'quantity': D(p*), 'profit': (p*-c)*D(p*), 'consumer_surplus': CS}
    pass


def perfect_price_discrimination(valuations: List[float],
                                 marginal_cost: float) -> Dict:
    """
    Calculate outcome under perfect (first-degree) price discrimination.

    Monopolist charges each customer their exact willingness to pay.
    This extracts all consumer surplus.

    Args:
        valuations: List of customers' willingness to pay
        marginal_cost: Constant marginal cost

    Returns:
        Dictionary with total profit and welfare
    """
    # TODO: Implement perfect price discrimination
    # Charge each customer their valuation v_i
    # Serve customer if v_i >= c
    # Total profit = sum of (v_i - c) for all v_i >= c
    # Consumer surplus = 0 (all extracted)
    # Total welfare = sum of (v_i - c) = profit (efficient!)
    # Return: {'profit': ..., 'num_customers': ..., 'consumer_surplus': 0, 'total_welfare': ...}
    pass


def third_degree_discrimination(demand1: Callable, demand2: Callable,
                               marginal_cost: float) -> Dict:
    """
    Find optimal prices for third-degree price discrimination.

    Monopolist can segment market into two groups with different demands.
    Sets different prices to maximize total profit.

    Args:
        demand1, demand2: Demand functions D_i(p) for each market segment
        marginal_cost: Constant marginal cost

    Returns:
        Optimal prices for each segment
    """
    # TODO: Optimize prices separately for each market
    # For each market i, set MR_i = MC
    # With linear demand D_i = a_i - b_i*p:
    # MR_i = a_i - 2*b_i*p_i = c
    # p_i* = (a_i + b_i*c) / (2*b_i)
    #
    # Inverse elasticity rule: (p_i - c)/p_i = 1/|ε_i|
    # Less elastic market gets higher price
    #
    # Return: {
    #   'price1': p1*, 'quantity1': D1(p1*),
    #   'price2': p2*, 'quantity2': D2(p2*),
    #   'total_profit': π*, 'welfare': W
    # }
    pass


def second_degree_discrimination(customer_types: List[Dict],
                                 marginal_cost: float) -> Dict:
    """
    Design optimal two-part tariff for second-degree discrimination.

    Offer quantity-price bundles that induce self-selection.
    High-value customers choose large bundle, low-value choose small.

    Args:
        customer_types: List of {'valuation': v, 'fraction': f} dictionaries
        marginal_cost: Constant marginal cost

    Returns:
        Optimal menu of (quantity, total_price) bundles
    """
    # TODO: Design screening menu
    # Two types: High and Low
    # High type bundle: Set q_H at efficient level (v_H = p), extract surplus with fixed fee
    # Low type bundle: Distort q_L down to prevent high type from mimicking
    #
    # Constraints:
    # IC(H): U_H(bundle_H) >= U_H(bundle_L)
    # IC(L): U_L(bundle_L) >= U_L(bundle_H)
    # PC(L): U_L(bundle_L) >= 0
    #
    # Return: {
    #   'high_type_bundle': (q_H, T_H),
    #   'low_type_bundle': (q_L, T_L),
    #   'profit': π*
    # }
    pass


def two_part_tariff(demand_func: Callable, marginal_cost: float,
                   customer_valuations: List[float]) -> Dict:
    """
    Design optimal two-part tariff: T(q) = F + p*q

    Monopolist charges fixed fee F plus per-unit price p.

    Args:
        demand_func: Individual demand function q(p)
        marginal_cost: Constant marginal cost
        customer_valuations: Distribution of customer values

    Returns:
        Optimal fixed fee and per-unit price
    """
    # TODO: Optimize two-part tariff
    # With identical customers:
    #   Set p = c (efficient)
    #   Set F = consumer surplus at p=c (extract all surplus)
    #
    # With heterogeneous customers:
    #   Trade-off between intensive margin (p) and extensive margin (F)
    #   Higher F excludes low-value customers
    #   Higher p distorts quantity
    #
    # Return: {'fixed_fee': F*, 'per_unit_price': p*, 'profit': π*, 'num_customers': n}
    pass


def compare_discrimination_welfare(demand_params: Tuple[float, float],
                                  marginal_cost: float) -> Dict:
    """
    Compare welfare under different pricing regimes.

    Args:
        demand_params: (a, b) for D(p) = a - b*p
        marginal_cost: Constant MC

    Returns:
        Comparison of consumer surplus, profit, and total welfare
    """
    # TODO: Compare welfare across pricing strategies
    # 1. Uniform pricing: standard monopoly
    # 2. Perfect discrimination: CS=0, W maximized (efficient)
    # 3. Third-degree: ambiguous welfare effect
    #
    # Return: {
    #   'uniform': {'CS': ..., 'PS': ..., 'W': ...},
    #   'perfect': {'CS': 0, 'PS': ..., 'W': ...},
    #   'welfare_gain_perfect': W_perfect - W_uniform
    # }
    pass


# Test functions
def test_uniform_pricing():
    """Test uniform monopoly pricing."""
    demand = lambda p: max(0, 100 - 2*p)

    result = uniform_monopoly_price(demand, marginal_cost=10, price_range=(10, 50))

    assert result is not None
    price = result['price']

    # For D = 100 - 2p: MR = 50 - p = 10 => p* = 40
    # (Or using p = (a/b + c)/2 = (50 + 10)/2 = 30)
    # Actually: R = p(100-2p), MR = 100-4p, MR=MC: 100-4p=10 => p=22.5
    # Let me recalculate: D(p) = 100-2p => p(D) = 50 - 0.5*D
    # R(D) = D*(50-0.5D) = 50D - 0.5D²
    # MR = 50 - D, MC = 10 => D* = 40, p* = 50-0.5*40 = 30

    print(f"✓ Uniform monopoly price: {price:.2f}, Q={result['quantity']:.2f}")


def test_perfect_discrimination():
    """Test perfect price discrimination."""
    valuations = [50, 40, 30, 20, 10, 5]

    result = perfect_price_discrimination(valuations, marginal_cost=15)

    assert result is not None
    profit = result['profit']
    cs = result['consumer_surplus']

    # Serve customers with v >= 15: [50, 40, 30, 20]
    # Profit = (50-15) + (40-15) + (30-15) + (20-15) = 35+25+15+5 = 80
    assert cs == 0, "CS should be zero under perfect discrimination"

    print(f"✓ Perfect discrimination: Profit={profit:.2f}, CS={cs:.2f}")


def test_third_degree():
    """Test third-degree price discrimination."""
    demand1 = lambda p: max(0, 100 - p)    # More elastic
    demand2 = lambda p: max(0, 80 - 0.5*p)  # Less elastic

    result = third_degree_discrimination(demand1, demand2, marginal_cost=20)

    assert result is not None
    p1 = result['price1']
    p2 = result['price2']

    # Less elastic market (market 2) should have higher price
    # Market 1: p = (100 + 20)/2 = 60
    # Market 2: invert demand: p = 160 - 2*q, MR = 160 - 4*q = 20 => q=35, p=90

    print(f"✓ Third-degree discrimination: p1={p1:.2f}, p2={p2:.2f}")


def test_two_part_tariff():
    """Test two-part tariff."""
    demand = lambda p: max(0, 50 - p)
    valuations = [50, 40, 30, 20, 10]

    result = two_part_tariff(demand, marginal_cost=10, customer_valuations=valuations)

    assert result is not None

    print(f"✓ Two-part tariff: F={result['fixed_fee']:.2f}, p={result['per_unit_price']:.2f}")


if __name__ == "__main__":
    print("\n=== Price Discrimination Tests ===\n")
    test_uniform_pricing()
    test_perfect_discrimination()
    test_third_degree()
    test_two_part_tariff()
    print("\n🎉 All tests passed! You understand price discrimination!")

    print("\n=== Key Insights ===")
    print("• Perfect discrimination: extracts all CS, but is efficient")
    print("• Third-degree: segment markets, charge inverse to elasticity")
    print("• Second-degree: self-selection through quantity discounts")
    print("• Two-part tariff: fixed fee + per-unit price")
    print("• Discrimination can increase or decrease welfare")
    print("• More discrimination → higher profit, but ambiguous welfare effect")
