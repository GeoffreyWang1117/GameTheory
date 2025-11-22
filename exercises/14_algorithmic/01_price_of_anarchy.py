"""
Exercise: Price of Anarchy
===========================

The Price of Anarchy (PoA) measures the efficiency loss due to selfish behavior.
It compares the worst Nash equilibrium to the social optimum.

PoA = (Social Optimum) / (Worst Nash Equilibrium)

Applications: traffic routing, network design, resource allocation

Learning Objectives:
- Understand efficiency of equilibria
- Calculate Price of Anarchy
- Analyze Braess's Paradox
- Study selfish routing games

Key Concepts:
- Social optimum vs Nash equilibrium
- Coordination ratio
- Braess's Paradox
- Selfish routing
- Network congestion games
"""

from typing import Dict, List, Tuple, Callable
import numpy as np


def calculate_price_of_anarchy(social_optimum: float,
                               nash_equilibria: List[float]) -> float:
    """
    Calculate the Price of Anarchy.

    PoA = (Best possible outcome) / (Worst equilibrium outcome)

    For costs: PoA = (Worst NE cost) / (Optimal cost)
    For utilities: PoA = (Optimal utility) / (Worst NE utility)

    Args:
        social_optimum: Social welfare at optimum
        nash_equilibria: List of social welfare values at different NE

    Returns:
        Price of Anarchy (>= 1, where 1 means efficient)
    """
    # TODO: Calculate PoA
    # If measuring costs (lower is better):
    #   PoA = max(nash_equilibria) / social_optimum
    # If measuring utilities (higher is better):
    #   PoA = social_optimum / min(nash_equilibria)
    #
    # PoA = 1 means equilibria are efficient
    # PoA > 1 means efficiency loss from selfish behavior
    pass


def selfish_routing_two_links(flow: float, latency_func1: Callable,
                              latency_func2: Callable) -> Dict:
    """
    Analyze selfish routing on two parallel links.

    Users route traffic selfishly to minimize their own latency.
    At equilibrium: latency on used routes is equal (Wardrop equilibrium).

    Args:
        flow: Total traffic demand
        latency_func1: l_1(x) - latency on link 1 as function of flow x
        latency_func2: l_2(x) - latency on link 2 as function of flow x

    Returns:
        Nash equilibrium routing and social optimum comparison
    """
    # TODO: Find selfish routing equilibrium and optimal routing
    #
    # Selfish (Wardrop) equilibrium:
    # - At equilibrium, latency_func1(f1) = latency_func2(f2) where f1 + f2 = flow
    # - Or if one link unused: latency on used link <= latency on unused link
    #
    # Social optimum:
    # - Minimize total latency: f1 * l1(f1) + f2 * l2(f2)
    # - Subject to: f1 + f2 = flow
    #
    # Compare equilibrium and optimum
    #
    # Return: {
    #   'equilibrium': {'flow1': f1, 'flow2': f2, 'total_latency': ...},
    #   'optimum': {'flow1': f1*, 'flow2': f2*, 'total_latency': ...},
    #   'price_of_anarchy': ...
    # }
    pass


def braess_paradox_network(flow: float) -> Dict:
    """
    Demonstrate Braess's Paradox: adding a link can worsen equilibrium.

    Classic 4-node network:
    - Original: A → B → D, A → C → D
    - After adding B → C link: all traffic uses A → B → C → D

    Args:
        flow: Total traffic from A to D

    Returns:
        Analysis showing paradox
    """
    # TODO: Analyze Braess's Paradox
    #
    # Original network:
    # Path 1 (A→B→D): latency = x + 45 (where x is flow on A→B)
    # Path 2 (A→C→D): latency = 45 + x (where x is flow on C→D)
    # Equilibrium: equal split, total latency = flow * 67.5
    #
    # After adding zero-cost link B→C:
    # New path A→B→C→D has latency = x + 0 + x = 2x
    # This becomes dominant, but total latency = flow * 2*flow > original!
    #
    # Paradox: Adding capacity made things worse!
    #
    # Return: {
    #   'original_equilibrium_latency': ...,
    #   'new_equilibrium_latency': ...,
    #   'paradox': True/False
    # }
    pass


def congestion_game_poa(num_players: int, facilities: List[Dict],
                       player_demands: List[int] = None) -> float:
    """
    Calculate Price of Anarchy for a congestion game.

    Each player chooses a facility. Cost depends on congestion.

    Args:
        num_players: Number of players
        facilities: List of {'capacity': c, 'cost_func': f(x)} dictionaries
        player_demands: Optional demand/weight for each player

    Returns:
        Price of Anarchy
    """
    # TODO: Calculate PoA for congestion game
    #
    # Nash equilibrium: Each player chooses facility to minimize their cost
    # Social optimum: Minimize sum of costs
    #
    # For identical players and facilities:
    # - Equal split is often optimal
    # - But equilibrium may be unequal
    #
    # PoA for linear cost functions: PoA = 4/3
    # PoA for general cost functions can be higher
    #
    # Return PoA value
    pass


