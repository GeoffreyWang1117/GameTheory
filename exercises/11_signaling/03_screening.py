"""
Exercise: Screening and Adverse Selection
==========================================

Screening is the dual of signaling: the uninformed party designs a mechanism
to induce the informed party to reveal their type through self-selection.

Classic examples:
- Insurance companies offering different contracts
- Employers offering different salary-bonus combinations
- Monopolist offering different pricing plans

Learning Objectives:
- Understand screening mechanisms
- Design incentive-compatible contracts
- Handle adverse selection problems
- Apply revelation principle

Key Concepts:
- Adverse selection
- Self-selection constraints
- Participation constraints
- Second-degree price discrimination
- Mechanism design for screening
"""

from typing import Dict, List, Tuple, Callable
import numpy as np


def design_screening_contracts(types: List[str], type_probs: Dict[str, float],
                               valuations: Dict[str, float],
                               costs: Dict[str, float]):
    """
    Design optimal screening contracts for different types.

    The principal (uninformed) offers a menu of contracts. Each type (informed)
    selects the contract that maximizes their utility. The principal maximizes
    expected profit subject to:
    - Participation constraints (each type accepts)
    - Incentive compatibility (each type prefers their contract)

    Args:
        types: List of types (e.g., ['High', 'Low'])
        type_probs: Probability of each type
        valuations: Value/utility function for each type
        costs: Cost for principal to serve each type

    Returns:
        Dictionary of optimal contracts for each type
    """
    # TODO: Design screening contracts
    # For two types (High, Low):
    # - High type gets efficient allocation (no distortion)
    # - Low type gets distorted allocation to prevent high type from mimicking
    # - Incentive compatibility: U_H(contract_H) >= U_H(contract_L)
    # - Participation: U_L(contract_L) >= 0
    # Return format: {'High': (quantity, price), 'Low': (quantity, price)}
    pass


def check_incentive_compatibility(contracts: Dict[str, Tuple],
                                  utility_func: Callable) -> bool:
    """
    Check if contracts satisfy incentive compatibility constraints.

    Each type should prefer their designated contract over any other.

    Args:
        contracts: {type: (quantity, price)} - contract menu
        utility_func: (quantity, price, type) -> utility

    Returns:
        True if all IC constraints satisfied
    """
    # TODO: For each type, verify they prefer their contract to all others
    # For type t: U(contract[t], t) >= U(contract[t'], t) for all t' != t
    pass


def insurance_screening(prob_accident_high: float, prob_accident_low: float,
                       loss: float, risk_aversion: float,
                       prior_high: float):
    """
    Design insurance contracts to screen high and low risk types.

    Setup:
    - Two types: high-risk and low-risk
    - Risk-averse individuals with utility u(w) = sqrt(w)
    - Individuals know their type, insurer doesn't
    - Insurer offers menu of (premium, coverage) pairs

    Args:
        prob_accident_high: Accident probability for high-risk type
        prob_accident_low: Accident probability for low-risk type
        loss: Loss if accident occurs
        risk_aversion: Coefficient of risk aversion
        prior_high: Probability of high-risk type

    Returns:
        Optimal insurance contracts for each type
    """
    # TODO: Design insurance contracts
    # High-risk type gets full insurance (efficient)
    # Low-risk type gets partial insurance (to separate from high-risk)
    # IC constraint: High-risk won't mimic low-risk
    # Premium must cover expected cost for each type
    # Return: {'high_risk': (premium, coverage), 'low_risk': (premium, coverage)}
    pass


def quantity_discount_screening(demand_high: Callable, demand_low: Callable,
                                marginal_cost: float, prob_high: float):
    """
    Design quantity discount (two-part tariff) to screen consumer types.

    A monopolist faces two types of consumers with different demand curves.
    Monopolist can't observe type but can offer menu of (fixed_fee, per_unit_price).

    Args:
        demand_high: Demand function for high type q(p)
        demand_low: Demand function for low type q(p)
        marginal_cost: Cost per unit
        prob_high: Probability of high type

    Returns:
        Optimal two-part tariffs for each type
    """
    # TODO: Design two-part tariff menu
    # High type: Set p = MC, extract all surplus with fixed fee
    # Low type: Distort price above MC to prevent high type from mimicking
    # Return: {'high': (fixed_fee, price), 'low': (fixed_fee, price)}
    pass


