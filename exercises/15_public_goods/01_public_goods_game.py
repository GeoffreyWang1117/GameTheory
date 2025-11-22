"""
Exercise: Public Goods Games
=============================

Public goods games model situations where individuals can contribute to a
common pool that benefits everyone, but free-riding is tempting.

Classic examples: environmental protection, public broadcasting, open source

Learning Objectives:
- Understand free-rider problem
- Analyze voluntary contribution mechanisms
- Study threshold public goods
- Design mechanisms to elicit contributions

Key Concepts:
- Public goods (non-rival, non-excludable)
- Free-rider problem
- Dominant strategy equilibrium
- Social optimum vs equilibrium
- Provision point mechanisms
"""

from typing import List, Dict, Tuple, Callable
import numpy as np


def analyze_linear_public_good(num_players: int, endowment: float,
                               marginal_per_capita_return: float) -> Dict:
    """
    Analyze linear public goods game.

    Each player has endowment and chooses contribution to public good.
    Public good returns MPCR * (total contribution) to each player.

    Payoff for player i: (endowment - contribution_i) + MPCR * sum(contributions)

    Args:
        num_players: Number of players
        endowment: Initial endowment for each player
        marginal_per_capita_return: Return per unit contributed (MPCR)

    Returns:
        Analysis of equilibrium and optimum
    """
    # TODO: Analyze linear public goods game
    #
    # Individual incentive:
    # - Contributing 1 unit costs 1, returns MPCR to self
    # - If MPCR < 1: dominant strategy is to contribute 0 (free-ride!)
    # - If MPCR > 1: contribute entire endowment
    #
    # Social optimum:
    # - Contributing 1 unit costs 1, returns MPCR * n to group
    # - If MPCR * n > 1: optimal to contribute fully
    #
    # Tension: MPCR < 1 < MPCR * n
    # → Individual incentive (free-ride) ≠ social optimum (contribute)
    #
    # Return: {
    #   'equilibrium_contribution': ...,
    #   'optimal_contribution': ...,
    #   'equilibrium_payoff_per_player': ...,
    #   'optimal_payoff_per_player': ...,
    #   'efficiency_loss': ...
    # }
    pass


def threshold_public_good(valuations: List[float], cost: float,
                         threshold: float) -> Dict:
    """
    Analyze threshold (step-level) public good provision.

    Public good is provided if total contributions >= threshold.
    If provided, each player gets their valuation.
    Each player chooses contribution in [0, valuation].

    Args:
        valuations: List of players' values for the public good
        cost: Total cost to provide the good
        threshold: Minimum contributions needed (usually = cost)

    Returns:
        Equilibrium analysis
    """
    # TODO: Analyze threshold public good
    #
    # Multiple equilibria exist:
    # 1. No one contributes → good not provided (inefficient if sum(v) > cost)
    # 2. Enough players contribute exactly to meet threshold
    #
    # Coordination problem: who contributes?
    #
    # Equilibria:
    # - All-or-nothing equilibria where subset contributes exactly threshold
    # - Players with high valuations more likely to contribute
    #
    # Provision point mechanism: refund if threshold not met
    #
    # Return: {
    #   'will_provide': True/False,
    #   'equilibrium_contributions': [...],
    #   'total_surplus': ...
    # }
    pass


def volunteer_dilemma(num_players: int, cost_of_volunteering: float,
                     benefit_if_provided: float,
                     benefit_if_not_provided: float = 0) -> Dict:
    """
    Analyze volunteer's dilemma.

    Public good is provided if at least one player volunteers.
    Volunteering is costly, but benefits everyone.

    Example: Someone needs to report an emergency.

    Args:
        num_players: Number of players
        cost_of_volunteering: Cost to volunteer
        benefit_if_provided: Benefit when good is provided
        benefit_if_not_provided: Benefit when not provided (usually 0)

    Returns:
        Mixed strategy equilibrium
    """
    # TODO: Analyze volunteer's dilemma
    #
    # Pure strategy equilibria:
    # - Exactly one player volunteers (but which one?)
    # - n equilibria where different player volunteers
    #
    # Symmetric mixed strategy equilibrium:
    # - Each player volunteers with probability p
    # - At equilibrium, each player is indifferent
    #
    # Indifference condition:
    # EU(volunteer) = EU(not volunteer)
    # benefit - cost = benefit * P(at least one other volunteers)
    # benefit - cost = benefit * (1 - (1-p)^(n-1))
    #
    # Solve for p
    #
    # As n increases, p decreases (more free-riding)
    # But probability of provision may increase or decrease
    #
    # Return: {
    #   'volunteer_probability': p,
    #   'provision_probability': 1 - (1-p)^n,
    #   'expected_payoff': ...
    # }
    pass


def commons_tragedy(num_players: int, carrying_capacity: float,
                   value_per_unit: float, cost_per_unit: float = 0) -> Dict:
    """
    Analyze tragedy of the commons.

    Each player chooses how many units to extract from common resource.
    Total extraction beyond carrying capacity degrades the resource.

    Payoff: value * extraction * resource_quality(total_extraction) - cost * extraction

    Args:
        num_players: Number of players
        carrying_capacity: Sustainable extraction level
        value_per_unit: Value per unit extracted
        cost_per_unit: Cost per unit extracted

    Returns:
        Comparison of Nash equilibrium and social optimum
    """
    # TODO: Analyze tragedy of the commons
    #
    # Resource quality degrades with overuse:
    # quality(x) = 1 if x <= K (carrying capacity), else K/x
    #
    # Nash equilibrium: Each player maximizes own payoff
    # → Over-extraction beyond carrying capacity
    #
    # Social optimum: Maximize total surplus
    # → Limit extraction to carrying capacity
    #
    # Classic market failure: open access leads to over-exploitation
    #
    # Solutions: property rights, quotas, taxes
    #
    # Return: {
    #   'nash_extraction_per_player': ...,
    #   'optimal_extraction_per_player': ...,
    #   'nash_total_payoff': ...,
    #   'optimal_total_payoff': ...,
    #   'efficiency_ratio': ...
    # }
    pass


