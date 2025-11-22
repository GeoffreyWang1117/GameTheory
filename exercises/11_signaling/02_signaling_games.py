"""
Exercise: Signaling Games and Perfect Bayesian Equilibrium
===========================================================

Signaling games model situations where an informed player (sender) takes an action
that may reveal information to an uninformed player (receiver), who then responds.

Classic example: Spence's job market signaling model, where workers signal their
ability through education.

Learning Objectives:
- Understand signaling games structure
- Find Perfect Bayesian Equilibria (PBE)
- Distinguish separating and pooling equilibria
- Apply to education signaling and market signaling

Key Concepts:
- Sender and receiver
- Signals and beliefs
- Separating equilibrium (different types send different signals)
- Pooling equilibrium (all types send same signal)
- Perfect Bayesian Equilibrium
"""

from typing import Dict, Tuple, List, Callable
import numpy as np


def update_beliefs_bayes_rule(signal, type_priors, signal_probs):
    """
    Update beliefs about sender's type using Bayes' rule after observing a signal.

    P(type | signal) = P(signal | type) * P(type) / P(signal)

    Args:
        signal: Observed signal
        type_priors: Dictionary {type: prior probability}
        signal_probs: Dictionary {(type, signal): probability of signal given type}

    Returns:
        Dictionary {type: posterior probability}
    """
    # TODO: Apply Bayes' rule to update beliefs
    # 1. Calculate P(signal) = sum over types of P(signal|type) * P(type)
    # 2. For each type, calculate P(type|signal) = P(signal|type) * P(type) / P(signal)
    pass


def spence_education_signaling(cost_high: float, cost_low: float,
                               wage_high: float, wage_low: float,
                               prob_high: float):
    """
    Analyze Spence's education signaling model.

    Setup:
    - Workers are high or low ability (known to worker, unknown to employer)
    - Workers choose education level e >= 0
    - Education is more costly for low ability: cost = c(e, type)
    - Employers observe education and offer wage based on beliefs
    - High ability workers are more productive

    Payoff for worker: wage - cost(e, type)

    Args:
        cost_high: Cost per unit education for high ability
        cost_low: Cost per unit education for low ability
        wage_high: Wage for believed high ability worker
        wage_low: Wage for believed low ability worker
        prob_high: Prior probability of high ability

    Returns:
        Dictionary with separating equilibrium education levels
    """
    # TODO: Find a separating equilibrium where high ability workers signal with education
    # In separating equilibrium:
    # - High ability chooses e_H such that: wage_high - cost_high * e_H >= wage_low
    # - Low ability chooses e_L = 0 such that: wage_low >= wage_high - cost_low * e_H
    # - The second condition (incentive compatibility) determines minimum e_H
    # Return {'high_ability_education': e_H, 'low_ability_education': 0}
    pass


def check_separating_equilibrium(strategies: Dict[str, float], beliefs: Dict[float, str],
                                 cost_func: Callable, wage_func: Callable,
                                 types: List[str]) -> bool:
    """
    Check if a strategy profile and beliefs constitute a separating equilibrium.

    Args:
        strategies: {type: signal_chosen}
        beliefs: {signal: inferred_type}
        cost_func: (signal, type) -> cost
        wage_func: (inferred_type) -> wage
        types: List of possible types

    Returns:
        True if this is a valid separating PBE
    """
    # TODO: Verify separating equilibrium conditions:
    # 1. Different types choose different signals
    # 2. Beliefs are correct on equilibrium path (Bayes' rule)
    # 3. Each type's signal maximizes their payoff given resulting wage
    # 4. Wages are optimal responses to beliefs
    pass


def check_pooling_equilibrium(signal: float, beliefs: Dict[str, float],
                              cost_func: Callable, wage_func: Callable,
                              types: List[str], type_priors: Dict[str, float]) -> bool:
    """
    Check if a pooling equilibrium exists where all types choose the same signal.

    Args:
        signal: The common signal all types send
        beliefs: Posterior beliefs about type (should equal priors in pooling)
        cost_func: (signal, type) -> cost
        wage_func: (beliefs) -> wage offered
        types: List of possible types
        type_priors: Prior probabilities of types

    Returns:
        True if this is a valid pooling PBE
    """
    # TODO: Verify pooling equilibrium conditions:
    # 1. All types send the same signal
    # 2. Beliefs equal priors (no information revealed)
    # 3. No type wants to deviate to a different signal
    # 4. Out-of-equilibrium beliefs must support no deviation
    pass


