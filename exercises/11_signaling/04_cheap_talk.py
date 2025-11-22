"""
Exercise: Cheap Talk and Communication Games
=============================================

Cheap talk refers to communication that is costless and non-binding. Despite being
"cheap," such communication can still be informative in equilibrium under certain
conditions (Crawford-Sobel 1982).

Key question: When can pure communication convey information?

Learning Objectives:
- Understand cheap talk games
- Find informative equilibria
- Analyze conditions for credible communication
- Apply to expert advice and political discourse

Key Concepts:
- Costless signals
- Credibility and incentive alignment
- Babbling equilibrium (uninformative)
- Partially informative equilibria
- Crawford-Sobel model
"""

from typing import List, Dict, Callable, Tuple
import numpy as np


def analyze_cheap_talk_equilibrium(sender_bias: float, num_messages: int,
                                   state_distribution: str = 'uniform'):
    """
    Analyze equilibria in Crawford-Sobel cheap talk model.

    Setup:
    - Sender observes state θ (e.g., expert knows true value)
    - Sender sends costless message m
    - Receiver takes action a based on message
    - Sender prefers action a = θ + b (biased)
    - Receiver prefers action a = θ (unbiased)

    With uniform state distribution on [0,1]:
    - Babbling equilibrium always exists (receiver ignores message)
    - Informative equilibria partition state space into intervals
    - Maximum informativeness depends on bias b

    Args:
        sender_bias: Bias parameter b (sender prefers higher actions)
        num_messages: Number of distinct messages to try
        state_distribution: 'uniform' on [0,1]

    Returns:
        Dictionary with equilibrium partition thresholds
    """
    # TODO: Find partition equilibrium
    # For N message types, find thresholds 0 = t_0 < t_1 < ... < t_N = 1
    # Such that sender with state in [t_i, t_{i+1}] sends message m_i
    # Receiver responds with E[θ | θ in [t_i, t_{i+1}]]
    #
    # Indifference condition at threshold t_i:
    # Sender at t_i is indifferent between message i-1 and message i
    # This gives: (a_{i-1} - t_i - b)^2 = (a_i - t_i - b)^2
    #
    # For uniform distribution: a_i = (t_i + t_{i+1})/2
    # Can show: max N ≈ 1/(4b) for small b
    pass


def find_babbling_equilibrium(sender_preferences: Callable,
                              receiver_preferences: Callable,
                              states: List[float],
                              state_probs: List[float]):
    """
    Find babbling equilibrium where communication is uninformative.

    In babbling equilibrium:
    - Sender's message is independent of state
    - Receiver ignores message and takes prior-optimal action
    - Sender is indifferent among all messages

    Args:
        sender_preferences: (action, state, bias) -> utility
        receiver_preferences: (action, state) -> utility
        states: Possible states
        state_probs: Prior probabilities

    Returns:
        Receiver's optimal action ignoring messages
    """
    # TODO: Find babbling equilibrium
    # Receiver's optimal action = E[optimal action | prior]
    # For quadratic loss -(a - θ)^2, this is E[θ]
    # In babbling equilibrium, all messages are equally likely
    pass


def check_credibility(message: str, state: float, bias: float,
                     receiver_action: Callable) -> bool:
    """
    Check if a message is credible given sender's incentives.

    A message is credible if the sender with the claimed state actually wants
    to send that message (given receiver's response).

    Args:
        message: Claimed message/state
        state: True state
        bias: Sender's bias parameter
        receiver_action: Function mapping message to receiver's action

    Returns:
        True if sender with this state would send this message
    """
    # TODO: Check credibility
    # If sender claims message m, receiver takes action a(m)
    # Sender with state θ has utility -(a - θ - b)^2
    # Message is credible if sender prefers this to any other message
    pass


