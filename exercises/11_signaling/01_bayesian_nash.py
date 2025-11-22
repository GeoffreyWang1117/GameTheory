"""
Exercise: Bayesian Nash Equilibrium
====================================

In Bayesian games, players have incomplete information about other players' characteristics.
Each player has a "type" drawn from a probability distribution, and players choose strategies
based on their beliefs about others' types.

A Bayesian Nash Equilibrium (BNE) is a strategy profile where each player's strategy is
optimal given their type and their beliefs about other players' types.

Learning Objectives:
- Understand incomplete information games
- Calculate expected payoffs with uncertainty
- Find Bayesian Nash Equilibria
- Apply to auction and market entry scenarios

Key Concepts:
- Types and type spaces
- Beliefs and priors
- Bayesian Nash Equilibrium
- Ex-ante vs ex-post payoffs
"""

from typing import Dict, Tuple, Callable
import numpy as np


def calculate_expected_payoff(strategy, type_val, beliefs, payoff_func):
    """
    Calculate expected payoff for a player given their strategy and beliefs.

    Args:
        strategy: Player's chosen action
        type_val: Player's type
        beliefs: Dictionary mapping opponent types to probabilities
        payoff_func: Function(my_action, my_type, opponent_action, opponent_type) -> payoff

    Returns:
        Expected payoff as a float
    """
    # TODO: Calculate the expected payoff by averaging over opponent types weighted by beliefs
    # Hint: For each possible opponent type and action, compute payoff and weight by probability
    pass


def find_bayesian_nash_equilibrium(types1, types2, priors1, priors2, payoff_func1, payoff_func2, actions):
    """
    Find a Bayesian Nash Equilibrium in a two-player game.

    Args:
        types1, types2: Lists of possible types for each player
        priors1, priors2: Dictionaries mapping types to probabilities
        payoff_func1, payoff_func2: Payoff functions for each player
        actions: List of possible actions

    Returns:
        Dictionary mapping (player, type) to best action
    """
    # TODO: For each type of each player, find the best response given beliefs
    # A BNE requires that each type's strategy is a best response
    # Hint: Use calculate_expected_payoff to compare different actions
    pass


def market_entry_game(cost_high: float, cost_low: float, prob_low: float, monopoly_profit: float, duopoly_profit: float):
    """
    Analyze a market entry game with incomplete information.

    Two firms decide whether to enter a market. Firm 1 knows its cost (high or low).
    Firm 2 only knows the probability that Firm 1 has low cost.

    Payoffs:
    - If only one firm enters: monopoly_profit - cost
    - If both enter: duopoly_profit - cost
    - If neither enters: 0

    Args:
        cost_high: High cost level
        cost_low: Low cost level
        prob_low: Probability that Firm 1 has low cost
        monopoly_profit: Profit when alone in market
        duopoly_profit: Profit when competing

    Returns:
        Dictionary with equilibrium strategies for each type
    """
    # TODO: Find the Bayesian Nash Equilibrium of this entry game
    # Firm 1's strategy depends on its type (high or low cost)
    # Firm 2's strategy depends on expected payoff given beliefs about Firm 1
    # Return format: {'firm1_low': 'Enter'/'Stay Out', 'firm1_high': ..., 'firm2': ...}
    pass


def first_price_auction_bid(valuation: float, num_bidders: int, value_distribution: str = 'uniform'):
    """
    Calculate optimal bid in a first-price sealed-bid auction with incomplete information.

    In a first-price auction, bidders submit sealed bids and the highest bidder wins,
    paying their bid. With private values and symmetric bidders, there's a BNE in
    bidding strategies.

    For uniform distribution on [0, V], the symmetric BNE is:
    b(v) = (n-1)/n * v

    Args:
        valuation: Bidder's private valuation
        num_bidders: Total number of bidders
        value_distribution: 'uniform' or 'exponential'

    Returns:
        Optimal bid amount
    """
    # TODO: Calculate the optimal bid given the valuation and number of bidders
    # For uniform distribution: use the formula b(v) = (n-1)/n * v
    # This is the unique symmetric Bayesian Nash Equilibrium
    pass


