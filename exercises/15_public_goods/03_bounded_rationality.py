"""
Exercise: Bounded Rationality and Learning
===========================================

Bounded rationality recognizes that players have cognitive limitations.
They don't always compute Nash equilibria but use heuristics and learn.

Learning Objectives:
- Model limited reasoning with quantal response
- Implement cognitive hierarchy models
- Analyze learning dynamics
- Apply to market entry games

Key Concepts:
- Quantal Response Equilibrium (QRE)
- Cognitive Hierarchy (CH) model
- Reinforcement learning
- Experience-weighted attraction (EWA)
- Adaptive play
"""

from typing import Dict, List, Tuple, Callable
import numpy as np


def quantal_response(payoffs: np.ndarray, lambda_rationality: float) -> np.ndarray:
    """
    Calculate Quantal Response: probabilistic best response.

    Instead of always playing best response, players play better actions
    with higher probability (logit choice).

    P(action i) ∝ exp(λ * payoff_i)

    where λ is rationality parameter:
    - λ = 0: completely random
    - λ → ∞: best response (fully rational)

    Args:
        payoffs: Expected payoffs for each action
        lambda_rationality: Rationality parameter

    Returns:
        Probability distribution over actions
    """
    # TODO: Calculate quantal response probabilities
    #
    # Logit choice rule:
    # P(action_i) = exp(λ * payoff_i) / Σ_j exp(λ * payoff_j)
    #
    # This is softmax function with temperature 1/λ
    #
    # Properties:
    # - Higher payoff → higher probability (but not certainty)
    # - As λ increases, concentrates on best action
    # - Explains observed randomness in experiments
    #
    # Return probability distribution
    pass


def find_quantal_response_equilibrium(payoff_matrix1: np.ndarray,
                                     payoff_matrix2: np.ndarray,
                                     lambda_param: float,
                                     max_iterations: int = 100) -> Dict:
    """
    Find Quantal Response Equilibrium (QRE) for 2-player game.

    QRE is a fixed point where each player quantal-responds to the other.

    Args:
        payoff_matrix1: Payoff matrix for player 1
        payoff_matrix2: Payoff matrix for player 2
        lambda_param: Rationality parameter
        max_iterations: Maximum iterations for fixed-point search

    Returns:
        QRE strategy profile
    """
    # TODO: Find QRE using fixed-point iteration
    #
    # Algorithm:
    # 1. Start with initial guess (e.g., uniform)
    # 2. Compute player 1's QR to player 2's strategy
    # 3. Compute player 2's QR to player 1's strategy
    # 4. Repeat until convergence
    #
    # QRE is interior (fully mixed) for finite λ
    # As λ → ∞, QRE → Nash equilibrium
    # As λ → 0, QRE → uniform random
    #
    # QRE often fits experimental data better than Nash
    #
    # Return: {
    #   'player1_strategy': [...],
    #   'player2_strategy': [...],
    #   'converged': True/False
    # }
    pass


def cognitive_hierarchy_prediction(payoff_matrix: np.ndarray,
                                  max_level: int = 3,
                                  level_distribution: List[float] = None) -> np.ndarray:
    """
    Predict behavior using Cognitive Hierarchy model.

    CH model: Different players think at different levels.
    Level-0: random
    Level-k: best respond to belief about lower levels

    Population is mixture of levels with Poisson distribution (typically).

    Args:
        payoff_matrix: Payoff matrix
        max_level: Maximum level to consider
        level_distribution: P(level=k) for k=0,1,2,... (default: Poisson)

    Returns:
        Aggregate predicted play
    """
    # TODO: Implement Cognitive Hierarchy model
    #
    # Default level distribution: Poisson(τ) where τ ≈ 1.5
    # P(level = k) = τ^k * e^(-τ) / k!
    #
    # Algorithm:
    # 1. Compute level-0 play (uniform random)
    # 2. For k = 1 to max_level:
    #    - Compute belief: average of levels 0 to k-1 weighted by population
    #    - Level-k best responds to this belief
    # 3. Average strategies across levels weighted by level_distribution
    #
    # CH explains:
    # - Why people don't play Nash in one-shot games
    # - Systematic patterns in experimental data
    # - Heterogeneity in sophistication
    #
    # Return population strategy
    pass