def revelation_principle_screening(types: List[str],
                                   payoff_func: Callable,
                                   actions: List):
    """
    Apply revelation principle to find optimal direct mechanism.

    The revelation principle states that any outcome achievable by an indirect
    mechanism can be achieved by a direct truthful mechanism.

    Args:
        types: List of possible types
        payoff_func: (reported_type, true_type, action) -> payoff
        actions: List of possible actions/allocations

    Returns:
        Direct mechanism mapping each type to an action
    """
    # TODO: Design direct revelation mechanism
    # Find action for each type such that:
    # 1. Truth-telling is optimal (IC)
    # 2. Participation constraints met
    # 3. Principal's objective maximized
    # Return: {type: optimal_action}
    pass


# Test functions
def test_incentive_compatibility():
    """Test IC constraint checking."""
    contracts = {
        'High': (10, 50),  # (quantity, price)
        'Low': (5, 20)
    }

    def utility(quantity, price, type):
        # Higher type has higher valuation
        value_per_unit = 8 if type == 'High' else 5
        return value_per_unit * quantity - price

    is_ic = check_incentive_compatibility(contracts, utility)

    # Check manually:
    # High choosing High: 8*10 - 50 = 30
    # High choosing Low: 8*5 - 20 = 20
    # Low choosing Low: 5*5 - 20 = 5
    # Low choosing High: 5*10 - 50 = 0
    # IC satisfied if 30 >= 20 (yes) and 5 >= 0 (yes)

    assert is_ic is not None
    print(f"✓ Incentive compatibility check: {is_ic}")


def test_screening_contracts():
    """Test contract design."""
    contracts = design_screening_contracts(
        types=['High', 'Low'],
        type_probs={'High': 0.3, 'Low': 0.7},
        valuations={'High': 10, 'Low': 5},
        costs={'High': 2, 'Low': 2}
    )

    assert contracts is not None
    assert 'High' in contracts and 'Low' in contracts

    print(f"✓ Screening contracts designed:")
    print(f"  High type: {contracts['High']}")
    print(f"  Low type: {contracts['Low']}")


def test_insurance_screening():
    """Test insurance contract design."""
    contracts = insurance_screening(
        prob_accident_high=0.4,
        prob_accident_low=0.1,
        loss=10000,
        risk_aversion=0.5,
        prior_high=0.2
    )

    assert contracts is not None
    assert 'high_risk' in contracts and 'low_risk' in contracts

    high_premium, high_coverage = contracts['high_risk']
    low_premium, low_coverage = contracts['low_risk']

    # High-risk should get full coverage in separating equilibrium
    # Low-risk gets partial coverage (distorted down)
    assert high_coverage >= low_coverage, "High-risk should get more coverage"

    print(f"✓ Insurance screening:")
    print(f"  High-risk: premium=${high_premium:.2f}, coverage=${high_coverage:.2f}")
    print(f"  Low-risk: premium=${low_premium:.2f}, coverage=${low_coverage:.2f}")


def test_quantity_discount():
    """Test quantity discount screening."""
    # Linear demand: q = a - b*p
    demand_high = lambda p: max(0, 100 - 2*p)
    demand_low = lambda p: max(0, 60 - 2*p)

    contracts = quantity_discount_screening(
        demand_high, demand_low,
        marginal_cost=10,
        prob_high=0.3
    )

    assert contracts is not None
    print(f"✓ Quantity discount screening:")
    print(f"  High type: {contracts['high']}")
    print(f"  Low type: {contracts['low']}")


if __name__ == "__main__":
    print("\n=== Screening and Adverse Selection Tests ===\n")
    test_incentive_compatibility()
    test_screening_contracts()
    test_insurance_screening()
    test_quantity_discount()
    print("\n🎉 All tests passed! You understand screening mechanisms!")

    print("\n=== Key Insights ===")
    print("• Screening induces self-selection through contract menus")
    print("• High type gets efficient allocation (no distortion)")
    print("• Low type allocation is distorted to prevent mimicry")
    print("• IC constraints: each type prefers their contract")
    print("• Applications: insurance, pricing, employment contracts")
    print("• Revelation principle: focus on direct truthful mechanisms")
