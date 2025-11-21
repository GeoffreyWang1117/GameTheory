"""
Exercise 21: Rubinstein Alternating Offers Bargaining

In Rubinstein's model, two players alternate making offers to divide a pie.
If an offer is rejected, the game continues with roles reversed, but the pie
shrinks due to discounting (impatience).

Key insight: Even with infinite rounds, there's a unique subgame perfect equilibrium!
The equilibrium offer is accepted immediately.

TODO: Implement Rubinstein bargaining model.
"""


def rubinstein_equilibrium(delta1, delta2, pie_size=1.0):
    """
    Calculate the Rubinstein bargaining equilibrium.

    With discount factors δ1 and δ2, the equilibrium has player 1 offer:
    x* = (1 - δ2) / (1 - δ1*δ2)

    And player 2 accepts. Player 1 gets x*, player 2 gets (1 - x*).

    Args:
        delta1: Player 1's discount factor (0 < δ < 1)
        delta2: Player 2's discount factor
        pie_size: Total size of pie to divide

    Returns:
        Tuple (equilibrium_offer, player1_payoff, player2_payoff)

    TODO: Calculate Rubinstein equilibrium.
    """
    # TODO: Calculate equilibrium offer
    # x* = (1 - δ2) / (1 - δ1*δ2)

    x_star = (1 - delta2) / (1 - delta1 * delta2)

    # Scale by pie size
    offer = x_star * pie_size

    player1_payoff = offer
    player2_payoff = pie_size - offer

    return offer, player1_payoff, player2_payoff


def simulate_bargaining_game(delta1, delta2, pie_size=1.0, max_rounds=10):
    """
    Simulate the bargaining game for a limited number of rounds.

    Args:
        delta1, delta2: Discount factors
        pie_size: Initial pie size
        max_rounds: Maximum number of offers

    Returns:
        List of (round, proposer, offer_to_p1, pie_size) tuples

    TODO: Simulate backward induction for finite game.
    """
    # Work backwards from last round
    history = []

    # TODO: Implement backward induction
    # In last round, proposer offers nothing to other player
    # Work backwards using indifference conditions

    # For finite game, use backward induction
    current_pie = pie_size

    # Start from the end
    # If it's the last round, proposer keeps everything
    # One round before: responder indifferent between accepting and waiting
    # Continue backwards...

    # Simplified: simulate forward with equilibrium strategies
    current_pie = pie_size
    proposer = 1

    for round_num in range(max_rounds):
        if proposer == 1:
            # Player 1 offers what makes player 2 indifferent
            # Player 2 compares: accept x2 now vs wait and propose next round
            # If wait: next round pie is δ2 * current_pie, and P2 can get share
            offer_to_p2 = delta2 * (1 - rubinstein_equilibrium(delta1, delta2)[1] / current_pie) * current_pie
            offer_to_p1 = current_pie - offer_to_p2

            history.append((round_num, 1, offer_to_p1, current_pie))

            # In equilibrium, offer is accepted
            break
        else:
            offer_to_p1 = delta1 * rubinstein_equilibrium(delta1, delta2)[0]
            offer_to_p2 = current_pie - offer_to_p1

            history.append((round_num, 2, offer_to_p1, current_pie))
            break

    return history


def first_mover_advantage(delta):
    """
    Calculate first-mover advantage when both players have same discount factor.

    With symmetric discount factors, player 1 gets:
    (1 - δ) / (1 - δ²) = 1 / (1 + δ)

    Args:
        delta: Common discount factor

    Returns:
        Share of the pie that first mover gets

    TODO: Calculate first-mover share.
    """
    # TODO: Calculate equilibrium share for first mover
    # With δ1 = δ2 = δ: x* = (1-δ)/(1-δ²) = 1/(1+δ)

    share = 1 / (1 + delta)

    return share


def patience_advantage(delta_patient, delta_impatient):
    """
    Show how patience affects bargaining power.

    More patient players (higher δ) get more of the pie.

    Args:
        delta_patient: Discount factor of patient player
        delta_impatient: Discount factor of impatient player

    Returns:
        Analysis of how patience affects outcomes

    TODO: Analyze patience effect.
    """
    # Case 1: Patient player goes first
    offer1, p1_payoff, p2_payoff = rubinstein_equilibrium(delta_patient, delta_impatient)

    # Case 2: Impatient player goes first
    offer2, p2_first, p1_second = rubinstein_equilibrium(delta_impatient, delta_patient)

    analysis = {
        'patient_proposes': {
            'patient_gets': p1_payoff,
            'impatient_gets': p2_payoff
        },
        'impatient_proposes': {
            'patient_gets': p1_second,
            'impatient_gets': p2_first
        }
    }

    return analysis


def test_solution():
    """Test function - Do not modify."""
    # Test symmetric case (both have same discount factor)
    delta = 0.9

    offer, p1, p2 = rubinstein_equilibrium(delta, delta)

    print(f"Symmetric case (δ={delta}):")
    print(f"  Player 1 offers: {offer:.3f}")
    print(f"  Player 1 gets: {p1:.3f}")
    print(f"  Player 2 gets: {p2:.3f}")

    # Check first-mover advantage
    expected_share = 1 / (1 + delta)
    assert abs(p1 - expected_share) < 0.01, f"Expected {expected_share:.3f}, got {p1:.3f}"

    # Test asymmetric case
    patient = 0.95
    impatient = 0.5

    offer_asym, p1_asym, p2_asym = rubinstein_equilibrium(patient, impatient)

    print(f"\nAsymmetric case (δ1={patient}, δ2={impatient}):")
    print(f"  Patient player 1 gets: {p1_asym:.3f}")
    print(f"  Impatient player 2 gets: {p2_asym:.3f}")

    # Patient player should get more
    assert p1_asym > 0.5, "Patient player should get more than half"

    # Test patience advantage
    patience_analysis = patience_advantage(0.9, 0.5)
    print(f"\nPatience advantage analysis:")
    print(f"  When patient proposes: patient gets {patience_analysis['patient_proposes']['patient_gets']:.3f}")
    print(f"  When impatient proposes: patient gets {patience_analysis['impatient_proposes']['patient_gets']:.3f}")

    # Patient player should always get more regardless of who proposes
    assert patience_analysis['patient_proposes']['patient_gets'] > 0.5
    assert patience_analysis['impatient_proposes']['patient_gets'] > 0.5

    # Test first-mover advantage
    fma_50 = first_mover_advantage(0.5)
    fma_90 = first_mover_advantage(0.9)

    print(f"\nFirst-mover advantage:")
    print(f"  With δ=0.5: first mover gets {fma_50:.3f}")
    print(f"  With δ=0.9: first mover gets {fma_90:.3f}")

    # First-mover advantage decreases as players become more patient
    assert fma_50 > fma_90, "First-mover advantage should decrease with patience"

    print("\nKey insights:")
    print("1. Unique subgame perfect equilibrium with immediate agreement")
    print("2. First-mover advantage exists but diminishes with patience")
    print("3. Patient players get larger share regardless of proposal order")
    print("4. Discounting (time cost) drives agreement")

    return True


if __name__ == '__main__':
    test_solution()
