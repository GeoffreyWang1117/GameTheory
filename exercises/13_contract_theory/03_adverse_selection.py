"""
Exercise: Adverse Selection and Optimal Contracts
==================================================

Adverse selection occurs when one party has private information before contracting.
The uninformed party must design contracts to screen different types.

Classic examples:
- Insurance markets (Rothschild-Stiglitz)
- Used car market (Akerlof's "lemons")
- Credit markets

Learning Objectives:
- Understand adverse selection problems
- Design separating contracts
- Analyze pooling equilibria
- Study market unraveling

Key Concepts:
- Hidden information (types)
- Screening through self-selection
- Separating vs pooling equilibria
- Lemons problem and market breakdown
- Cream-skimming
"""

from typing import Dict, List, Tuple, Callable
import numpy as np


def rothschild_stiglitz_insurance(prob_accident_high: float,
                                  prob_accident_low: float,
                                  loss_amount: float,
                                  fraction_high_risk: float,
                                  risk_aversion: float) -> Dict:
    """
    Find Rothschild-Stiglitz equilibrium in insurance market.

    Two types of customers (high and low risk) choose from menu of contracts.
    Each contract specifies (premium, coverage).

    Separating equilibrium:
    - High-risk gets full insurance at actuarially fair price
    - Low-risk gets partial insurance to signal their type

    Args:
        prob_accident_high: P(accident) for high-risk type
        prob_accident_low: P(accident) for low-risk type
        loss_amount: Loss if accident occurs
        fraction_high_risk: Fraction of population that is high-risk
        risk_aversion: Coefficient of risk aversion

    Returns:
        Separating equilibrium contracts
    """
    # TODO: Find Rothschild-Stiglitz separating equilibrium
    #
    # High-risk contract:
    # - Full insurance: coverage = loss_amount
    # - Premium: p_H * loss_amount (actuarially fair for high-risk)
    #
    # Low-risk contract:
    # - Partial insurance (distorted to prevent high-risk from mimicking)
    # - Premium: p_L * coverage (actuarially fair for low-risk)
    #
    # IC constraint for high-risk:
    # U_H(high-risk contract) >= U_H(low-risk contract)
    #
    # Return: {
    #   'high_risk': {'premium': ..., 'coverage': ...},
    #   'low_risk': {'premium': ..., 'coverage': ...},
    #   'equilibrium_type': 'separating'/'pooling'/'none'
    # }
    #
    # Note: Separating equilibrium may not exist if fraction_high_risk is large
    pass


def lemons_market(quality_distribution: List[Tuple[float, float]],
                 seller_valuation_factor: float,
                 buyer_max_price: float) -> Dict:
    """
    Analyze Akerlof's lemons problem in used car market.

    Sellers know car quality, buyers only know distribution.
    At any price p, only cars with seller_value <= p are sold.
    Buyers anticipate this and adjust their willingness to pay.

    Args:
        quality_distribution: List of (quality, fraction) tuples
        seller_valuation_factor: Seller values quality at factor * quality
        buyer_max_price: Buyer values quality at max_price * quality

    Returns:
        Market equilibrium outcome
    """
    # TODO: Analyze lemons market
    #
    # Adverse selection cascade:
    # 1. At price p, sellers with value <= p sell
    # 2. Average quality of cars for sale = E[quality | seller_value <= p]
    # 3. Buyers willing to pay buyer_max_price * E[quality | sale]
    # 4. Equilibrium: p* such that p = buyer_willingness(p)
    #
    # May result in market unraveling:
    # - Only low-quality cars traded ("lemons")
    # - Or complete market breakdown
    #
    # Return: {
    #   'equilibrium_price': p*,
    #   'average_quality_traded': ...,
    #   'fraction_market_active': ...,
    #   'efficiency_loss': ...
    # }
    pass


def optimal_screening_menu(types: List[str],
                           type_probs: Dict[str, float],
                           cost_function: Callable,
                           valuation_function: Callable) -> Dict:
    """
    Design optimal screening menu for a monopolist facing heterogeneous types.

    Monopolist offers menu of (quantity, price) bundles.
    High type gets efficient quantity, low type gets distorted quantity.

    Args:
        types: List of customer types
        type_probs: Probability of each type
        cost_function: Cost to serve quantity q
        valuation_function: (quantity, type) -> customer value

    Returns:
        Optimal menu of contracts
    """
    # TODO: Design optimal screening menu (second-degree price discrimination)
    #
    # For two types (High, Low):
    # High type:
    #   - Efficient quantity: MV_H(q) = MC(q)
    #   - Extract all surplus via fixed fee
    #
    # Low type:
    #   - Distorted quantity (below efficient)
    #   - Distortion prevents high type from mimicking
    #
    # IC constraints:
    # U_H(contract_H) >= U_H(contract_L)
    # U_L(contract_L) >= U_L(contract_H)
    #
    # PC constraint:
    # U_L(contract_L) >= 0  (binds in optimum)
    #
    # Return: {
    #   type: {'quantity': q, 'price': T},
    #   ...
    # }
    pass


