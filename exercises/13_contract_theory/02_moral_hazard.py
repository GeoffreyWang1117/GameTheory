"""
Exercise: Moral Hazard in Insurance and Finance
================================================

Moral hazard occurs when one party's actions are hidden and affect the outcome
of a transaction. Common in insurance (hidden precaution) and finance (hidden effort).

Learning Objectives:
- Understand moral hazard in various contexts
- Design contracts to mitigate moral hazard
- Analyze deductibles and co-insurance
- Study monitoring and incentives

Key Concepts:
- Hidden action after contracting
- Effort choice and prevention
- Deductibles and co-payments
- Monitoring costs
- Bonding and collateral
"""

from typing import Dict, Tuple, Callable
import numpy as np


def insurance_moral_hazard(loss_amount: float, prob_accident_careful: float,
                          prob_accident_careless: float, effort_cost: float,
                          insurance_loading: float = 0) -> Dict:
    """
    Analyze moral hazard in insurance markets.

    Individual can exert effort (care) to reduce accident probability.
    Insurer cannot observe effort level.

    Args:
        loss_amount: Financial loss if accident occurs
        prob_accident_careful: P(accident | careful)
        prob_accident_careless: P(accident | careless)
        effort_cost: Cost of being careful
        insurance_loading: Insurance company markup (0 = actuarially fair)

    Returns:
        Optimal insurance coverage accounting for moral hazard
    """
    # TODO: Analyze insurance with moral hazard
    #
    # Full insurance eliminates incentive to be careful:
    # If fully insured, individual is careless (saves effort cost)
    #
    # Optimal contract uses partial insurance:
    # - Deductible or co-insurance
    # - Individual bears some risk → incentive to be careful
    #
    # Calculate:
    # 1. Full insurance outcome (careless behavior)
    # 2. Partial insurance that induces careful behavior
    # 3. Compare expected utilities
    #
    # Return: {
    #   'full_insurance': {'coverage': L, 'premium': ..., 'effort': 'careless'},
    #   'partial_insurance': {'coverage': ..., 'deductible': ..., 'effort': 'careful'},
    #   'optimal_type': 'full'/'partial'
    # }
    pass


def optimal_deductible(loss: float, prob_accident_careful: float,
                      prob_accident_careless: float, effort_cost: float,
                      risk_aversion: float) -> float:
    """
    Calculate optimal deductible to induce careful behavior.

    Deductible D creates incentive to be careful while providing insurance.

    Args:
        loss: Loss amount if accident
        prob_accident_careful: P(accident | careful)
        prob_accident_careless: P(accident | careless)
        effort_cost: Cost of being careful
        risk_aversion: Coefficient of risk aversion

    Returns:
        Optimal deductible amount
    """
    # TODO: Find optimal deductible
    # IC constraint: Individual prefers (careful + deductible D) to (careless + deductible D)
    # EU(careful) >= EU(careless)
    # p_c*u(w - D - c) + (1-p_c)*u(w - c) >= p_r*u(w - D) + (1-p_r)*u(w)
    #
    # Higher deductible → stronger incentive to be careful
    # But also exposes individual to more risk
    #
    # Optimal D balances incentives and risk-sharing
    # Return minimum D that induces careful behavior
    pass


def monitoring_vs_incentives(output_high: float, output_low: float,
                             prob_high_if_high_effort: float,
                             effort_cost: float, monitoring_cost: float,
                             monitoring_accuracy: float) -> Dict:
    """
    Compare monitoring vs incentive pay for inducing effort.

    Principal can either:
    1. Monitor effort directly (imperfectly) at cost
    2. Use output-based incentives

    Args:
        output_high: High output level
        output_low: Low output level
        prob_high_if_high_effort: P(high output | high effort)
        effort_cost: Cost of exerting effort
        monitoring_cost: Cost of monitoring system
        monitoring_accuracy: Probability monitoring detects shirking

    Returns:
        Comparison of monitoring and incentive schemes
    """
    # TODO: Compare approaches
    #
    # Monitoring:
    # - Cost: monitoring_cost
    # - If caught shirking with prob p_detect, penalize agent
    # - Need penalty large enough to deter shirking
    #
    # Incentive pay:
    # - Cost: Higher wages for performance
    # - No monitoring cost but agent bears risk
    #
    # Choose cheaper approach
    #
    # Return: {
    #   'monitoring': {'cost': ..., 'expected_output': ...},
    #   'incentives': {'cost': ..., 'expected_output': ...},
    #   'optimal': 'monitoring'/'incentives'
    # }
    pass