def reinforcement_learning(num_actions: int, num_rounds: int,
                          payoff_history: List[Tuple[int, float]],
                          learning_rate: float = 0.1) -> np.ndarray:
    """
    Simulate reinforcement learning (Roth-Erev model).

    Players learn by reinforcing actions that worked well in the past.

    Args:
        num_actions: Number of available actions
        num_rounds: Number of rounds to simulate
        payoff_history: List of (action_played, payoff_received) tuples
        learning_rate: How fast to update (epsilon in Roth-Erev)

    Returns:
        Updated propensities for each action
    """
    # TODO: Implement reinforcement learning
    #
    # Roth-Erev model:
    # - Maintain propensity q_i for each action i
    # - Choose action with probability proportional to propensity
    # - Update: q_i(t+1) = (1-φ)*q_i(t) + payoff_i(t) if i was played
    #
    # Alternatively, simple Q-learning:
    # - Q(action) estimates expected payoff
    # - Update: Q(a) ← Q(a) + α * (payoff - Q(a)) if a was played
    #
    # Over time, propensities concentrate on better actions
    # But never fully converges to best response (keeps exploring)
    #
    # Return final propensities or Q-values
    pass


def experience_weighted_attraction(payoff_matrix: np.ndarray,
                                  history: List[Tuple[int, int, float]],
                                  phi: float = 0.5,
                                  delta: float = 0.5,
                                  rho: float = 0.1) -> np.ndarray:
    """
    Implement Experience-Weighted Attraction (EWA) learning.

    EWA generalizes both reinforcement and belief-based learning.

    Args:
        payoff_matrix: Payoff matrix
        history: List of (own_action, opponent_action, payoff) tuples
        phi: Depreciation parameter (memory decay)
        delta: Weight on hypothetical payoffs vs realized
        rho: Initial attraction level

    Returns:
        Attractions for each action
    """
    # TODO: Implement EWA learning
    #
    # Attraction A_i(t) for action i:
    # A_i(t+1) = [φ*N(t)*A_i(t) + [δ + (1-δ)*I(i=a(t))]*π_i(t)] / [φ*N(t) + 1]
    #
    # where:
    # - N(t) is experience weight
    # - I(i=a(t)) is indicator if action i was played
    # - δ controls weight on hypothetical vs realized payoffs
    # - φ controls memory decay
    #
    # Choice probability: exp(λ*A_i) / Σ exp(λ*A_j)
    #
    # EWA nests:
    # - Reinforcement learning (δ = 0)
    # - Belief-based learning (δ = 1)
    # - Weighted fictitious play (special case)
    #
    # Return attraction values
    pass


def market_entry_with_learning(num_firms: int, capacity: int,
                               entry_cost: float, market_value: float,
                               num_periods: int) -> Dict:
    """
    Simulate market entry game with learning.

    Each firm decides whether to enter. If ≤ capacity firms enter, they profit.
    If > capacity firms enter, all entrants lose.

    Standard: Mixed strategy equilibrium p = capacity/num_firms
    With learning: may see fluctuations, cycles, or convergence

    Args:
        num_firms: Number of potential entrants
        capacity: Maximum profitable entrants
        entry_cost: Cost to enter
        market_value: Value if entry successful
        num_periods: Number of periods to simulate

    Returns:
        Entry patterns over time
    """
    # TODO: Simulate market entry with learning
    #
    # Each period:
    # 1. Firms decide whether to enter based on learning rule
    # 2. Observe outcome (profit or loss)
    # 3. Update beliefs/propensities
    #
    # Possible learning rules:
    # - Imitate successful firms
    # - Fictitious play
    # - Reinforcement learning
    #
    # Dynamics:
    # - May cycle around equilibrium
    # - May converge to pure coordination (exactly k firms always enter)
    # - Depends on learning rule and parameters
    #
    # Return: {
    #   'entry_rates_over_time': [...],
    #   'average_entry_rate': ...,
    #   'equilibrium_prediction': capacity/num_firms,
    #   'converged': True/False
    # }
    pass