def find_least_cost_separating_equilibrium(types: List[str],
                                           costs: Dict[str, float],
                                           wages: Dict[str, float],
                                           prior_high: float):
    """
    Find the least-cost separating equilibrium in a signaling game.

    The Riley outcome is the separating equilibrium with minimal signaling by high type.

    Args:
        types: ['High', 'Low']
        costs: Cost per unit of signal {'High': c_H, 'Low': c_L} with c_L > c_H
        wages: Wages for each type {'High': w_H, 'Low': w_L} with w_H > w_L
        prior_high: Prior probability of high type

    Returns:
        Minimum education level for high type that separates
    """
    # TODO: Find minimum signal e* such that:
    # High type prefers (wage_high, e*) to (wage_low, 0):
    #   wage_high - cost_high * e* >= wage_low
    # Low type prefers (wage_low, 0) to (wage_high, e*):
    #   wage_low >= wage_high - cost_low * e*
    # The second constraint binds, giving: e* = (wage_high - wage_low) / cost_low
    pass


# Test functions
def test_bayes_rule():
    """Test belief updating."""
    type_priors = {'High': 0.3, 'Low': 0.7}
    signal_probs = {
        ('High', 'Signal_A'): 0.8,
        ('High', 'Signal_B'): 0.2,
        ('Low', 'Signal_A'): 0.3,
        ('Low', 'Signal_B'): 0.7
    }

    beliefs = update_beliefs_bayes_rule('Signal_A', type_priors, signal_probs)

    # P(Signal_A) = 0.3 * 0.8 + 0.7 * 0.3 = 0.24 + 0.21 = 0.45
    # P(High | Signal_A) = 0.8 * 0.3 / 0.45 = 0.24 / 0.45 ≈ 0.533
    # P(Low | Signal_A) = 0.3 * 0.7 / 0.45 = 0.21 / 0.45 ≈ 0.467

    assert beliefs is not None
    assert abs(beliefs['High'] - 0.533) < 0.01, f"Expected 0.533, got {beliefs['High']}"
    print(f"✓ Bayes rule updating: P(High|Signal_A) = {beliefs['High']:.3f}")


def test_spence_signaling():
    """Test education signaling model."""
    result = spence_education_signaling(
        cost_high=1.0,    # High ability cost per year
        cost_low=2.0,     # Low ability cost per year (more costly)
        wage_high=50,     # Wage if believed high ability
        wage_low=20,      # Wage if believed low ability
        prob_high=0.4
    )

    assert result is not None
    assert 'high_ability_education' in result
    assert 'low_ability_education' in result

    e_high = result['high_ability_education']
    e_low = result['low_ability_education']

    # In separating equilibrium, low ability chooses 0
    assert e_low == 0, "Low ability should choose no education in separating equilibrium"

    # High ability must signal enough that low ability won't mimic
    # Incentive compatibility: 20 >= 50 - 2 * e_high => e_high >= 15
    assert e_high >= 15, f"Education signal too low: {e_high}"

    print(f"✓ Spence signaling equilibrium: High={e_high} years, Low={e_low} years")


def test_separating_equilibrium():
    """Test separating equilibrium verification."""
    strategies = {'High': 2.0, 'Low': 0.0}
    beliefs = {2.0: 'High', 0.0: 'Low'}

    def cost(signal, type):
        return signal * (1.0 if type == 'High' else 2.0)

    def wage(believed_type):
        return 50 if believed_type == 'High' else 20

    is_separating = check_separating_equilibrium(
        strategies, beliefs, cost, wage, ['High', 'Low']
    )

    assert is_separating is not None
    print(f"✓ Separating equilibrium check: {is_separating}")


def test_least_cost_separating():
    """Test Riley outcome."""
    min_education = find_least_cost_separating_equilibrium(
        types=['High', 'Low'],
        costs={'High': 1.0, 'Low': 2.0},
        wages={'High': 50, 'Low': 20},
        prior_high=0.4
    )

    assert min_education is not None
    expected = (50 - 20) / 2.0  # (w_H - w_L) / c_L = 30 / 2 = 15
    assert abs(min_education - expected) < 0.01, f"Expected {expected}, got {min_education}"
    print(f"✓ Least-cost separating (Riley): {min_education} years of education")


if __name__ == "__main__":
    print("\n=== Signaling Games Tests ===\n")
    test_bayes_rule()
    test_spence_signaling()
    test_separating_equilibrium()
    test_least_cost_separating()
    print("\n🎉 All tests passed! You understand signaling games!")

    print("\n=== Key Insights ===")
    print("• Signaling reveals private information through costly actions")
    print("• Separating equilibrium: different types send different signals")
    print("• Pooling equilibrium: all types send the same signal (no information)")
    print("• Education can be a signal even if it doesn't increase productivity")
    print("• Least-cost separating (Riley outcome) minimizes wasteful signaling")
