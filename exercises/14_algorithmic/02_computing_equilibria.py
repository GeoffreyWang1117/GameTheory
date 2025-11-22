"""
Exercise: Computing Nash Equilibria
====================================

Finding Nash equilibria is computationally challenging. For general games,
it's PPAD-complete (even for 2 players).

This exercise covers practical algorithms for computing equilibria.

Learning Objectives:
- Implement support enumeration for mixed strategies
- Use Lemke-Howson algorithm for 2-player games
- Understand computational complexity
- Apply best response dynamics

Key Concepts:
- Support enumeration
- Lemke-Howson algorithm
- PPAD complexity class
- Best response computation
- Fixed point algorithms
"""

from typing import Dict, List, Tuple, Set
import numpy as np
from itertools import combinations


def find_pure_nash_equilibria(payoff_matrix1: np.ndarray,
                              payoff_matrix2: np.ndarray) -> List[Tuple[int, int]]:
    """
    Find all pure strategy Nash equilibria by exhaustive search.

    Args:
        payoff_matrix1: Payoff matrix for player 1 (rows)
        payoff_matrix2: Payoff matrix for player 2 (columns)

    Returns:
        List of (row, col) tuples representing pure NE
    """
    # TODO: Find all pure Nash equilibria
    # For each strategy profile (i, j):
    #   Check if player 1 wants to deviate from i given j
    #   Check if player 2 wants to deviate from j given i
    # If neither wants to deviate, it's a Nash equilibrium
    #
    # Algorithm:
    # for i in range(num_rows):
    #     for j in range(num_cols):
    #         if payoff1[i,j] >= payoff1[k,j] for all k (player 1's BR to j)
    #         and payoff2[i,j] >= payoff2[i,k] for all k (player 2's BR to i)
    #         then (i,j) is a pure NE
    pass


def support_enumeration_2x2(payoff_matrix1: np.ndarray,
                            payoff_matrix2: np.ndarray) -> List[Dict]:
    """
    Find all Nash equilibria for 2x2 game using support enumeration.

    Support enumeration: Try all possible supports (sets of strategies played
    with positive probability) and solve for mixed strategy probabilities.

    Args:
        payoff_matrix1: 2x2 payoff matrix for player 1
        payoff_matrix2: 2x2 payoff matrix for player 2

    Returns:
        List of equilibria (pure and mixed)
    """
    # TODO: Enumerate all supports and find equilibria
    #
    # For 2x2 game, possible supports:
    # 1. ({0}, {0}), ({0}, {1}), ({1}, {0}), ({1}, {1}) - pure strategies
    # 2. ({0,1}, {0,1}) - both players mix
    #
    # For fully mixed equilibrium:
    # Player 1 mixes to make Player 2 indifferent:
    #   payoff2[0,0]*p + payoff2[1,0]*(1-p) = payoff2[0,1]*p + payoff2[1,1]*(1-p)
    # Solve for p (probability of row 0)
    #
    # Similarly for Player 2's mixing probability q
    #
    # Return: [
    #   {'player1': [1, 0], 'player2': [1, 0], 'type': 'pure'},
    #   {'player1': [p, 1-p], 'player2': [q, 1-q], 'type': 'mixed'},
    #   ...
    # ]
    pass


def best_response_dynamics(initial_strategy: np.ndarray,
                          payoff_matrices: List[np.ndarray],
                          max_iterations: int = 100) -> Dict:
    """
    Run best response dynamics to find (or approximate) Nash equilibrium.

    Players alternately play best responses to others' current strategies.
    May converge to pure NE, cycle, or chaos.

    Args:
        initial_strategy: Initial strategy profile
        payoff_matrices: List of payoff matrices for each player
        max_iterations: Maximum number of iterations

    Returns:
        Result of dynamics (converged or not)
    """
    # TODO: Implement best response dynamics
    #
    # Algorithm:
    # 1. Start with initial strategy profile
    # 2. Each iteration:
    #    - Player i computes best response to others' strategies
    #    - Update player i's strategy to BR
    #    - Check for convergence (strategy unchanged)
    # 3. Return final strategy or indicate cycling
    #
    # Note: BR dynamics may not converge!
    # Converges for: potential games, zero-sum games
    # May cycle for: coordination games, others
    #
    # Return: {
    #   'converged': True/False,
    #   'final_strategy': ...,
    #   'iterations': ...
    # }
    pass


def fictitious_play_simple(payoff_matrix1: np.ndarray,
                           payoff_matrix2: np.ndarray,
                           num_iterations: int = 1000) -> Dict:
    """
    Run fictitious play algorithm.

    Each player maintains beliefs about opponent's mixed strategy (based on
    historical play) and best responds to those beliefs.

    Args:
        payoff_matrix1: Payoff matrix for player 1
        payoff_matrix2: Payoff matrix for player 2
        num_iterations: Number of iterations

    Returns:
        Empirical frequency of play (approximates mixed NE if converges)
    """
    # TODO: Implement fictitious play
    #
    # Algorithm:
    # 1. Initialize: each player plays randomly
    # 2. Each iteration:
    #    - Player 1 believes Player 2 will play empirical frequency
    #    - Player 1 best responds to this belief
    #    - Update Player 1's empirical frequency
    #    - Same for Player 2
    # 3. In zero-sum games and some others, empirical frequencies converge to NE
    #
    # Return: {
    #   'player1_frequencies': [...],
    #   'player2_frequencies': [...],
    #   'converged': True/False
    # }
    pass


