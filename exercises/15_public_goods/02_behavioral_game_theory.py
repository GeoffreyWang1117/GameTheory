"""
Exercise: Behavioral Game Theory
=================================

Behavioral game theory incorporates psychological insights and experimental
findings into game theory models. People don't always play Nash equilibria!

Learning Objectives:
- Understand deviations from Nash predictions
- Model fairness and reciprocity
- Analyze social preferences
- Apply to Ultimatum and Dictator games

Key Concepts:
- Bounded rationality
- Fairness and inequity aversion
- Reciprocity (positive and negative)
- Social preferences (altruism, spite)
- Level-k thinking
"""

from typing import Dict, List, Tuple, Callable
import numpy as np


def ultimatum_game_standard(pie_size: float, proposer_offer: float) -> Dict:
    """
    Analyze standard Ultimatum Game with self-interested players.

    Proposer offers split of pie. Responder accepts or rejects.
    If accepted: proposer gets (pie - offer), responder gets offer.
    If rejected: both get 0.

    Standard prediction (SPNE): proposer offers minimum, responder accepts.
    Reality: offers typically 40-50%, low offers often rejected!

    Args:
        pie_size: Total amount to divide
        proposer_offer: Amount offered to responder

    Returns:
        Analysis of offer
    """
    # TODO: Analyze ultimatum game
    #
    # Subgame perfect Nash equilibrium (assuming self-interest):
    # - Responder accepts any offer > 0 (backward induction)
    # - Proposer offers minimum (e.g., $0.01)
    #
    # Experimental findings:
    # - Modal offer: 40-50% of pie
    # - Offers below 20-30% often rejected
    # - Varies across cultures
    #
    # Explanation: fairness concerns, negative reciprocity
    #
    # Return: {
    #   'spne_prediction': {'offer': 0.01, 'accept': True},
    #   'typical_behavior': {'offer_range': (0.4*pie, 0.5*pie), 'rejection_threshold': 0.2*pie},
    #   'offer_fairness': offer / pie_size
    # }
    pass


def inequity_aversion_model(alpha: float, beta: float,
                            allocation_self: float,
                            allocation_other: float) -> float:
    """
    Calculate utility under Fehr-Schmidt inequity aversion model.

    Utility = own_payoff - alpha * max(other - own, 0) - beta * max(own - other, 0)

    where:
    - alpha: disutility from disadvantageous inequity (typically alpha > beta)
    - beta: disutility from advantageous inequity

    Args:
        alpha: Disadvantageous inequity aversion parameter
        beta: Advantageous inequity aversion parameter
        allocation_self: Own payoff
        allocation_other: Other player's payoff

    Returns:
        Utility accounting for inequity aversion
    """
    # TODO: Calculate Fehr-Schmidt utility
    #
    # Three cases:
    # 1. allocation_self > allocation_other: suffer from guilt (beta)
    # 2. allocation_self < allocation_other: suffer from envy (alpha)
    # 3. allocation_self = allocation_other: no inequity, utility = payoff
    #
    # Typically: alpha > beta (envy stronger than guilt)
    #            beta < 1 (still prefer more money)
    #
    # Return utility value
    pass


def predict_ultimatum_with_fairness(pie_size: float, alpha_r: float, beta_p: float) -> Dict:
    """
    Predict ultimatum game outcome with inequity-averse players.

    Proposer has advantageous inequity aversion beta_p.
    Responder has disadvantageous inequity aversion alpha_r.

    Args:
        pie_size: Total pie
        alpha_r: Responder's envy parameter
        beta_p: Proposer's guilt parameter

    Returns:
        Predicted offer and acceptance
    """
    # TODO: Solve ultimatum game with inequity aversion
    #
    # Responder accepts offer x if:
    # x - alpha_r * max((pie-x) - x, 0) >= 0
    # If x < pie/2: x - alpha_r*(pie - 2x) >= 0
    # x * (1 + 2*alpha_r) >= alpha_r * pie
    # x >= alpha_r / (1 + 2*alpha_r) * pie
    #
    # Minimum acceptable offer: x_min = alpha_r / (1 + 2*alpha_r) * pie
    #
    # Proposer chooses x to maximize:
    # (pie - x) - beta_p * max((pie-x) - x, 0)
    #
    # If proposer offers x < pie/2:
    # Utility = (pie-x) - beta_p*(pie - 2x) = pie*(1-beta_p) + x*(2*beta_p - 1)
    # If beta_p > 1/2: prefers equal split
    # If beta_p < 1/2: offers minimum acceptable x_min
    #
    # Return: {
    #   'predicted_offer': x*,
    #   'minimum_acceptable': x_min,
    #   'will_accept': True
    # }
    pass


