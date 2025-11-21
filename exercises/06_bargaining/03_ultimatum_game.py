"""
Exercise 22: Ultimatum Game and Behavioral Game Theory

The Ultimatum Game is deceptively simple:
- Player 1 (Proposer) offers a split of money (e.g., $10)
- Player 2 (Responder) accepts or rejects
- If accepted: split as proposed. If rejected: both get $0.

Standard game theory predicts: Proposer offers minimum ($0.01), Responder accepts.
Reality: People reject unfair offers! This reveals preferences for fairness.

TODO: Analyze the Ultimatum Game and behavioral deviations.
"""


def ultimatum_game_subgame_perfect():
    """
    Find the subgame perfect equilibrium of the Ultimatum Game.

    By backward induction:
    - Responder accepts any offer > 0 (better than $0)
    - Proposer offers minimum positive amount

    Returns:
        Tuple (proposer_offer, responder_gets, prediction)

    TODO: Calculate SPNE.
    """
    # TODO: Implement SPNE calculation
    # Standard game theory: offer ε ≈ 0, responder accepts

    total = 10
    epsilon = 0.01  # Minimum positive amount

    proposer_offer = total - epsilon
    responder_gets = epsilon

    prediction = {
        'proposer_gets': proposer_offer,
        'responder_gets': responder_gets,
        'responder_action': 'accept',
        'reasoning': 'Backward induction: responder accepts any positive offer'
    }

    return proposer_offer, responder_gets, prediction


def fairness_preference_model(offer, total, fairness_weight_alpha):
    """
    Model responder utility with fairness preferences.

    Utility = money_received - α * |money_received - fair_share|

    Where fair_share = total/2, and α measures aversion to unfairness.

    Args:
        offer: Amount offered to responder
        total: Total pie size
        fairness_weight_alpha: Weight on fairness (α)

    Returns:
        Utility of accepting the offer

    TODO: Calculate utility with fairness preferences.
    """
    fair_share = total / 2

    # TODO: Calculate utility
    # U(accept) = offer - α * |offer - fair_share|
    # U(reject) = 0 (but maintains fairness norm)

    utility_accept = offer - fairness_weight_alpha * abs(offer - fair_share)

    # Utility of rejecting (punishment for unfairness)
    utility_reject = 0

    return utility_accept, utility_reject


def minimum_acceptable_offer(total, alpha):
    """
    Find the minimum offer a fairness-minded responder would accept.

    Responder accepts if: offer - α|offer - total/2| >= 0

    Args:
        total: Total pie size
        alpha: Fairness weight

    Returns:
        Minimum acceptable offer

    TODO: Solve for minimum acceptable offer.
    """
    fair_share = total / 2

    # TODO: Solve for minimum offer where utility >= 0
    # For offer < fair_share: offer - α(fair_share - offer) >= 0
    # offer(1 + α) >= α * fair_share
    # offer >= α * fair_share / (1 + α)

    min_offer = alpha * fair_share / (1 + alpha)

    return min_offer


def optimal_proposal_with_fairness(total, alpha, rejection_prob_function):
    """
    Find optimal proposal accounting for fairness and rejection risk.

    Proposer maximizes: (total - offer) * Pr(accept | offer)

    Args:
        total: Total amount
        alpha: Responder's fairness parameter
        rejection_prob_function: Function mapping offer -> rejection probability

    Returns:
        Optimal offer

    TODO: Find optimal offer balancing greed and acceptance.
    """
    best_offer = None
    best_expected = -float('inf')

    # TODO: Search for optimal offer
    for offer in range(0, int(total * 100) + 1):
        offer_amount = offer / 100.0

        accept_prob = 1 - rejection_prob_function(offer_amount, total, alpha)
        expected_payoff = (total - offer_amount) * accept_prob

        if expected_payoff > best_expected:
            best_expected = expected_payoff
            best_offer = offer_amount

    return best_offer


