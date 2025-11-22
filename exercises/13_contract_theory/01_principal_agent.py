"""
Exercise: Principal-Agent Problem
==================================

The principal-agent problem arises when one party (principal) hires another
(agent) to perform tasks, but cannot perfectly observe the agent's effort.

Classic example: employer (principal) and worker (agent).

Learning Objectives:
- Understand hidden action problems
- Design optimal contracts under moral hazard
- Analyze effort incentives
- Trade-off between risk and incentives

Key Concepts:
- Hidden action (moral hazard)
- Incentive compatibility
- Participation constraint
- Risk-sharing vs incentives trade-off
- Piece-rate vs fixed wage
"""

from typing import Dict, Tuple, Callable
import numpy as np


def first_best_effort(output_high: float, output_low: float,
                     prob_high_if_high_effort: float,
                     prob_high_if_low_effort: float,
                     effort_cost_high: float,
                     effort_cost_low: float = 0) -> Dict:
    """
    Calculate first-best (efficient) effort level.

    First-best is what a social planner would choose if effort were observable.
    Choose effort to maximize total surplus: E[output] - effort_cost

    Args:
        output_high: Output if high realization
        output_low: Output if low realization
        prob_high_if_high_effort: P(high output | high effort)
        prob_high_if_low_effort: P(high output | low effort)
        effort_cost_high: Cost of exerting high effort
        effort_cost_low: Cost of exerting low effort (typically 0)

    Returns:
        Dictionary with optimal effort and expected surplus
    """
    # TODO: Calculate first-best effort
    # Expected output with high effort: p_H * y_H + (1-p_H) * y_L
    # Expected output with low effort: p_L * y_H + (1-p_L) * y_L
    # Net surplus with high effort: E[output | high] - c_high
    # Net surplus with low effort: E[output | low] - c_low
    # Choose effort that maximizes net surplus
    # Return: {'optimal_effort': 'high'/'low', 'expected_surplus': ...}
    pass


def design_optimal_contract(output_high: float, output_low: float,
                           prob_high_if_high_effort: float,
                           prob_high_if_low_effort: float,
                           effort_cost: float,
                           agent_outside_utility: float,
                           agent_risk_aversion: float = 0) -> Dict:
    """
    Design optimal incentive contract under moral hazard.

    Principal wants agent to exert high effort but cannot observe effort.
    Must design payment scheme (w_high, w_low) to induce high effort.

    Constraints:
    - IC: Agent prefers high effort to low effort
    - PC: Agent accepts the contract

    Args:
        output_high: Output if high realization
        output_low: Output if low realization
        prob_high_if_high_effort: P(high | high effort)
        prob_high_if_low_effort: P(high | low effort)
        effort_cost: Cost of high effort (low effort costs 0)
        agent_outside_utility: Agent's reservation utility
        agent_risk_aversion: 0 for risk-neutral, >0 for risk-averse

    Returns:
        Optimal wages for high and low output
    """
    # TODO: Design optimal contract
    # For risk-neutral agent:
    # IC constraint: p_H*(w_H - w_L) >= c
    # PC constraint: p_H*w_H + (1-p_H)*w_L - c >= U_0
    # Principal minimizes: p_H*w_H + (1-p_H)*w_L
    #
    # Optimal: Set IC to bind (minimize wage bill)
    # w_H - w_L = c / (p_H - p_L)  (if p_H > p_L)
    # Set PC to bind: p_H*w_H + (1-p_H)*w_L = U_0 + c
    #
    # Solve for w_H and w_L
    # Return: {'wage_high': w_H, 'wage_low': w_L, 'expected_wage': ..., 'principal_profit': ...}
    pass


def analyze_risk_sharing(output_high: float, output_low: float,
                        prob_high: float, principal_risk_aversion: float,
                        agent_risk_aversion: float) -> Dict:
    """
    Analyze optimal risk-sharing without moral hazard.

    When effort is observable, contract is about sharing risk optimally.
    With risk-neutral principal and risk-averse agent: principal bears all risk (fixed wage).
    With both risk-averse: share risk according to relative risk aversion.

    Args:
        output_high: High output level
        output_low: Low output level
        prob_high: Probability of high output
        principal_risk_aversion: Principal's risk aversion parameter
        agent_risk_aversion: Agent's risk aversion parameter

    Returns:
        Optimal risk-sharing arrangement
    """
    # TODO: Determine optimal risk-sharing
    # If principal is risk-neutral (r_P = 0) and agent is risk-averse (r_A > 0):
    #   → Fixed wage (principal bears all risk)
    # If both risk-neutral: any sharing works
    # If both risk-averse: share risk based on relative aversion
    #
    # With observable effort, can separate risk-sharing from incentives
    # Return: {'wage_high': ..., 'wage_low': ..., 'type': 'fixed'/'variable'}
    pass


