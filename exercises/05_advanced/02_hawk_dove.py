"""
Exercise 16: Hawk-Dove Game Analysis

The Hawk-Dove game (also called Chicken or Snowdrift game) models conflicts
over resources where escalation is costly.

This exercise explores the rich dynamics of this classic evolutionary game.

TODO: Implement comprehensive Hawk-Dove analysis.
"""

import numpy as np


def create_hawk_dove_game(V, C):
    """
    Create Hawk-Dove game with given parameters.

    Args:
        V: Value of resource
        C: Cost of fighting

    Returns:
        Dictionary with payoff matrix and parameters

    TODO: Create game specification.
    """
    payoff_matrix = {
        ('H', 'H'): ((V - C) / 2, (V - C) / 2),
        ('H', 'D'): (V, 0),
        ('D', 'H'): (0, V),
        ('D', 'D'): (V / 2, V / 2),
    }

    return {
        'payoff_matrix': payoff_matrix,
        'V': V,
        'C': C,
        'matrix_form': np.array([
            [(V - C) / 2, V],
            [0, V / 2]
        ])
    }


def find_nash_equilibria_hawk_dove(V, C):
    """
    Find all Nash Equilibria for Hawk-Dove game.

    Args:
        V: Value of resource
        C: Cost of conflict

    Returns:
        List of equilibria (pure and mixed)

    TODO: Find all Nash Equilibria.
    HINT: Check pure strategy equilibria and compute mixed strategy equilibrium.
    """
    equilibria = []

    # TODO: Check pure strategy equilibria
    # When C > V: both (H,D) and (D,H) are Nash equilibria
    # When C < V: only (H,H) is Nash equilibrium

    if C > V:
        equilibria.append({'type': 'pure', 'strategy': ('H', 'D')})
        equilibria.append({'type': 'pure', 'strategy': ('D', 'H')})

        # Mixed strategy equilibrium
        # p = probability of playing Hawk
        # At equilibrium: E(H) = E(D)
        # E(H) = p*(V-C)/2 + (1-p)*V
        # E(D) = p*0 + (1-p)*V/2
        # Setting equal: p*(V-C)/2 + (1-p)*V = (1-p)*V/2
        # Solving: p = V/C

        p_hawk = V / C
        equilibria.append({
            'type': 'mixed',
            'strategy': {'H': p_hawk, 'D': 1 - p_hawk}
        })
    else:
        equilibria.append({'type': 'pure', 'strategy': ('H', 'H')})

    return equilibria


def expected_payoff_mixed(p, game):
    """
    Calculate expected payoff for each strategy against a population
    playing Hawk with probability p.

    Args:
        p: Probability of playing Hawk
        game: Game dictionary with payoff matrix

    Returns:
        Tuple (expected_payoff_hawk, expected_payoff_dove)

    TODO: Calculate expected payoffs.
    """
    V = game['V']
    C = game['C']

    # TODO: Calculate expected payoffs
    # E(Hawk) = p * (V-C)/2 + (1-p) * V
    # E(Dove) = p * 0 + (1-p) * V/2

    E_hawk = p * (V - C) / 2 + (1 - p) * V
    E_dove = p * 0 + (1 - p) * V / 2

    return E_hawk, E_dove


def plot_payoff_vs_frequency(game, num_points=100):
    """
    Generate data for plotting expected payoffs vs frequency of Hawks.

    Args:
        game: Game dictionary
        num_points: Number of points to sample

    Returns:
        Dictionary with frequencies and payoffs

    TODO: Generate plot data.
    """
    frequencies = np.linspace(0, 1, num_points)
    hawk_payoffs = []
    dove_payoffs = []

    # TODO: Calculate payoffs for each frequency
    for p in frequencies:
        E_h, E_d = expected_payoff_mixed(p, game)
        hawk_payoffs.append(E_h)
        dove_payoffs.append(E_d)

    return {
        'frequencies': frequencies,
        'hawk_payoffs': hawk_payoffs,
        'dove_payoffs': dove_payoffs,
    }


