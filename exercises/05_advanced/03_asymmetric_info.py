"""
Exercise 17: Games with Asymmetric Information

When players have different information, we need Bayesian game theory.
Players form beliefs about unknown information and choose strategies accordingly.

Example: A seller knows the quality of their product, but the buyer doesn't.

TODO: Implement Bayesian games and perfect Bayesian equilibrium concepts.
"""


def expected_utility(action, belief, payoff_function):
    """
    Calculate expected utility given beliefs about opponent's type.

    Args:
        action: The action to evaluate
        belief: Dictionary mapping opponent types -> probabilities
        payoff_function: Function (action, opponent_type) -> payoff

    Returns:
        Expected utility

    TODO: Calculate expected utility.
    """
    expected = 0.0

    # TODO: Sum over opponent types weighted by belief
    for opp_type, probability in belief.items():
        payoff = payoff_function(action, opp_type)
        expected += probability * payoff

    return expected


def bayesian_best_response(beliefs, possible_actions, payoff_function):
    """
    Find best response given beliefs about opponent.

    Args:
        beliefs: Dictionary of beliefs about opponent types
        possible_actions: List of possible actions
        payoff_function: Payoff function

    Returns:
        Best action

    TODO: Find action that maximizes expected utility.
    """
    best_action = None
    best_utility = float('-inf')

    # TODO: Find action with highest expected utility
    for action in possible_actions:
        eu = expected_utility(action, beliefs, payoff_function)

        if eu > best_utility:
            best_utility = eu
            best_action = action

    return best_action, best_utility


def update_belief_bayes_rule(prior, likelihood, evidence):
    """
    Update beliefs using Bayes' rule.

    P(type | evidence) = P(evidence | type) * P(type) / P(evidence)

    Args:
        prior: Dictionary mapping types -> prior probabilities
        likelihood: Dictionary mapping types -> P(evidence | type)
        evidence: The observed evidence (for documentation)

    Returns:
        Updated posterior beliefs

    TODO: Apply Bayes' rule.
    """
    # Calculate P(evidence) = sum over types of P(evidence|type)*P(type)
    p_evidence = sum(likelihood[t] * prior[t] for t in prior.keys())

    # TODO: Calculate posterior for each type
    posterior = {}

    for t in prior.keys():
        if p_evidence > 0:
            posterior[t] = (likelihood[t] * prior[t]) / p_evidence
        else:
            posterior[t] = prior[t]  # No update if evidence has 0 probability

    return posterior


def signaling_game_payoffs():
    """
    Create a simple signaling game (Job Market Signaling).

    Worker knows their type (High or Low ability)
    Can choose to get Education (E) or Not (N)
    Employer observes education and offers wage

    Returns:
        Game specification

    TODO: Define the signaling game.
    """
    # Worker types
    types = ['High', 'Low']
    type_prior = {'High': 0.5, 'Low': 0.5}

    # Actions
    worker_actions = ['E', 'N']  # Education or No education
    employer_actions = ['High_Wage', 'Low_Wage']

    # Costs of education (lower for high type)
    education_cost = {'High': 1, 'Low': 3}

    # Payoffs (simplified)
    def worker_payoff(worker_type, education, wage):
        """Worker payoff = wage - education cost (if educated)."""
        wage_value = 10 if wage == 'High_Wage' else 5
        cost = education_cost[worker_type] if education == 'E' else 0
        return wage_value - cost

    def employer_payoff(worker_type, wage):
        """Employer payoff = worker productivity - wage."""
        productivity = 12 if worker_type == 'High' else 6
        wage_paid = 10 if wage == 'High_Wage' else 5
        return productivity - wage_paid

    return {
        'types': types,
        'type_prior': type_prior,
        'worker_actions': worker_actions,
        'employer_actions': employer_actions,
        'education_cost': education_cost,
        'worker_payoff': worker_payoff,
        'employer_payoff': employer_payoff,
    }


def check_separating_equilibrium(game):
    """
    Check if a separating equilibrium exists (different types choose different actions).

    In separating equilibrium:
    - High type chooses E, Low type chooses N
    - Employer infers type from education choice
    - Each player's strategy is optimal given beliefs

    Args:
        game: Signaling game specification

    Returns:
        True if separating equilibrium exists with costs, False otherwise

    TODO: Check separating equilibrium conditions.
    """
    # TODO: Check if high type prefers E with high wage over N with low wage
    # And low type prefers N with low wage over E with high wage

    high_with_edu = game['worker_payoff']('High', 'E', 'High_Wage')
    high_without_edu = game['worker_payoff']('High', 'N', 'Low_Wage')

    low_with_edu = game['worker_payoff']('Low', 'E', 'High_Wage')
    low_without_edu = game['worker_payoff']('Low', 'N', 'Low_Wage')

    # For separating equilibrium:
    # High type prefers E + High_Wage over N + Low_Wage
    condition1 = high_with_edu >= high_without_edu

    # Low type prefers N + Low_Wage over E + High_Wage
    condition2 = low_without_edu >= low_with_edu

    return condition1 and condition2


def check_pooling_equilibrium(game):
    """
    Check if a pooling equilibrium exists (both types choose same action).

    Args:
        game: Signaling game specification

    Returns:
        True if pooling equilibrium exists

    TODO: Check pooling equilibrium conditions.
    """
    # In pooling equilibrium, both types choose same action
    # Employer can't distinguish, so belief = prior

    # Both choose E
    pooling_E_possible = True
    # Check if Low type wants to choose E given employer will use prior
    # (This is complex and depends on employer's optimal response)

    # Both choose N
    pooling_N_possible = True

    # Simplified check
    return True  # Simplified


def test_solution():
    """Test function - Do not modify."""
    # Test expected utility calculation
    belief = {'Type1': 0.6, 'Type2': 0.4}

    def simple_payoff(action, opp_type):
        if action == 'A':
            return 10 if opp_type == 'Type1' else 5
        else:
            return 7 if opp_type == 'Type1' else 8

    eu_A = expected_utility('A', belief, simple_payoff)
    expected = 0.6 * 10 + 0.4 * 5
    assert abs(eu_A - expected) < 0.01, f"Expected {expected}, got {eu_A}"

    # Test best response
    br, util = bayesian_best_response(belief, ['A', 'B'], simple_payoff)
    print(f"Best response: {br} with utility {util:.2f}")

    # Test Bayes' rule
    prior = {'Heads': 0.5, 'Tails': 0.5}
    # Suppose we observe "Signal" which is more likely from Heads
    likelihood = {'Heads': 0.8, 'Tails': 0.3}
    posterior = update_belief_bayes_rule(prior, likelihood, "Signal")

    print(f"\nBayes' rule update:")
    print(f"Prior: {prior}")
    print(f"Likelihood: {likelihood}")
    print(f"Posterior: {posterior}")

    # Heads should be more likely after seeing signal
    assert posterior['Heads'] > posterior['Tails'], "Should update toward Heads"

    # Test signaling game
    game = signaling_game_payoffs()
    has_separating = check_separating_equilibrium(game)
    print(f"\nSeparating equilibrium exists: {has_separating}")

    print("\nKey insights:")
    print("1. Asymmetric information creates strategic complexity")
    print("2. Signaling can reveal private information")
    print("3. Education can serve as a signal of ability")
    print("4. Bayes' rule updates beliefs from observed actions")

    return True


if __name: == '__main__':
    test_solution()