def lemke_howson_2player(payoff_matrix1: np.ndarray,
                         payoff_matrix2: np.ndarray) -> Dict:
    """
    Find Nash equilibrium using Lemke-Howson algorithm (simplified).

    Lemke-Howson is a pivoting algorithm that traces a path through
    best response polytopes to find a completely labeled vertex (NE).

    This is a simplified version for educational purposes.

    Args:
        payoff_matrix1: Payoff matrix for player 1
        payoff_matrix2: Payoff matrix for player 2

    Returns:
        A Nash equilibrium
    """
    # TODO: Implement simplified Lemke-Howson
    #
    # Full Lemke-Howson is complex (linear complementarity problem).
    # Simplified approach:
    # 1. Convert to linear complementarity formulation
    # 2. Use pivoting to trace path through polytope
    # 3. Find completely labeled vertex
    #
    # For this exercise, you can use support enumeration as fallback
    # Or implement a basic pivoting scheme
    #
    # Return: {
    #   'player1_strategy': [...],
    #   'player2_strategy': [...],
    #   'payoffs': (p1_payoff, p2_payoff)
    # }
    pass


def check_nash_equilibrium(strategy1: np.ndarray, strategy2: np.ndarray,
                          payoff_matrix1: np.ndarray,
                          payoff_matrix2: np.ndarray,
                          tolerance: float = 1e-6) -> bool:
    """
    Verify if a strategy profile is a Nash equilibrium.

    Args:
        strategy1: Player 1's mixed strategy
        strategy2: Player 2's mixed strategy
        payoff_matrix1: Player 1's payoff matrix
        payoff_matrix2: Player 2's payoff matrix
        tolerance: Numerical tolerance for comparisons

    Returns:
        True if strategy profile is a Nash equilibrium
    """
    # TODO: Verify Nash equilibrium
    #
    # Check:
    # 1. Each player's strategy is a best response
    # 2. Expected payoff from current strategy >= payoff from any deviation
    #
    # For player 1:
    #   current_payoff = strategy1.T @ payoff_matrix1 @ strategy2
    #   For each pure strategy i:
    #     pure_payoff_i = payoff_matrix1[i, :] @ strategy2
    #     Must have: pure_payoff_i <= current_payoff (+ tolerance)
    #
    # Similarly for player 2
    #
    # Return True if both conditions hold
    pass


# Test functions
def test_find_pure_nash():
    """Test finding pure Nash equilibria."""
    # Prisoner's Dilemma
    payoff1 = np.array([[3, 0], [5, 1]])
    payoff2 = np.array([[3, 5], [0, 1]])

    equilibria = find_pure_nash_equilibria(payoff1, payoff2)

    # (D, D) = (1, 1) is the unique pure NE
    assert equilibria is not None
    assert (1, 1) in equilibria, "Should find (D,D) as pure NE"

    print(f"✓ Pure Nash equilibria found: {equilibria}")


def test_support_enumeration():
    """Test support enumeration for 2x2 game."""
    # Matching Pennies (no pure NE, one mixed NE)
    payoff1 = np.array([[1, -1], [-1, 1]])
    payoff2 = np.array([[-1, 1], [1, -1]])

    equilibria = support_enumeration_2x2(payoff1, payoff2)

    assert equilibria is not None
    # Should find the mixed strategy equilibrium (0.5, 0.5) for both players

    print(f"✓ Equilibria found via support enumeration:")
    for eq in equilibria:
        print(f"  P1: {eq['player1']}, P2: {eq['player2']}")


def test_best_response_dynamics():
    """Test best response dynamics."""
    # Coordination game (should converge to a pure NE)
    payoff1 = np.array([[2, 0], [0, 1]])
    payoff2 = np.array([[2, 0], [0, 1]])

    initial = np.array([0.5, 0.5])  # Start with mixed

    result = best_response_dynamics(
        initial_strategy=initial,
        payoff_matrices=[payoff1, payoff2],
        max_iterations=50
    )

    assert result is not None

    print(f"✓ Best response dynamics:")
    print(f"  Converged: {result['converged']}")
    print(f"  Iterations: {result['iterations']}")


def test_fictitious_play():
    """Test fictitious play."""
    # Zero-sum game (should converge)
    payoff1 = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])  # Rock-Paper-Scissors
    payoff2 = -payoff1

    result = fictitious_play_simple(payoff1, payoff2, num_iterations=500)

    assert result is not None

    # Should converge to (1/3, 1/3, 1/3) for both players
    freq1 = result['player1_frequencies']

    print(f"✓ Fictitious play:")
    print(f"  P1 frequencies: {np.array(freq1)}")


def test_verify_nash():
    """Test Nash equilibrium verification."""
    # Matching pennies mixed NE
    payoff1 = np.array([[1, -1], [-1, 1]])
    payoff2 = np.array([[-1, 1], [1, -1]])

    strategy1 = np.array([0.5, 0.5])
    strategy2 = np.array([0.5, 0.5])

    is_nash = check_nash_equilibrium(strategy1, strategy2, payoff1, payoff2)

    assert is_nash is not None
    assert is_nash == True, "Should verify as Nash equilibrium"

    print(f"✓ Nash equilibrium verification: {is_nash}")


if __name__ == "__main__":
    print("\n=== Computing Nash Equilibria Tests ===\n")
    test_find_pure_nash()
    test_support_enumeration()
    test_best_response_dynamics()
    test_fictitious_play()
    test_verify_nash()
    print("\n🎉 All tests passed! You can compute Nash equilibria!")

    print("\n=== Key Insights ===")
    print("• Finding NE is computationally hard (PPAD-complete)")
    print("• Pure NE: check all strategy profiles (exponential)")
    print("• Mixed NE: support enumeration works for small games")
    print("• Lemke-Howson: polynomial for 2-player games")
    print("• Best response dynamics may not converge")
    print("• Fictitious play converges for zero-sum games")
    print("• Always verify computed equilibria!")