def atomic_vs_nonatomic_routing(flow: float, latency_linear: Callable,
                                num_discrete_players: int = None) -> Dict:
    """
    Compare atomic (discrete players) vs non-atomic (infinitesimal) routing.

    Non-atomic: Flow is continuous (many tiny players)
    Atomic: Discrete number of players with non-negligible flow

    Args:
        flow: Total traffic demand
        latency_linear: Linear latency function l(x) = a*x + b
        num_discrete_players: If provided, analyze atomic game

    Returns:
        Comparison of models
    """
    # TODO: Compare atomic and non-atomic models
    #
    # Non-atomic (Wardrop equilibrium):
    # - Each player infinitesimal, no impact on congestion
    # - Equalize latencies across paths
    #
    # Atomic (Nash equilibrium):
    # - Finite players, each affects congestion
    # - May have different PoA
    #
    # Atomic games can have worse PoA than non-atomic
    #
    # Return: {
    #   'nonatomic_poa': ...,
    #   'atomic_poa': ...,
    #   'comparison': 'atomic_worse'/'nonatomic_worse'/'equal'
    # }
    pass


# Test functions
def test_price_of_anarchy():
    """Test PoA calculation."""
    social_optimum = 100
    nash_equilibria = [90, 85, 88]

    poa = calculate_price_of_anarchy(social_optimum, nash_equilibria)

    # Worst NE is 85, so PoA = 100/85 ≈ 1.176
    assert poa is not None
    assert poa >= 1, "PoA should be at least 1"

    print(f"✓ Price of Anarchy: {poa:.3f}")


def test_selfish_routing():
    """Test selfish routing analysis."""
    # Linear latency functions
    l1 = lambda x: x        # Link 1: l(x) = x
    l2 = lambda x: 1        # Link 2: l(x) = 1 (constant)

    result = selfish_routing_two_links(flow=1, latency_func1=l1, latency_func2=l2)

    assert result is not None

    eq_latency = result['equilibrium']['total_latency']
    opt_latency = result['optimum']['total_latency']
    poa = result['price_of_anarchy']

    # In equilibrium with flow 1:
    # If f1 on link 1, then l1(f1) = f1 should equal l2(1-f1) = 1
    # So f1 = 1 (all on link 1 doesn't work), or split such that f1 = 1
    # Actually: l1(f1) = l2(f2) means f1 = 1 (constant), so f1 can be any value where f1 >= 1
    # Wait, if l2 = 1 always, then in equilibrium f1 such that f1 = 1, so f1 = 1, f2 = 0

    assert poa >= 1

    print(f"✓ Selfish routing PoA: {poa:.3f}")
    print(f"  Equilibrium latency: {eq_latency:.3f}")
    print(f"  Optimal latency: {opt_latency:.3f}")


def test_braess_paradox():
    """Test Braess's Paradox."""
    result = braess_paradox_network(flow=6)

    assert result is not None

    original = result['original_equilibrium_latency']
    new = result['new_equilibrium_latency']

    # Should demonstrate paradox
    if result.get('paradox', False):
        assert new > original, "New network should be worse (paradox)"

    print(f"✓ Braess's Paradox:")
    print(f"  Original: {original:.2f}")
    print(f"  With new link: {new:.2f}")
    print(f"  Paradox: {result['paradox']}")


def test_congestion_game():
    """Test congestion game PoA."""
    facilities = [
        {'capacity': 10, 'cost_func': lambda x: x},
        {'capacity': 10, 'cost_func': lambda x: x}
    ]

    poa = congestion_game_poa(num_players=20, facilities=facilities)

    assert poa is not None
    assert poa >= 1

    # For linear costs, PoA is bounded by 4/3
    assert poa <= 1.34, f"PoA {poa} exceeds theoretical bound for linear costs"

    print(f"✓ Congestion game PoA: {poa:.3f}")


if __name__ == "__main__":
    print("\n=== Price of Anarchy Tests ===\n")
    test_price_of_anarchy()
    test_selfish_routing()
    test_braess_paradox()
    test_congestion_game()
    print("\n🎉 All tests passed! You understand Price of Anarchy!")

    print("\n=== Key Insights ===")
    print("• PoA measures efficiency loss from selfish behavior")
    print("• PoA = 1 means equilibria are efficient (no loss)")
    print("• Braess's Paradox: adding capacity can hurt performance")
    print("• Selfish routing: users don't internalize congestion externality")
    print("• Congestion games with linear costs: PoA ≤ 4/3")
    print("• Design implication: need pricing/tolls to achieve optimum")