def dictator_game(pie_size: float, beta: float) -> float:
    """
    Predict dictator game allocation with inequity aversion.

    Dictator unilaterally decides allocation (no acceptance decision).

    Standard prediction: keep everything.
    Reality: often give 20-30%.

    Args:
        pie_size: Total amount
        beta: Dictator's advantageous inequity aversion

    Returns:
        Amount given to recipient
    """
    # TODO: Solve dictator game with inequity aversion
    #
    # Dictator chooses x to give, keeping (pie - x), maximizing:
    # (pie - x) - beta * max((pie-x) - x, 0)
    #
    # If x < pie/2:
    # Utility = (pie-x) - beta*(pie - 2x) = pie*(1-beta) + x*(2*beta - 1)
    #
    # If beta > 1/2: maximized at x = pie/2 (equal split)
    # If beta < 1/2: maximized at x = 0 (keep all)
    # If beta = 1/2: indifferent
    #
    # Experimental: beta often around 0.2-0.4
    # → Dictators give some but less than 50%
    #
    # Return amount given
    pass


def reciprocity_trust_game(amount_sent: float, multiplier: float,
                           trustee_beta: float, trustee_reciprocity: float) -> Dict:
    """
    Analyze trust (investment) game with reciprocity.

    Investor sends amount to Trustee. Amount is multiplied.
    Trustee decides how much to return.

    Standard: Trustee keeps all, so Investor sends 0.
    Reality: Investors send positive amounts, Trustees often reciprocate.

    Args:
        amount_sent: Amount investor sends
        multiplier: Amount is multiplied by this
        trustee_beta: Trustee's inequity aversion
        trustee_reciprocity: Trustee's reciprocity parameter

    Returns:
        Amount returned by trustee
    """
    # TODO: Model trust game with reciprocity
    #
    # After investor sends x:
    # - Investor has: initial_endowment - x
    # - Trustee has: initial_endowment + multiplier * x
    #
    # Trustee chooses amount y to return, maximizing:
    # Utility = (multiplier*x - y) - beta*(advantageous inequity)
    #           + reciprocity * kindness_of_investor
    #
    # Reciprocity: return more if investor sent more (positive reciprocity)
    #
    # With pure inequity aversion: return to equalize payoffs
    # With reciprocity: return more than pure inequality aversion predicts
    #
    # Return: {
    #   'amount_returned': y,
    #   'trustee_keeps': multiplier*x - y,
    #   'return_ratio': y / (multiplier*x)
    # }
    pass


def level_k_thinking(payoff_matrix: np.ndarray, k: int) -> np.ndarray:
    """
    Predict behavior using level-k cognitive hierarchy model.

    Level-0: Play randomly (uniform)
    Level-1: Best respond to level-0
    Level-2: Best respond to level-1
    ...
    Level-k: Best respond to level-(k-1)

    Args:
        payoff_matrix: Payoff matrix for player
        k: Thinking level

    Returns:
        Strategy distribution for level-k player
    """
    # TODO: Implement level-k reasoning
    #
    # Base case (level-0): uniform random
    # Recursive case (level-k): best response to level-(k-1)
    #
    # In games like beauty contest, higher k → closer to Nash
    # But finite k explains departure from Nash
    #
    # Population often has mix of levels:
    # - Level-1 most common
    # - Few beyond level-3
    #
    # Return strategy distribution
    pass