def groves_clarke_mechanism(num_players: int, values_for_project: List[float],
                            project_cost: float) -> Dict:
    """
    Implement Groves-Clarke (pivotal) mechanism for public project.

    Decide whether to build public project based on reported valuations.
    Use VCG payments to induce truthful reporting.

    Args:
        num_players: Number of players
        values_for_project: True values (positive or negative)
        project_cost: Cost of the project

    Returns:
        Decision and payments
    """
    # TODO: Implement Groves-Clarke mechanism
    #
    # Decision rule:
    # Build project if sum(values) >= cost
    #
    # Payment for player i (if pivotal):
    # If i's report changes decision, i pays externality on others
    # payment_i = |sum(values_{-i}) - cost| if i is pivotal, else 0
    #
    # This is strategyproof: truth-telling is dominant strategy
    #
    # But budget may not balance (can collect surplus or deficit)
    #
    # Return: {
    #   'build_project': True/False,
    #   'payments': [...],
    #   'surplus': ...,
    #   'total_welfare': ...
    # }
    pass


# Test functions
def test_linear_public_good():
    """Test linear public goods game."""
    result = analyze_linear_public_good(
        num_players=4,
        endowment=20,
        marginal_per_capita_return=0.4
    )

    assert result is not None

    # MPCR = 0.4 < 1: dominant strategy is contribute 0
    # But MPCR * n = 1.6 > 1: socially optimal to contribute fully
    eq_contrib = result['equilibrium_contribution']
    opt_contrib = result['optimal_contribution']

    assert eq_contrib == 0, "Equilibrium should be free-riding"
    assert opt_contrib == 20, "Optimal is full contribution"

    print(f"✓ Linear public good:")
    print(f"  Equilibrium: {eq_contrib}, Optimal: {opt_contrib}")


def test_threshold_public_good():
    """Test threshold public goods."""
    result = threshold_public_good(
        valuations=[30, 25, 20, 15, 10],
        cost=60,
        threshold=60
    )

    assert result is not None

    # Sum of values = 100 > cost = 60, so provision is efficient
    # Multiple equilibria exist

    print(f"✓ Threshold public good:")
    print(f"  Will provide: {result['will_provide']}")


def test_volunteer_dilemma():
    """Test volunteer's dilemma."""
    result = volunteer_dilemma(
        num_players=5,
        cost_of_volunteering=10,
        benefit_if_provided=30
    )

    assert result is not None

    prob_volunteer = result['volunteer_probability']
    prob_provision = result['provision_probability']

    # Each player should volunteer with some probability
    assert 0 < prob_volunteer < 1

    print(f"✓ Volunteer's dilemma:")
    print(f"  P(volunteer) = {prob_volunteer:.3f}")
    print(f"  P(provision) = {prob_provision:.3f}")


def test_commons_tragedy():
    """Test tragedy of the commons."""
    result = commons_tragedy(
        num_players=10,
        carrying_capacity=100,
        value_per_unit=10,
        cost_per_unit=2
    )

    assert result is not None

    nash_extraction = result['nash_extraction_per_player']
    optimal_extraction = result['optimal_extraction_per_player']

    # Nash should over-extract compared to optimum
    assert nash_extraction * 10 > 100, "Should over-extract in Nash equilibrium"
    assert optimal_extraction * 10 <= 100, "Optimal respects capacity"

    print(f"✓ Tragedy of commons:")
    print(f"  Nash: {nash_extraction:.1f}/player, Optimal: {optimal_extraction:.1f}/player")


def test_groves_clarke():
    """Test Groves-Clarke mechanism."""
    result = groves_clarke_mechanism(
        num_players=3,
        values_for_project=[40, 30, -20],  # Net benefit = 50
        project_cost=30
    )

    assert result is not None

    # Sum of values (50) > cost (30), so build
    assert result['build_project'] == True

    # Check that mechanism is feasible
    total_payment = sum(result['payments'])

    print(f"✓ Groves-Clarke mechanism:")
    print(f"  Build: {result['build_project']}")
    print(f"  Payments: {result['payments']}")


if __name__ == "__main__":
    print("\n=== Public Goods Games Tests ===\n")
    test_linear_public_good()
    test_threshold_public_good()
    test_volunteer_dilemma()
    test_commons_tragedy()
    test_groves_clarke()
    print("\n🎉 All tests passed! You understand public goods games!")

    print("\n=== Key Insights ===")
    print("• Public goods: non-rival, non-excludable → free-rider problem")
    print("• Linear public good: dominant strategy is free-ride if MPCR < 1")
    print("• Threshold goods: multiple equilibria, coordination problem")
    print("• Volunteer's dilemma: mixed strategy equilibrium, diffusion of responsibility")
    print("• Tragedy of commons: open access leads to over-exploitation")
    print("• Groves-Clarke: VCG mechanism for public projects (strategyproof)")