def team_moral_hazard(num_workers: int, output_per_worker: float,
                     effort_cost: float, team_production_function: Callable) -> Dict:
    """
    Analyze moral hazard in team production.

    With team production, individual effort is hard to observe and reward.
    Free-riding problem: each worker has incentive to shirk.

    Args:
        num_workers: Team size
        output_per_worker: Output if all workers exert effort
        effort_cost: Cost of effort for each worker
        team_production_function: Maps (num_workers_with_effort) -> total_output

    Returns:
        Analysis of team incentive problem
    """
    # TODO: Analyze team moral hazard
    #
    # Equal sharing: Each gets 1/n of team output
    # Individual's gain from effort: (1/n) * marginal_product - cost
    # As n increases, incentive to free-ride increases
    #
    # Solutions:
    # 1. Monitoring and supervision
    # 2. Tournaments (relative performance)
    # 3. Team incentives with peer pressure
    # 4. Individual output measurement
    #
    # Calculate Nash equilibrium effort levels under equal sharing
    #
    # Return: {
    #   'equilibrium_effort_fraction': ...,  # Fraction who work
    #   'total_output': ...,
    #   'output_if_all_work': ...,
    #   'efficiency_loss': ...
    # }
    pass


def executive_compensation(firm_value_high: float, firm_value_low: float,
                          prob_high_if_high_effort: float,
                          effort_cost: float, risk_free_rate: float) -> Dict:
    """
    Design executive compensation with stock options and bonuses.

    CEO's effort affects firm value but is not observable.
    Compensation can include salary, stock, and options.

    Args:
        firm_value_high: Firm value if high realization
        firm_value_low: Firm value if low realization
        prob_high_if_high_effort: P(high value | high effort)
        effort_cost: CEO's cost of effort
        risk_free_rate: Risk-free return rate

    Returns:
        Optimal compensation package
    """
    # TODO: Design executive pay
    #
    # Components:
    # 1. Base salary (fixed)
    # 2. Bonus tied to performance
    # 3. Stock options (convex payoff)
    #
    # Stock options provide leverage: upside potential, limited downside
    # This can induce excessive risk-taking
    #
    # Optimal mix depends on:
    # - CEO risk aversion
    # - Effort cost
    # - Firm volatility
    #
    # Return: {
    #   'base_salary': ...,
    #   'performance_bonus': ...,
    #   'stock_grant': ...,
    #   'options': ...,
    #   'expected_compensation': ...
    # }
    pass


# Test functions
def test_insurance_moral_hazard():
    """Test insurance moral hazard."""
    result = insurance_moral_hazard(
        loss_amount=10000,
        prob_accident_careful=0.1,
        prob_accident_careless=0.3,
        effort_cost=200,
        insurance_loading=0.1
    )

    assert result is not None
    assert 'full_insurance' in result
    assert 'partial_insurance' in result

    # Full insurance induces careless behavior
    assert result['full_insurance']['effort'] == 'careless'

    print(f"✓ Insurance moral hazard analysis:")
    print(f"  Full insurance: {result['full_insurance']}")
    print(f"  Partial insurance: {result['partial_insurance']}")


def test_optimal_deductible():
    """Test optimal deductible calculation."""
    deductible = optimal_deductible(
        loss=5000,
        prob_accident_careful=0.1,
        prob_accident_careless=0.25,
        effort_cost=100,
        risk_aversion=0.5
    )

    assert deductible is not None
    # Deductible should be positive to create incentives
    assert deductible > 0

    print(f"✓ Optimal deductible: ${deductible:.2f}")


def test_monitoring_vs_incentives():
    """Test monitoring vs incentives comparison."""
    result = monitoring_vs_incentives(
        output_high=1000,
        output_low=400,
        prob_high_if_high_effort=0.8,
        effort_cost=50,
        monitoring_cost=100,
        monitoring_accuracy=0.9
    )

    assert result is not None
    assert 'monitoring' in result and 'incentives' in result
    assert 'optimal' in result

    print(f"✓ Monitoring vs Incentives:")
    print(f"  Optimal approach: {result['optimal']}")


def test_team_moral_hazard():
    """Test team production moral hazard."""
    def team_output(num_working):
        return 100 * num_working  # Linear in effort

    result = team_moral_hazard(
        num_workers=5,
        output_per_worker=100,
        effort_cost=30,
        team_production_function=team_output
    )

    assert result is not None

    # With equal sharing, some free-riding expected
    effort_fraction = result['equilibrium_effort_fraction']

    print(f"✓ Team moral hazard: {effort_fraction:.1%} of team works")


def test_executive_compensation():
    """Test executive compensation design."""
    result = executive_compensation(
        firm_value_high=1000000,
        firm_value_low=500000,
        prob_high_if_high_effort=0.7,
        effort_cost=10000,
        risk_free_rate=0.05
    )

    assert result is not None

    print(f"✓ Executive compensation: {result}")


if __name__ == "__main__":
    print("\n=== Moral Hazard Tests ===\n")
    test_insurance_moral_hazard()
    test_optimal_deductible()
    test_monitoring_vs_incentives()
    test_team_moral_hazard()
    test_executive_compensation()
    print("\n🎉 All tests passed! You understand moral hazard!")

    print("\n=== Key Insights ===")
    print("• Moral hazard: hidden actions reduce efficiency")
    print("• Insurance: full coverage eliminates incentive for care")
    print("• Deductibles and co-insurance create prevention incentives")
    print("• Monitoring vs incentives: trade-off between cost and effectiveness")
    print("• Team production: free-riding problem with equal sharing")
    print("• Executive pay: balance incentives, risk-sharing, and fairness")