# Test functions
def test_ultimatum_standard():
    """Test standard ultimatum game."""
    result = ultimatum_game_standard(pie_size=100, proposer_offer=30)

    assert result is not None

    spne_offer = result['spne_prediction']['offer']
    typical_range = result['typical_behavior']['offer_range']

    # SPNE predicts tiny offer, reality is 40-50%
    assert spne_offer < 1, "SPNE should be near-zero offer"
    assert typical_range[0] >= 40, "Typical offers are 40-50%"

    print(f"✓ Ultimatum game:")
    print(f"  SPNE offer: ${spne_offer:.2f}")
    print(f"  Typical offers: ${typical_range[0]}-${typical_range[1]}")


def test_inequity_aversion():
    """Test inequity aversion model."""
    # Envy: other earns more
    utility_envy = inequity_aversion_model(
        alpha=0.6, beta=0.3,
        allocation_self=30,
        allocation_other=70
    )

    # Guilt: I earn more
    utility_guilt = inequity_aversion_model(
        alpha=0.6, beta=0.3,
        allocation_self=70,
        allocation_other=30
    )

    # Equal
    utility_equal = inequity_aversion_model(
        alpha=0.6, beta=0.3,
        allocation_self=50,
        allocation_other=50
    )

    assert utility_envy < utility_equal, "Envy reduces utility"
    assert utility_guilt < utility_equal, "Guilt reduces utility"
    assert utility_envy < utility_guilt, "Envy hurts more (alpha > beta)"

    print(f"✓ Inequity aversion utilities:")
    print(f"  Equal split: {utility_equal:.1f}")
    print(f"  Disadvantaged: {utility_envy:.1f}")
    print(f"  Advantaged: {utility_guilt:.1f}")


def test_ultimatum_with_fairness():
    """Test ultimatum with fairness preferences."""
    result = predict_ultimatum_with_fairness(
        pie_size=100,
        alpha_r=0.5,  # Responder's envy
        beta_p=0.4    # Proposer's guilt
    )

    assert result is not None

    offer = result['predicted_offer']
    min_accept = result['minimum_acceptable']

    # With fairness, offer should be higher than SPNE
    assert offer >= min_accept
    assert offer > 5  # Higher than SPNE near-zero

    print(f"✓ Ultimatum with fairness:")
    print(f"  Predicted offer: ${offer:.2f}")
    print(f"  Minimum acceptable: ${min_accept:.2f}")


def test_dictator_game():
    """Test dictator game."""
    # Selfish dictator
    give_selfish = dictator_game(pie_size=100, beta=0.0)

    # Fair dictator
    give_fair = dictator_game(pie_size=100, beta=0.6)

    assert give_selfish == 0, "Selfish dictator keeps all"
    assert give_fair == 50, "Fair dictator splits equally"

    print(f"✓ Dictator game:")
    print(f"  Selfish (β=0): gives ${give_selfish}")
    print(f"  Fair (β=0.6): gives ${give_fair}")


def test_trust_game():
    """Test trust game with reciprocity."""
    result = reciprocity_trust_game(
        amount_sent=50,
        multiplier=3,
        trustee_beta=0.3,
        trustee_reciprocity=0.5
    )

    assert result is not None

    returned = result['amount_returned']
    ratio = result['return_ratio']

    # With reciprocity, should return substantial amount
    assert returned > 0, "Trustee should return some amount"
    assert ratio > 0, "Return ratio should be positive"

    print(f"✓ Trust game:")
    print(f"  Amount returned: ${returned:.2f} ({ratio:.1%} of ${50*3})")


if __name__ == "__main__":
    print("\n=== Behavioral Game Theory Tests ===\n")
    test_ultimatum_standard()
    test_inequity_aversion()
    test_ultimatum_with_fairness()
    test_dictator_game()
    test_trust_game()
    print("\n🎉 All tests passed! You understand behavioral game theory!")

    print("\n=== Key Insights ===")
    print("• People deviate systematically from Nash predictions")
    print("• Fairness matters: inequity aversion explains many behaviors")
    print("• Ultimatum game: offers typically 40-50%, low offers rejected")
    print("• Dictator game: many give 20-30% despite no strategic reason")
    print("• Reciprocity: people reward kindness and punish unkindness")
    print("• Level-k thinking: bounded rationality in strategic reasoning")
    print("• Behavioral models improve predictions in many contexts")