# Test functions
def test_expected_payoff():
    """Test expected payoff calculation."""
    def simple_payoff(my_action, my_type, opp_action, opp_type):
        if my_action == 'A' and opp_action == 'A':
            return my_type + opp_type
        return my_type

    beliefs = {'type1': 0.6, 'type2': 0.4}
    # Assume opponent plays 'A' always
    result = calculate_expected_payoff('A', 5, beliefs,
                                       lambda ma, mt, oa, ot: simple_payoff(ma, mt, 'A', ot))

    # With opponent types 1 and 2 with probs 0.6 and 0.4:
    # E[payoff] = 0.6 * (5 + 1) + 0.4 * (5 + 2) = 0.6 * 6 + 0.4 * 7 = 3.6 + 2.8 = 6.4
    # (assuming opponent type values are 1 and 2)
    assert result is not None, "Expected payoff calculation failed"
    print("✓ Expected payoff calculation works")


def test_market_entry():
    """Test market entry game."""
    result = market_entry_game(
        cost_high=60,
        cost_low=20,
        prob_low=0.5,
        monopoly_profit=100,
        duopoly_profit=50
    )

    assert result is not None, "Market entry analysis failed"
    assert 'firm1_low' in result and 'firm1_high' in result and 'firm2' in result

    # Low-cost firm should enter (100-20=80 > 50-20=30 even if both enter)
    # High-cost firm should stay out if duopoly (50-60=-10)
    # Firm 2 should consider expected competition
    print(f"✓ Market entry equilibrium: {result}")


def test_first_price_auction():
    """Test first-price auction bidding."""
    # With 3 bidders and valuation 90, optimal bid = 2/3 * 90 = 60
    bid = first_price_auction_bid(90, 3, 'uniform')
    assert bid is not None, "Auction bid calculation failed"
    expected_bid = (3 - 1) / 3 * 90
    assert abs(bid - expected_bid) < 0.01, f"Expected bid {expected_bid}, got {bid}"
    print(f"✓ First-price auction bid: {bid} (valuation=90, n=3)")


def test_bayesian_nash():
    """Test BNE finding."""
    # Simple 2x2 game with two types each
    types1 = ['Strong', 'Weak']
    types2 = ['Strong', 'Weak']
    priors1 = {'Strong': 0.5, 'Weak': 0.5}
    priors2 = {'Strong': 0.5, 'Weak': 0.5}
    actions = ['Fight', 'Concede']

    def payoff1(a1, t1, a2, t2):
        if a1 == 'Fight' and a2 == 'Concede':
            return 10
        if a1 == 'Concede' and a2 == 'Fight':
            return 0
        if a1 == 'Fight' and a2 == 'Fight':
            return 5 if t1 == 'Strong' else -5
        return 5

    def payoff2(a2, t2, a1, t1):
        return payoff1(a2, t2, a1, t1)

    result = find_bayesian_nash_equilibrium(types1, types2, priors1, priors2,
                                           payoff1, payoff2, actions)

    assert result is not None, "BNE finding failed"
    print(f"✓ Bayesian Nash Equilibrium found: {result}")


if __name__ == "__main__":
    print("\n=== Bayesian Nash Equilibrium Tests ===\n")
    test_expected_payoff()
    test_first_price_auction()
    test_market_entry()
    test_bayesian_nash()
    print("\n🎉 All tests passed! You understand Bayesian games!")

    print("\n=== Key Insights ===")
    print("• In Bayesian games, players optimize given their beliefs about others' types")
    print("• First-price auction BNE: bid below your value to account for winner's curse")
    print("• Market entry depends on cost types and beliefs about competitors")
    print("• BNE requires each type's strategy to be a best response to others' strategies")
