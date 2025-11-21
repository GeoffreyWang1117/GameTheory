"""
Exercise 12: Analyzing Tit-for-Tat

Tit-for-Tat (TFT) won Axelrod's tournaments despite its simplicity.
Let's understand why through analysis and variants.

TODO: Implement TFT variants and analyze their properties.
"""


class TitForTat:
    """Classic Tit-for-Tat strategy."""

    def __init__(self):
        self.opponent_history = []

    def choose(self):
        if not self.opponent_history:
            return 'C'
        return self.opponent_history[-1]

    def update(self, opponent_action):
        self.opponent_history.append(opponent_action)


class GenerousTitForTat:
    """
    Tit-for-Tat with occasional forgiveness.

    After opponent defects, sometimes cooperate anyway (with probability p).

    TODO: Implement Generous TFT.
    """

    def __init__(self, generosity=0.1):
        self.generosity = generosity
        self.opponent_history = []

    def choose(self):
        import random

        if not self.opponent_history:
            return 'C'

        last_opponent = self.opponent_history[-1]

        # TODO: If opponent defected, forgive with probability self.generosity
        if last_opponent == 'D':
            if random.random() < self.generosity:
                return 'C'  # Forgive
            return 'D'

        return 'C'

    def update(self, opponent_action):
        self.opponent_history.append(opponent_action)


class TitForTwoTats:
    """
    Only retaliates after TWO consecutive defections.
    More forgiving than TFT.

    TODO: Implement Tit-for-Two-Tats.
    """

    def __init__(self):
        self.opponent_history = []

    def choose(self):
        # TODO: Only defect if opponent defected in last TWO rounds
        if len(self.opponent_history) < 2:
            return 'C'

        if self.opponent_history[-1] == 'D' and self.opponent_history[-2] == 'D':
            return 'D'

        return 'C'

    def update(self, opponent_action):
        self.opponent_history.append(opponent_action)


class Pavlov:
    """
    Win-Stay, Lose-Shift strategy.

    - If last round was good (CC or DC), repeat same action
    - If last round was bad (DD or CD), switch action

    Also called "Simpleton" - surprisingly effective!

    TODO: Implement Pavlov/Win-Stay-Lose-Shift.
    """

    def __init__(self):
        self.my_history = []
        self.opponent_history = []

    def choose(self):
        if not self.my_history:
            return 'C'

        my_last = self.my_history[-1]
        opp_last = self.opponent_history[-1]

        # TODO: Implement Win-Stay, Lose-Shift logic
        # Win (good outcomes): CC or DC -> stay
        # Lose (bad outcomes): CD or DD -> shift

        if (my_last == 'C' and opp_last == 'C') or (my_last == 'D' and opp_last == 'C'):
            # Win: stay with current action
            return my_last
        else:
            # Lose: shift to other action
            return 'D' if my_last == 'C' else 'C'

    def update(self, my_action, opponent_action):
        self.my_history.append(my_action)
        self.opponent_history.append(opponent_action)


def simulate_matchup(strategy1, strategy2, rounds, payoff_matrix):
    """
    Simulate a matchup between two strategies.

    Args:
        strategy1, strategy2: Strategy objects
        rounds: Number of rounds
        payoff_matrix: Payoff matrix

    Returns:
        Tuple (score1, score2, cooperation_rate1, cooperation_rate2)

    TODO: Implement simulation with cooperation rate tracking.
    """
    score1 = 0
    score2 = 0
    coop_count1 = 0
    coop_count2 = 0

    for _ in range(rounds):
        # Get actions
        action1 = strategy1.choose()
        action2 = strategy2.choose()

        # Count cooperation
        if action1 == 'C':
            coop_count1 += 1
        if action2 == 'C':
            coop_count2 += 1

        # Get payoffs
        p1, p2 = payoff_matrix[(action1, action2)]
        score1 += p1
        score2 += p2

        # Update strategies
        if hasattr(strategy1, 'update'):
            if 'my_action' in strategy1.update.__code__.co_varnames:
                strategy1.update(action1, action2)
            else:
                strategy1.update(action2)

        if hasattr(strategy2, 'update'):
            if 'my_action' in strategy2.update.__code__.co_varnames:
                strategy2.update(action2, action1)
            else:
                strategy2.update(action1)

    coop_rate1 = coop_count1 / rounds
    coop_rate2 = coop_count2 / rounds

    return score1, score2, coop_rate1, coop_rate2


