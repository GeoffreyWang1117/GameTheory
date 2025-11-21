"""
Exercise 15: Evolutionary Game Theory

Evolutionary game theory applies game theory to biological evolution.
Instead of rational players, we have populations of strategies that reproduce
based on their fitness (payoff).

Key concept: Evolutionarily Stable Strategy (ESS) - a strategy that, if adopted
by a population, cannot be invaded by any rare mutant strategy.

TODO: Implement evolutionary dynamics and ESS analysis.
"""

import numpy as np


def replicator_dynamics(population, payoff_matrix, dt=0.01):
    """
    Update population proportions according to replicator dynamics.

    The replicator equation: dx_i/dt = x_i * (f_i - f_avg)
    where f_i is fitness of strategy i, f_avg is average fitness

    Args:
        population: Array of population proportions (must sum to 1)
        payoff_matrix: 2D numpy array of payoffs
        dt: Time step

    Returns:
        Updated population proportions

    TODO: Implement replicator dynamics update.
    """
    population = np.array(population, dtype=float)

    # Calculate fitness for each strategy
    # fitness[i] = sum_j (payoff[i][j] * population[j])
    fitness = payoff_matrix @ population

    # Average fitness
    avg_fitness = np.dot(population, fitness)

    # TODO: Update population according to replicator dynamics
    # dx_i/dt = x_i * (f_i - f_avg)
    dpopulation = population * (fitness - avg_fitness) * dt

    new_population = population + dpopulation

    # Ensure non-negative and normalized
    new_population = np.maximum(new_population, 0)
    total = np.sum(new_population)
    if total > 0:
        new_population /= total

    return new_population


def simulate_evolution(initial_population, payoff_matrix, steps=1000, dt=0.01):
    """
    Simulate evolutionary dynamics over time.

    Args:
        initial_population: Starting population distribution
        payoff_matrix: Payoff matrix
        steps: Number of time steps
        dt: Time step size

    Returns:
        Array of population distributions over time

    TODO: Simulate evolution.
    """
    history = [np.array(initial_population)]

    # TODO: Run replicator dynamics for 'steps' iterations
    current = np.array(initial_population)

    for _ in range(steps):
        current = replicator_dynamics(current, payoff_matrix, dt)
        history.append(current.copy())

    return np.array(history)


def is_ess(strategy_index, payoff_matrix, epsilon=0.01):
    """
    Check if a pure strategy is an Evolutionarily Stable Strategy.

    A strategy i is an ESS if for all j ≠ i:
    1. E(i, i) >= E(j, i) (Nash condition)
    2. If E(i, i) = E(j, i), then E(i, j) > E(j, j) (stability condition)

    Args:
        strategy_index: Index of the strategy to check
        payoff_matrix: Payoff matrix
        epsilon: Tolerance for equality

    Returns:
        True if strategy is an ESS

    TODO: Implement ESS check.
    """
    n = len(payoff_matrix)
    i = strategy_index

    # TODO: Check ESS conditions against all other strategies
    for j in range(n):
        if i == j:
            continue

        # Payoffs when playing against strategy i
        E_i_i = payoff_matrix[i][i]  # Strategy i vs i
        E_j_i = payoff_matrix[j][i]  # Strategy j vs i

        # Check Nash condition
        if E_i_i < E_j_i - epsilon:
            return False

        # If equal, check stability condition
        if abs(E_i_i - E_j_i) < epsilon:
            E_i_j = payoff_matrix[i][j]
            E_j_j = payoff_matrix[j][j]

            if E_i_j <= E_j_j + epsilon:
                return False

    return True


def find_all_ess(payoff_matrix):
    """
    Find all pure strategy ESS.

    Args:
        payoff_matrix: Payoff matrix (numpy array or list of lists)

    Returns:
        List of indices of ESS strategies

    TODO: Find all ESS.
    """
    payoff_matrix = np.array(payoff_matrix)
    n = len(payoff_matrix)

    ess_strategies = []

    # TODO: Check each strategy
    for i in range(n):
        if is_ess(i, payoff_matrix):
            ess_strategies.append(i)

    return ess_strategies


def hawk_dove_payoffs(V, C):
    """
    Create payoff matrix for Hawk-Dove game.

    V = value of resource
    C = cost of fighting

    Payoffs:
    - Hawk vs Hawk: (V-C)/2 each (split resource minus fighting cost)
    - Hawk vs Dove: V to Hawk, 0 to Dove
    - Dove vs Hawk: 0 to Dove, V to Hawk
    - Dove vs Dove: V/2 each (share resource)

    Args:
        V: Value of resource
        C: Cost of fighting (assume C > V for interesting dynamics)

    Returns:
        2x2 numpy array payoff matrix

    TODO: Create Hawk-Dove payoff matrix.
    """
    # TODO: Create payoff matrix
    # Rows/Cols: [Hawk, Dove]
    payoff_matrix = np.array([
        [(V - C) / 2, V],      # Hawk vs [Hawk, Dove]
        [0, V / 2]              # Dove vs [Hawk, Dove]
    ])

    return payoff_matrix


def test_solution():
    """Test function - Do not modify."""
    # Test Hawk-Dove game where C > V
    V = 2
    C = 4
    payoff_matrix = hawk_dove_payoffs(V, C)

    print("Hawk-Dove Game Payoffs:")
    print("       Hawk    Dove")
    print(f"Hawk  {payoff_matrix[0,0]:5.1f}  {payoff_matrix[0,1]:5.1f}")
    print(f"Dove  {payoff_matrix[1,0]:5.1f}  {payoff_matrix[1,1]:5.1f}")

    # Check for ESS
    ess = find_all_ess(payoff_matrix)
    print(f"\nPure strategy ESS: {['Hawk' if i==0 else 'Dove' for i in ess]}")

    # When C > V, neither pure strategy is ESS!
    # There's a mixed ESS instead
    assert len(ess) == 0, "With C > V, no pure strategy is ESS"

    # Simulate evolution from different starting points
    print("\nSimulating evolution...")

    # Start with mostly Hawks
    pop1 = simulate_evolution([0.8, 0.2], payoff_matrix, steps=500)
    final1 = pop1[-1]
    print(f"Starting 80% Hawks -> Final: {final1[0]:.2%} Hawks, {final1[1]:.2%} Doves")

    # Start with mostly Doves
    pop2 = simulate_evolution([0.2, 0.8], payoff_matrix, steps=500)
    final2 = pop2[-1]
    print(f"Starting 20% Hawks -> Final: {final2[0]:.2%} Hawks, {final2[1]:.2%} Doves")

    # Both should converge to mixed equilibrium near V/C = 0.5
    expected_hawk_freq = V / C
    assert abs(final1[0] - expected_hawk_freq) < 0.1, "Should converge to V/C ratio"
    assert abs(final2[0] - expected_hawk_freq) < 0.1, "Should converge to V/C ratio"

    print(f"\nEquilibrium frequency of Hawks ≈ V/C = {V}/{C} = {V/C:.2f}")

    print("\nKey insights:")
    print("1. ESS is a refinement of Nash Equilibrium for evolutionary settings")
    print("2. Replicator dynamics shows how populations evolve over time")
    print("3. In Hawk-Dove with C>V, mixed strategy ESS emerges naturally")
    print("4. Polymorphism (multiple strategies coexisting) can be stable")

    return True


if __name__ == '__main__':
    test_solution()
