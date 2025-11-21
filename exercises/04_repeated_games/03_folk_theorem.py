"""
Exercise 13: Folk Theorem

The Folk Theorem states that in infinitely repeated games, a wide range of outcomes
can be sustained as Nash Equilibria through appropriate punishment strategies.

Key idea: If players are patient enough (high discount factor), they can sustain
cooperative outcomes by threatening to punish deviations.

TODO: Understand and implement Folk Theorem concepts.
"""


def calculate_present_value(payoff_stream, discount_factor):
    """
    Calculate the present value of a stream of payoffs.

    PV = Σ δ^t * payoff_t where δ is the discount factor

    Args:
        payoff_stream: List of payoffs per period
        discount_factor: Discount factor (0 < δ < 1)

    Returns:
        Present value of the stream

    TODO: Implement present value calculation.
    """
    pv = 0.0

    # TODO: Calculate discounted sum
    for t, payoff in enumerate(payoff_stream):
        pv += (discount_factor ** t) * payoff

    return pv


def infinite_stream_value(per_period_payoff, discount_factor):
    """
    Calculate present value of an infinite constant payoff stream.

    For constant payoff r per period: PV = r / (1 - δ)

    Args:
        per_period_payoff: Payoff received each period
        discount_factor: Discount factor

    Returns:
        Present value

    TODO: Implement infinite stream formula.
    """
    # TODO: Implement formula r / (1 - delta)
    return per_period_payoff / (1 - discount_factor)


def minimum_discount_for_cooperation(payoff_matrix, strategy='grim'):
    """
    Find the minimum discount factor needed to sustain cooperation.

    In Prisoner's Dilemma, cooperation can be sustained if:
    δ >= (T - R) / (T - P)

    where:
    T = Temptation (defect vs cooperate)
    R = Reward (mutual cooperation)
    P = Punishment (mutual defection)

    Args:
        payoff_matrix: Standard form PD payoff matrix
        strategy: Punishment strategy ('grim' or 'tit_for_tat')

    Returns:
        Minimum discount factor to sustain cooperation

    TODO: Calculate minimum discount factor.
    """
    # Extract payoffs
    R = payoff_matrix[('C', 'C')][0]  # Reward
    T = payoff_matrix[('D', 'C')][0]  # Temptation
    P = payoff_matrix[('D', 'D')][0]  # Punishment
    S = payoff_matrix[('C', 'D')][0]  # Sucker's payoff

    # TODO: Calculate minimum delta
    # Value of cooperating forever: R / (1 - δ)
    # Value of deviating once then being punished:
    #   - Grim trigger: T + δP/(1-δ)
    #   - Need: R/(1-δ) >= T + δP/(1-δ)

    if strategy == 'grim':
        # R/(1-δ) >= T + δP/(1-δ)
        # R >= T(1-δ) + δP
        # R >= T - Tδ + δP
        # R - T >= δ(P - T)
        # δ >= (T - R) / (T - P)
        min_delta = (T - R) / (T - P)
    else:
        # For TFT or other strategies, calculation may differ
        min_delta = (T - R) / (T - P)

    return min_delta


def can_sustain_outcome(payoff, deviation_payoff, punishment_payoff, discount_factor):
    """
    Check if an outcome can be sustained as equilibrium.

    An outcome can be sustained if no player wants to deviate:
    Value(cooperate) >= Value(deviate once + get punished)

    Args:
        payoff: Payoff from sustained outcome per period
        deviation_payoff: Payoff from deviating once
        punishment_payoff: Payoff during punishment phase
        discount_factor: Discount factor

    Returns:
        True if outcome can be sustained

    TODO: Implement sustainability check.
    """
    # Value of sustained outcome
    value_cooperate = infinite_stream_value(payoff, discount_factor)

    # Value of deviating once then getting punished forever
    value_deviate = deviation_payoff + discount_factor * infinite_stream_value(
        punishment_payoff, discount_factor
    )

    # TODO: Check if cooperation is better than deviation
    return value_cooperate >= value_deviate - 0.0001


def find_feasible_payoffs(payoff_matrix, discount_factor):
    """
    Find the range of average payoffs that can be sustained.

    According to Folk Theorem, any individually rational payoff above
    the minmax value can be sustained with high enough discount factor.

    Args:
        payoff_matrix: The stage game payoff matrix
        discount_factor: Discount factor

    Returns:
        Dictionary with analysis of feasible region

    TODO: Analyze feasible payoffs.
    """
    # Get key payoffs
    CC_payoff = payoff_matrix[('C', 'C')][0]
    CD_payoff = payoff_matrix[('C', 'D')][0]
    DC_payoff = payoff_matrix[('D', 'C')][0]
    DD_payoff = payoff_matrix[('D', 'D')][0]

    # Minmax value (worst that opponents can force you to)
    minmax = DD_payoff  # In PD, minmax is mutual defection

    # Check what can be sustained
    results = {
        'minmax': minmax,
        'can_sustain_cooperation': can_sustain_outcome(
            CC_payoff, DC_payoff, DD_payoff, discount_factor
        ),
        'required_delta_for_cooperation': minimum_discount_for_cooperation(payoff_matrix),
    }

    return results


def test_solution():
    """Test function - Do not modify."""
    # Test present value calculation
    payoffs = [10, 10, 10]
    delta = 0.9
    pv = calculate_present_value(payoffs, delta)
    expected = 10 + 10*0.9 + 10*0.81
    assert abs(pv - expected) < 0.01, f"Expected {expected}, got {pv}"

    # Test infinite stream
    infinite_pv = infinite_stream_value(10, 0.9)
    assert abs(infinite_pv - 100) < 0.01, "10/(1-0.9) should be 100"

    # Test with Prisoner's Dilemma
    payoff_matrix = {
        ('C', 'C'): (3, 3),
        ('C', 'D'): (0, 5),
        ('D', 'C'): (5, 0),
        ('D', 'D'): (1, 1),
    }

    min_delta = minimum_discount_for_cooperation(payoff_matrix)
    print(f"\nMinimum discount factor for cooperation: {min_delta:.3f}")
    assert 0 < min_delta < 1, "Should be between 0 and 1"

    # With discount factor below minimum, cooperation cannot be sustained
    assert can_sustain_outcome(3, 5, 1, min_delta - 0.01) == False

    # With discount factor above minimum, cooperation can be sustained
    assert can_sustain_outcome(3, 5, 1, min_delta + 0.01) == True

    # Analyze feasible outcomes
    analysis = find_feasible_payoffs(payoff_matrix, 0.9)
    print(f"\nWith δ=0.9:")
    print(f"  Minmax value: {analysis['minmax']}")
    print(f"  Can sustain cooperation: {analysis['can_sustain_cooperation']}")
    print(f"  Required δ: {analysis['required_delta_for_cooperation']:.3f}")

    print("\nKey insights - Folk Theorem:")
    print("1. Patient players (high δ) can sustain cooperative outcomes")
    print("2. Many different payoffs can be equilibria in repeated games")
    print("3. Punishment threats make cooperation credible")
    print("4. 'Shadow of the future' enables cooperation today")

    return True


if __name__ == '__main__':
    test_solution()
