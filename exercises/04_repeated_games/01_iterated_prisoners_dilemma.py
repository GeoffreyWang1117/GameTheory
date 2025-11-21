"""
Exercise 11: Iterated Prisoner's Dilemma

When the Prisoner's Dilemma is repeated multiple times, cooperation can emerge!
Players can punish defection and reward cooperation over time.

This was famously studied by Robert Axelrod's tournaments.

TODO: Implement strategies for iterated games.
"""


class Strategy:
    """Base class for IPD strategies."""

    def __init__(self, name):
        self.name = name
        self.reset()

    def reset(self):
        """Reset strategy state for a new game."""
        self.history = []
        self.opponent_history = []

    def choose_action(self):
        """
        Choose an action based on history.

        Returns:
            'C' for Cooperate or 'D' for Defect

        TODO: Implement in subclasses.
        """
        raise NotImplementedError

    def update_history(self, my_action, opponent_action):
        """Update history after a round."""
        self.history.append(my_action)
        self.opponent_history.append(opponent_action)


class AlwaysCooperate(Strategy):
    """Strategy that always cooperates."""

    def __init__(self):
        super().__init__("Always Cooperate")

    def choose_action(self):
        # TODO: Always return 'C'
        return 'C'


class AlwaysDefect(Strategy):
    """Strategy that always defects."""

    def __init__(self):
        super().__init__("Always Defect")

    def choose_action(self):
        # TODO: Always return 'D'
        return 'D'


class TitForTat(Strategy):
    """
    Strategy that copies opponent's last move.
    Starts with cooperation.
    """

    def __init__(self):
        super().__init__("Tit-for-Tat")

    def choose_action(self):
        # TODO: If first round, cooperate. Otherwise, copy opponent's last move.
        if not self.opponent_history:
            return 'C'
        return self.opponent_history[-1]


class Grudger(Strategy):
    """
    Cooperates until opponent defects once, then defects forever.
    """

    def __init__(self):
        super().__init__("Grudger")

    def choose_action(self):
        # TODO: Cooperate until seeing a defection, then always defect
        if 'D' in self.opponent_history:
            return 'D'
        return 'C'


class Random(Strategy):
    """Randomly cooperates or defects with 50% probability."""

    def __init__(self):
        super().__init__("Random")

    def choose_action(self):
        import random
        # TODO: Return 'C' or 'D' randomly
        return random.choice(['C', 'D'])


def play_round(strategy1, strategy2, payoff_matrix):
    """
    Play one round of the game.

    Args:
        strategy1: First player's strategy
        strategy2: Second player's strategy
        payoff_matrix: Dictionary mapping (action1, action2) -> (payoff1, payoff2)

    Returns:
        Tuple (payoff1, payoff2) for this round

    TODO: Implement a single round.
    """
    # TODO: Get actions from both strategies
    action1 = strategy1.choose_action()
    action2 = strategy2.choose_action()

    # Get payoffs
    payoff1, payoff2 = payoff_matrix[(action1, action2)]

    # Update histories
    strategy1.update_history(action1, action2)
    strategy2.update_history(action2, action1)

    return payoff1, payoff2


def play_iterated_game(strategy1, strategy2, num_rounds, payoff_matrix):
    """
    Play an iterated game for a fixed number of rounds.

    Args:
        strategy1: First player's strategy
        strategy2: Second player's strategy
        num_rounds: Number of rounds to play
        payoff_matrix: Payoff matrix

    Returns:
        Tuple (total_payoff1, total_payoff2)

    TODO: Implement the full iterated game.
    """
    # Reset strategies
    strategy1.reset()
    strategy2.reset()

    total1 = 0
    total2 = 0

    # TODO: Play num_rounds rounds
    for _ in range(num_rounds):
        payoff1, payoff2 = play_round(strategy1, strategy2, payoff_matrix)
        total1 += payoff1
        total2 += payoff2

    return total1, total2


def run_tournament(strategies, num_rounds, payoff_matrix):
    """
    Run a round-robin tournament where each strategy plays against all others.

    Args:
        strategies: List of Strategy objects
        num_rounds: Number of rounds per matchup
        payoff_matrix: Payoff matrix

    Returns:
        Dictionary mapping strategy name -> total score

    TODO: Implement round-robin tournament.
    """
    scores = {s.name: 0 for s in strategies}

    # TODO: Each strategy plays against every other strategy (including itself)
    for i, s1 in enumerate(strategies):
        for j, s2 in enumerate(strategies):
            score1, score2 = play_iterated_game(s1, s2, num_rounds, payoff_matrix)
            scores[s1.name] += score1

    return scores


def test_solution():
    """Test function - Do not modify."""
    # Standard Prisoner's Dilemma payoffs
    payoff_matrix = {
        ('C', 'C'): (3, 3),   # Reward for mutual cooperation
        ('C', 'D'): (0, 5),   # Sucker's payoff / Temptation
        ('D', 'C'): (5, 0),   # Temptation / Sucker's payoff
        ('D', 'D'): (1, 1),   # Punishment for mutual defection
    }

    # Test individual strategies
    tft = TitForTat()
    assert tft.choose_action() == 'C', "TFT should start with cooperation"

    tft.update_history('C', 'D')
    assert tft.choose_action() == 'D', "TFT should defect after opponent defects"

    # Test pairwise games
    tft1 = TitForTat()
    tft2 = TitForTat()
    score1, score2 = play_iterated_game(tft1, tft2, 10, payoff_matrix)
    assert score1 == 30 and score2 == 30, "Two TFT should cooperate fully"

    # TFT vs Always Defect
    tft = TitForTat()
    ad = AlwaysDefect()
    score1, score2 = play_iterated_game(tft, ad, 10, payoff_matrix)
    # TFT gets suckered once (0), then mutual defection (1*9 = 9) = 9 total
    # AD gets temptation once (5), then mutual defection (1*9 = 9) = 14 total
    assert score1 == 9, f"TFT should score 9, got {score1}"
    assert score2 == 14, f"AD should score 14, got {score2}"

    # Run tournament
    strategies = [
        AlwaysCooperate(),
        AlwaysDefect(),
        TitForTat(),
        Grudger(),
    ]

    scores = run_tournament(strategies, 100, payoff_matrix)

    print("\nTournament Results (100 rounds each matchup):")
    for strategy, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {strategy}: {score}")

    print("\nKey insights:")
    print("1. Cooperation can emerge in repeated games through reciprocity")
    print("2. Tit-for-Tat is simple, nice, retaliatory, and forgiving")
    print("3. The shadow of the future enables cooperation")

    return True


if __name__ == '__main__':
    test_solution()