def compare_contracts(output_high: float, output_low: float,
                     prob_high_if_high_effort: float,
                     effort_cost: float) -> Dict:
    """
    Compare different contract types: fixed wage, piece rate, optimal contract.

    Args:
        output_high: High output level
        output_low: Low output level
        prob_high_if_high_effort: P(high | high effort)
        effort_cost: Cost of high effort

    Returns:
        Comparison of contracts
    """
    # TODO: Compare contract types
    # 1. Fixed wage w: agent chooses low effort (no incentive)
    # 2. Pure piece rate: w = α * output (strong incentives, agent bears risk)
    # 3. Optimal contract: balances incentives and risk-sharing
    #
    # Return: {
    #   'fixed_wage': {'effort': 'low', 'profit': ...},
    #   'piece_rate': {'effort': 'high', 'profit': ...},
    #   'optimal': {'effort': 'high', 'profit': ...}
    # }
    pass


# Test functions
def test_first_best():
    """Test first-best effort calculation."""
    result = first_best_effort(
        output_high=100,
        output_low=20,
        prob_high_if_high_effort=0.8,
        prob_high_if_low_effort=0.3,
        effort_cost_high=30,
        effort_cost_low=0
    )

    assert result is not None

    # E[output | high effort] = 0.8*100 + 0.2*20 = 84
    # E[output | low effort] = 0.3*100 + 0.7*20 = 44
    # Surplus with high effort: 84 - 30 = 54
    # Surplus with low effort: 44 - 0 = 44
    # High effort is first-best

    assert result['optimal_effort'] == 'high'

    print(f"✓ First-best effort: {result['optimal_effort']}, surplus={result['expected_surplus']:.2f}")


def test_optimal_contract():
    """Test optimal contract design."""
    result = design_optimal_contract(
        output_high=100,
        output_low=20,
        prob_high_if_high_effort=0.8,
        prob_high_if_low_effort=0.3,
        effort_cost=30,
        agent_outside_utility=0,
        agent_risk_aversion=0
    )

    assert result is not None
    w_high = result['wage_high']
    w_low = result['wage_low']

    # IC: 0.8*w_H + 0.2*w_L - 30 >= 0.3*w_H + 0.7*w_L
    # => 0.5*(w_H - w_L) >= 30 => w_H - w_L >= 60

    # Should have w_high > w_low (incentives)
    assert w_high > w_low, "High output wage should exceed low output wage"

    print(f"✓ Optimal contract: w_high={w_high:.2f}, w_low={w_low:.2f}")


def test_risk_sharing():
    """Test risk-sharing analysis."""
    result = analyze_risk_sharing(
        output_high=100,
        output_low=50,
        prob_high=0.6,
        principal_risk_aversion=0,    # Risk-neutral
        agent_risk_aversion=0.5       # Risk-averse
    )

    assert result is not None

    # With risk-neutral principal and risk-averse agent:
    # Optimal to give fixed wage (principal bears all risk)
    if 'type' in result:
        assert result['type'] == 'fixed', "Should be fixed wage with risk-neutral principal"

    print(f"✓ Risk-sharing: {result}")


def test_contract_comparison():
    """Test comparison of contract types."""
    comparison = compare_contracts(
        output_high=100,
        output_low=20,
        prob_high_if_high_effort=0.8,
        effort_cost=30
    )

    assert comparison is not None

    # Optimal contract should give highest principal profit
    # (among contracts inducing high effort)

    print(f"✓ Contract comparison:")
    for contract_type, details in comparison.items():
        print(f"  {contract_type}: {details}")


if __name__ == "__main__":
    print("\n=== Principal-Agent Problem Tests ===\n")
    test_first_best()
    test_optimal_contract()
    test_risk_sharing()
    test_contract_comparison()
    print("\n🎉 All tests passed! You understand principal-agent problems!")

    print("\n=== Key Insights ===")
    print("• Moral hazard: hidden action creates agency problem")
    print("• Incentive compatibility: agent must prefer desired effort")
    print("• Trade-off: risk-sharing vs incentives")
    print("• Risk-neutral agent: can use high-powered incentives")
    print("• Risk-averse agent: optimal contract shares risk, weakens incentives")
    print("• First-best (observable effort) vs second-best (hidden effort)")