# Test functions
def test_quantal_response():
    """Test quantal response calculation."""
    payoffs = np.array([5, 10, 3])

    # Low rationality (λ = 1)
    qr_low = quantal_response(payoffs, lambda_rationality=1)

    # High rationality (λ = 10)
    qr_high = quantal_response(payoffs, lambda_rationality=10)

    # Action 2 has highest payoff (10)
    assert qr_high[1] > qr_high[0] and qr_high[1] > qr_high[2]

    # Higher λ concentrates more on best action
    assert qr_high[1] > qr_low[1]

    print(f"✓ Quantal response:")
    print(f"  λ=1:  {qr_low}")
    print(f"  λ=10: {qr_high}")


def test_qre():
    """Test QRE finding."""
    # Matching pennies
    payoff1 = np.array([[1, -1], [-1, 1]])
    payoff2 = np.array([[-1, 1], [1, -1]])

    result = find_quantal_response_equilibrium(payoff1, payoff2, lambda_param=2)

    assert result is not None

    # QRE should be close to (0.5, 0.5) but not exactly
    # (Nash is exactly 0.5, QRE is interior but close for high λ)

    print(f"✓ QRE: P1={result['player1_strategy']}, P2={result['player2_strategy']}")


def test_cognitive_hierarchy():
    """Test cognitive hierarchy prediction."""
    # Simple 3x3 game
    payoff_matrix = np.array([
        [3, 0, 0],
        [0, 2, 0],
        [0, 0, 1]
    ])

    prediction = cognitive_hierarchy_prediction(payoff_matrix, max_level=3)

    assert prediction is not None
    assert np.sum(prediction) - 1.0 < 0.01  # Should sum to 1

    print(f"✓ Cognitive Hierarchy prediction: {prediction}")


def test_reinforcement_learning():
    """Test reinforcement learning."""
    # Simulate history of playing action 1 with good payoffs
    history = [(1, 10), (1, 8), (0, 2), (1, 12), (0, 1)]

    propensities = reinforcement_learning(
        num_actions=2,
        num_rounds=5,
        payoff_history=history,
        learning_rate=0.2
    )

    assert propensities is not None

    # Action 1 should have higher propensity (better payoffs)
    # assert propensities[1] > propensities[0]

    print(f"✓ Reinforcement learning propensities: {propensities}")


def test_market_entry():
    """Test market entry with learning."""
    result = market_entry_with_learning(
        num_firms=10,
        capacity=4,
        entry_cost=10,
        market_value=30,
        num_periods=50
    )

    assert result is not None

    avg_entry = result['average_entry_rate']
    equilibrium = result['equilibrium_prediction']

    # Should be close to equilibrium on average
    # assert abs(avg_entry - equilibrium) < 0.2

    print(f"✓ Market entry: average={avg_entry:.2f}, equilibrium={equilibrium:.2f}")


if __name__ == "__main__":
    print("\n=== Bounded Rationality Tests ===\n")
    test_quantal_response()
    test_qre()
    test_cognitive_hierarchy()
    test_reinforcement_learning()
    test_market_entry()
    print("\n🎉 All tests passed! You understand bounded rationality!")

    print("\n=== Key Insights ===")
    print("• Bounded rationality: cognitive limitations affect strategic behavior")
    print("• QRE: probabilistic best response, better fits experimental data")
    print("• Cognitive Hierarchy: heterogeneous levels of strategic thinking")
    print("• Reinforcement learning: learn from experience, not full rationality")
    print("• EWA: unified framework for different learning models")
    print("• Learning dynamics can differ from Nash equilibrium predictions")
    print("• These models explain systematic deviations in experiments")