def analyze_strategy_properties(strategy_class, name):
    """
    Analyze key properties of a strategy:
    1. Nice: Doesn't defect first
    2. Retaliating: Punishes defection
    3. Forgiving: Cooperates again after punishment
    4. Envious: Tries to outscore opponent

    Args:
        strategy_class: Strategy class to analyze
        name: Name of the strategy

    Returns:
        Dictionary of properties

    TODO: Implement property analysis.
    """
    properties = {}

    # Test if nice (doesn't defect first)
    s = strategy_class()
    first_action = s.choose()
    properties['nice'] = (first_action == 'C')

    # Test if retaliating
    s = strategy_class()
    if hasattr(s, 'update'):
        if 'my_action' in s.update.__code__.co_varnames:
            s.update('C', 'D')
        else:
            s.update('D')
        response_to_defection = s.choose()
        properties['retaliating'] = (response_to_defection == 'D')
    else:
        properties['retaliating'] = False

    # Test if forgiving (will cooperate again after retaliating)
    s = strategy_class()
    if hasattr(s, 'update'):
        # Opponent defects, then cooperates
        if 'my_action' in s.update.__code__.co_varnames:
            s.update('C', 'D')
            s.choose()  # Retaliate
            s.update('D', 'C')
        else:
            s.update('D')
            s.choose()  # Retaliate
            s.update('C')
        response_to_return = s.choose()
        properties['forgiving'] = (response_to_return == 'C')
    else:
        properties['forgiving'] = False

    return properties


def test_solution():
    """Test function - Do not modify."""
    payoff_matrix = {
        ('C', 'C'): (3, 3),
        ('C', 'D'): (0, 5),
        ('D', 'C'): (5, 0),
        ('D', 'D'): (1, 1),
    }

    # Test Generous TFT
    gtft = GenerousTitForTat(generosity=0.0)  # With 0 generosity, should act like TFT
    gtft.update('D')
    assert gtft.choose() == 'D', "Should retaliate"

    # Test TitForTwoTats
    tf2t = TitForTwoTats()
    tf2t.update('D')
    assert tf2t.choose() == 'C', "Should not retaliate after single defection"
    tf2t.update('D')
    assert tf2t.choose() == 'D', "Should retaliate after two defections"

    # Test Pavlov
    pavlov = Pavlov()
    first = pavlov.choose()
    assert first == 'C', "Pavlov should start with cooperation"

    # Simulate matchups
    print("\nStrategy Matchups (100 rounds):")

    tft1 = TitForTat()
    tft2 = TitForTat()
    s1, s2, cr1, cr2 = simulate_matchup(tft1, tft2, 100, payoff_matrix)
    print(f"  TFT vs TFT: {s1} vs {s2}, cooperation: {cr1:.0%} vs {cr2:.0%}")

    gtft = GenerousTitForTat(0.1)
    tft = TitForTat()
    s1, s2, cr1, cr2 = simulate_matchup(gtft, tft, 100, payoff_matrix)
    print(f"  GTFT vs TFT: {s1} vs {s2}, cooperation: {cr1:.0%} vs {cr2:.0%}")

    # Analyze properties
    print("\nStrategy Properties:")
    for strategy_class, name in [
        (TitForTat, "Tit-for-Tat"),
        (GenerousTitForTat, "Generous TFT"),
        (TitForTwoTats, "Tit-for-Two-Tats"),
        (Pavlov, "Pavlov"),
    ]:
        props = analyze_strategy_properties(strategy_class, name)
        print(f"  {name}: Nice={props.get('nice', '?')}, "
              f"Retaliating={props.get('retaliating', '?')}, "
              f"Forgiving={props.get('forgiving', '?')}")

    print("\nKey insights:")
    print("1. TFT's success comes from being nice, retaliating, and forgiving")
    print("2. Generous TFT can recover from noise/mistakes better")
    print("3. Pavlov adapts to opponent's behavior dynamically")

    return True


if __name__ == '__main__':
    test_solution()