def simple_rejection_prob(offer, total, alpha):
    """
    Simple rejection probability based on fairness.

    If offer < minimum acceptable, high rejection prob.
    Otherwise, low rejection prob.

    TODO: Implement rejection probability function.
    """
    min_acceptable = minimum_acceptable_offer(total, alpha)

    if offer < min_acceptable:
        # Higher rejection for more unfair offers
        unfairness = (min_acceptable - offer) / total
        rejection_prob = min(0.9, unfairness * 2)
    else:
        rejection_prob = 0.1  # Small prob of rejection even for fair offers

    return rejection_prob


def experimental_evidence_summary():
    """
    Summarize experimental findings from Ultimatum Game studies.

    Returns:
        Dictionary with experimental evidence

    TODO: Compile experimental findings.
    """
    evidence = {
        'modal_offer': 0.5,  # Most common offer is 50-50 split
        'mean_offer': 0.4,   # Average offer is 40% of total
        'rejection_rate': {
            'offer_20_percent': 0.4,  # ~40% reject offers of 20%
            'offer_30_percent': 0.2,  # ~20% reject offers of 30%
            'offer_40_percent': 0.05, # ~5% reject offers of 40%
        },
        'cultural_variation': True,
        'findings': [
            'People make substantially positive offers',
            'Low offers are frequently rejected',
            'Modal offer is 50-50 split',
            'Rejection rates decrease with offer size',
            'Behavior varies across cultures',
            'Experience reduces but doesn\'t eliminate fairness behavior'
        ]
    }

    return evidence


def test_solution():
    """Test function - Do not modify."""
    # Test SPNE
    offer, responder_gets, prediction = ultimatum_game_subgame_perfect()

    print("Subgame Perfect Equilibrium:")
    print(f"  Proposer offers: ${responder_gets:.2f}")
    print(f"  Proposer keeps: ${offer:.2f}")
    print(f"  Prediction: {prediction['responder_action']}")

    assert responder_gets < 1, "SPNE prediction: offer almost nothing"

    # Test fairness model
    total = 10
    alpha = 0.5

    # Fair offer
    u_accept_fair, u_reject_fair = fairness_preference_model(5, total, alpha)
    print(f"\nFairness model (α={alpha}):")
    print(f"  Utility of accepting fair offer (5): {u_accept_fair:.2f}")

    # Unfair offer
    u_accept_unfair, u_reject_unfair = fairness_preference_model(2, total, alpha)
    print(f"  Utility of accepting unfair offer (2): {u_accept_unfair:.2f}")

    assert u_accept_fair > u_accept_unfair, "Fair offers should give higher utility"

    # Test minimum acceptable offer
    min_offer = minimum_acceptable_offer(total, alpha)
    print(f"  Minimum acceptable offer: ${min_offer:.2f}")

    assert min_offer > 0.01, "With fairness, minimum offer should be substantial"
    assert min_offer < 5, "Minimum should be less than fair share"

    # Test optimal proposal
    optimal = optimal_proposal_with_fairness(total, alpha, simple_rejection_prob)
    print(f"\nOptimal proposal with fairness concerns: ${optimal:.2f}")

    assert optimal > min_offer, "Optimal offer should exceed minimum acceptable"
    assert optimal < total, "Can't offer more than total"

    # Show experimental evidence
    evidence = experimental_evidence_summary()
    print(f"\nExperimental Evidence:")
    print(f"  Modal offer: {evidence['modal_offer']*100:.0f}%")
    print(f"  Mean offer: {evidence['mean_offer']*100:.0f}%")
    print(f"  Rejection rate for 20% offer: {evidence['rejection_rate']['offer_20_percent']*100:.0f}%")

    print("\nKey insights:")
    print("1. Standard game theory predicts extreme selfishness")
    print("2. Actual behavior shows strong fairness preferences")
    print("3. People reject unfair offers even at personal cost")
    print("4. Ultimatum game reveals limits of pure self-interest assumption")
    print("5. Behavioral game theory incorporates social preferences")

    return True


if __name__ == '__main__':
    test_solution()