def signaling_vs_screening(education_cost_high: float,
                          education_cost_low: float,
                          productivity_high: float,
                          productivity_low: float,
                          prior_high: float) -> Dict:
    """
    Compare signaling (worker chooses education) vs screening (employer offers menu).

    Signaling: High-ability workers choose education to signal type
    Screening: Employer offers different wage-education packages

    Args:
        education_cost_high: Education cost for high ability
        education_cost_low: Education cost for low ability
        productivity_high: High ability productivity
        productivity_low: Low ability productivity
        prior_high: Probability of high ability

    Returns:
        Comparison of signaling and screening outcomes
    """
    # TODO: Compare signaling and screening
    #
    # Signaling (worker moves first):
    # - High ability chooses education e >= e* to separate
    # - Minimum e*: low ability indifferent to mimicking
    # - Can have multiple equilibria (different e*)
    #
    # Screening (employer moves first):
    # - Employer offers menu of (wage, education_requirement)
    # - Unique equilibrium (typically)
    # - May be more efficient (less wasteful signaling)
    #
    # Return: {
    #   'signaling': {'education_high': ..., 'education_low': ...},
    #   'screening': {'education_high': ..., 'education_low': ...},
    #   'welfare_comparison': ...
    # }
    pass


def credit_market_adverse_selection(prob_repay_good: float,
                                   prob_repay_bad: float,
                                   fraction_good: float,
                                   loan_amount: float,
                                   interest_rate_range: Tuple[float, float]) -> Dict:
    """
    Analyze adverse selection in credit markets.

    Borrowers know their repayment probability, lenders don't.
    Higher interest rates drive away good borrowers (adverse selection).

    Args:
        prob_repay_good: P(repayment) for good borrowers
        prob_repay_bad: P(repayment) for bad borrowers
        fraction_good: Fraction of good borrowers
        loan_amount: Amount borrowed
        interest_rate_range: (min_rate, max_rate) to consider

    Returns:
        Equilibrium interest rate and market outcomes
    """
    # TODO: Analyze credit market adverse selection
    #
    # At interest rate r:
    # - Good borrower accepts if: benefit >= (1 + r) * loan
    # - Bad borrower may accept even if expected not to repay
    #
    # As r increases:
    # - Good borrowers drop out → average quality decreases
    # - Lender's expected return may decrease!
    #
    # May lead to credit rationing:
    # - Lender won't raise r even with excess demand
    # - Raising r worsens borrower pool
    #
    # Return: {
    #   'equilibrium_rate': r*,
    #   'fraction_good_borrowers': ...,
    #   'lender_profit': ...,
    #   'credit_rationing': True/False
    # }
    pass


# Test functions
def test_rothschild_stiglitz():
    """Test insurance market equilibrium."""
    result = rothschild_stiglitz_insurance(
        prob_accident_high=0.4,
        prob_accident_low=0.1,
        loss_amount=10000,
        fraction_high_risk=0.3,
        risk_aversion=0.5
    )

    assert result is not None

    # High-risk should get full insurance
    if 'high_risk' in result:
        assert result['high_risk']['coverage'] == 10000

    print(f"✓ Rothschild-Stiglitz equilibrium:")
    print(f"  Type: {result.get('equilibrium_type', 'unknown')}")


def test_lemons_market():
    """Test lemons problem."""
    # Quality uniformly distributed from 0 to 100
    quality_dist = [(q, 0.01) for q in range(100)]

    result = lemons_market(
        quality_distribution=quality_dist,
        seller_valuation_factor=0.8,
        buyer_max_price=1.0
    )

    assert result is not None

    # Market should partially unravel
    fraction_active = result['fraction_market_active']
    assert 0 <= fraction_active <= 1

    print(f"✓ Lemons market: {fraction_active:.1%} of market active")


def test_screening_menu():
    """Test optimal screening menu."""
    def cost(q):
        return 10 * q

    def valuation(q, customer_type):
        v = {'High': 50, 'Low': 30}
        return v[customer_type] * q

    result = optimal_screening_menu(
        types=['High', 'Low'],
        type_probs={'High': 0.4, 'Low': 0.6},
        cost_function=cost,
        valuation_function=valuation
    )

    assert result is not None
    assert 'High' in result and 'Low' in result

    # High type should get larger quantity
    q_high = result['High']['quantity']
    q_low = result['Low']['quantity']
    assert q_high >= q_low

    print(f"✓ Screening menu:")
    print(f"  High type: q={q_high:.2f}, price={result['High']['price']:.2f}")
    print(f"  Low type: q={q_low:.2f}, price={result['Low']['price']:.2f}")


def test_credit_market():
    """Test credit market adverse selection."""
    result = credit_market_adverse_selection(
        prob_repay_good=0.95,
        prob_repay_bad=0.6,
        fraction_good=0.7,
        loan_amount=1000,
        interest_rate_range=(0.05, 0.3)
    )

    assert result is not None

    print(f"✓ Credit market: r={result['equilibrium_rate']:.2%}")


if __name__ == "__main__":
    print("\n=== Adverse Selection Tests ===\n")
    test_rothschild_stiglitz()
    test_lemons_market()
    test_screening_menu()
    test_credit_market()
    print("\n🎉 All tests passed! You understand adverse selection!")

    print("\n=== Key Insights ===")
    print("• Adverse selection: hidden information before contracting")
    print("• Rothschild-Stiglitz: separating contracts in insurance")
    print("• Lemons problem: market can unravel with asymmetric info")
    print("• Screening: high type gets efficient allocation, low type distorted")
    print("• Credit markets: adverse selection can cause rationing")
    print("• Signaling vs screening: who moves first matters")