def stable_polymorphism_frequency(V, C):
    """
    Find the stable frequency of Hawks in the population.

    At equilibrium, E(Hawk) = E(Dove), so neither has advantage.

    Args:
        V: Value
        C: Cost

    Returns:
        Equilibrium frequency of Hawks, or None if not applicable

    TODO: Calculate equilibrium frequency.
    """
    if C <= V:
        return None  # All Hawks is the only equilibrium

    # TODO: Solve for p where E(Hawk) = E(Dove)
    # p*(V-C)/2 + (1-p)*V = (1-p)*V/2
    # p*(V-C)/2 = (1-p)*V/2 - (1-p)*V
    # p*(V-C)/2 = (1-p)*(V/2 - V)
    # p*(V-C)/2 = -(1-p)*V/2
    # p*(V-C) = -(1-p)*V
    # p(V-C) = -V + pV
    # pV - pC = -V + pV
    # -pC = -V
    # p = V/C

    return V / C


def test_solution():
    """Test function - Do not modify."""
    # Case 1: C > V (conflict is costly)
    print("Case 1: C > V (Costly conflict)")
    game1 = create_hawk_dove_game(V=2, C=4)

    equilibria1 = find_nash_equilibria_hawk_dove(2, 4)
    print(f"Number of equilibria: {len(equilibria1)}")
    assert len(equilibria1) == 3, "Should have 2 pure + 1 mixed equilibrium"

    # Check mixed equilibrium
    mixed_eq = [eq for eq in equilibria1 if eq['type'] == 'mixed'][0]
    p_hawk = mixed_eq['strategy']['H']
    print(f"Mixed strategy equilibrium: p(Hawk) = {p_hawk:.2f}")
    assert abs(p_hawk - 0.5) < 0.01, "With V=2, C=4, should be 2/4 = 0.5"

    # Verify equilibrium property
    E_h, E_d = expected_payoff_mixed(p_hawk, game1)
    print(f"At equilibrium: E(Hawk) = {E_h:.2f}, E(Dove) = {E_d:.2f}")
    assert abs(E_h - E_d) < 0.01, "Payoffs should be equal at mixed equilibrium"

    # Case 2: C < V (conflict is worth it)
    print("\nCase 2: C < V (Conflict pays off)")
    equilibria2 = find_nash_equilibria_hawk_dove(V=4, C=2)
    print(f"Number of equilibria: {len(equilibria2)}")
    assert len(equilibria2) == 1, "Should have only 1 pure equilibrium (H,H)"
    assert equilibria2[0]['strategy'] == ('H', 'H'), "Should be (H,H)"

    # Test stable polymorphism
    poly_freq = stable_polymorphism_frequency(V=2, C=4)
    print(f"\nStable polymorphism frequency: {poly_freq:.2f}")
    assert abs(poly_freq - 0.5) < 0.01

    # Generate plot data
    plot_data = plot_payoff_vs_frequency(game1, num_points=20)
    print(f"\nGenerated {len(plot_data['frequencies'])} data points for plotting")

    # At equilibrium frequency, payoffs should be equal
    eq_idx = int(p_hawk * 19)  # Index in our data
    h_pay = plot_data['hawk_payoffs'][eq_idx]
    d_pay = plot_data['dove_payoffs'][eq_idx]
    print(f"At p={p_hawk:.2f}: Hawk payoff={h_pay:.2f}, Dove payoff={d_pay:.2f}")

    print("\nKey insights:")
    print("1. When C > V: Mixed strategy ESS with polymorphism")
    print("2. When C < V: Pure strategy equilibrium (all Hawks)")
    print("3. Hawk-Dove explains territorial behavior and ritualized combat")
    print("4. Real animals often use assessment and signaling to avoid costly fights")

    return True


if __name__ == '__main__':
    test_solution()