def expert_advice_game(expert_bias: float, decision_values: List[float],
                      expert_info_quality: float):
    """
    Model expert advice with potential bias.

    Setup:
    - Expert observes noisy signal about best decision
    - Expert may be biased (prefers certain outcomes)
    - Decision-maker receives advice and chooses
    - How much should decision-maker trust the advice?

    Args:
        expert_bias: How much expert's preferences differ
        decision_values: Possible values of decisions
        expert_info_quality: Precision of expert's information

    Returns:
        Optimal decision-maker strategy and expected welfare
    """
    # TODO: Analyze expert advice game
    # If bias is small and info quality high: follow advice
    # If bias is large: discount or ignore advice
    # Find threshold bias where advice becomes uninformative
    # Return: {'trust_advice': bool, 'expected_welfare': float}
    pass


def political_cheap_talk(candidate_positions: List[float],
                        voter_ideals: List[float],
                        campaign_messages: List[str]):
    """
    Analyze cheap talk in political campaigns.

    Candidates send campaign messages (cheap talk) about their positions.
    Voters must infer true positions from messages.

    Args:
        candidate_positions: True positions on policy spectrum
        voter_ideals: Voters' ideal positions
        campaign_messages: Messages candidates can send

    Returns:
        Equilibrium beliefs and voting behavior
    """
    # TODO: Model political cheap talk
    # In equilibrium: voters may learn nothing (babbling)
    # Or partial information if preferences somewhat aligned
    # Extreme bias → uninformative campaigns
    # Return beliefs and optimal voting given messages
    pass


# Test functions
def test_babbling_equilibrium():
    """Test babbling equilibrium finding."""
    states = [0.2, 0.5, 0.8]
    probs = [0.3, 0.4, 0.3]

    def sender_pref(action, state, bias):
        return -(action - state - bias)**2

    def receiver_pref(action, state):
        return -(action - state)**2

    action = find_babbling_equilibrium(sender_pref, receiver_pref, states, probs)

    # Expected state = 0.3*0.2 + 0.4*0.5 + 0.3*0.8 = 0.06 + 0.2 + 0.24 = 0.5
    assert action is not None
    expected_action = sum(s * p for s, p in zip(states, probs))
    assert abs(action - expected_action) < 0.01, f"Expected {expected_action}, got {action}"
    print(f"✓ Babbling equilibrium action: {action:.3f}")


def test_crawford_sobel():
    """Test Crawford-Sobel partition equilibrium."""
    # Small bias should allow more informative communication
    result_small_bias = analyze_cheap_talk_equilibrium(
        sender_bias=0.05,
        num_messages=4
    )

    # Large bias limits informativeness
    result_large_bias = analyze_cheap_talk_equilibrium(
        sender_bias=0.2,
        num_messages=4
    )

    assert result_small_bias is not None
    assert result_large_bias is not None

    print(f"✓ Crawford-Sobel equilibria found:")
    print(f"  Small bias (0.05): {result_small_bias}")
    print(f"  Large bias (0.20): {result_large_bias}")


def test_credibility():
    """Test message credibility."""
    def receiver_action(msg):
        # Receiver believes message and acts accordingly
        return float(msg)

    # With bias 0.1, sender at state 0.5 wants action 0.6
    # If sender claims 0.6, receiver does 0.6 - this is credible
    is_credible = check_credibility(
        message="0.6",
        state=0.5,
        bias=0.1,
        receiver_action=receiver_action
    )

    assert is_credible is not None
    print(f"✓ Credibility check: {is_credible}")


def test_expert_advice():
    """Test expert advice model."""
    result = expert_advice_game(
        expert_bias=0.15,
        decision_values=[0, 0.5, 1.0],
        expert_info_quality=0.8
    )

    assert result is not None
    assert 'trust_advice' in result or 'expected_welfare' in result

    print(f"✓ Expert advice analysis: {result}")


if __name__ == "__main__":
    print("\n=== Cheap Talk Games Tests ===\n")
    test_babbling_equilibrium()
    test_crawford_sobel()
    test_credibility()
    test_expert_advice()
    print("\n🎉 All tests passed! You understand cheap talk games!")

    print("\n=== Key Insights ===")
    print("• Cheap talk can be informative despite being costless")
    print("• Informativeness depends on alignment of interests")
    print("• Babbling equilibrium always exists (fully uninformative)")
    print("• Partial alignment → partially informative equilibria")
    print("• Applications: expert advice, political campaigns, negotiations")
    print("• Crawford-Sobel: max messages ≈ 1/(4×bias)")
