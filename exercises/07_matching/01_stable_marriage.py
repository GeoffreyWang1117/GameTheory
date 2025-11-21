"""
Exercise 23: Stable Marriage Problem

The Stable Marriage Problem: Match n men and n women where everyone has preferences.
A matching is STABLE if there's no (man, woman) pair who prefer each other over
their assigned partners.

Gale-Shapley Deferred Acceptance Algorithm (1962) always finds a stable matching!

Application: Medical residency matching, school choice, kidney exchange.

TODO: Implement the Gale-Shapley algorithm.
"""


def gale_shapley_algorithm(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley deferred acceptance algorithm.

    Men propose in order of preference. Women tentatively accept best proposal
    and reject others. Rejected men propose to next choice. Repeat until all matched.

    Args:
        men_preferences: Dict {man: [ordered list of women preferences]}
        women_preferences: Dict {woman: [ordered list of men preferences]}

    Returns:
        Dict {man: woman} representing the stable matching

    TODO: Implement Gale-Shapley algorithm.
    """
    # Initialize
    free_men = list(men_preferences.keys())
    engaged = {}  # woman -> man  engagements
    proposals_made = {man: 0 for man in men_preferences}  # track proposals

    # TODO: Implement Gale-Shapley algorithm
    while free_men:
        man = free_men.pop(0)

        # Find next woman this man hasn't proposed to yet
        if proposals_made[man] >= len(men_preferences[man]):
            # This man has proposed to everyone (shouldn't happen with valid input)
            continue

        woman = men_preferences[man][proposals_made[man]]
        proposals_made[man] += 1

        if woman not in engaged:
            # Woman is free, accept proposal
            engaged[woman] = man
        else:
            # Woman is engaged, compare with current partner
            current_partner = engaged[woman]

            # Check woman's preference
            woman_pref = women_preferences[woman]

            if woman_pref.index(man) < woman_pref.index(current_partner):
                # Woman prefers new proposer
                engaged[woman] = man
                free_men.append(current_partner)  # Old partner becomes free
            else:
                # Woman prefers current partner, reject new proposal
                free_men.append(man)

    # Convert to man -> woman mapping
    matching = {man: woman for woman, man in engaged.items()}

    return matching


def is_stable_matching(matching, men_pref, women_pref):
    """
    Check if a matching is stable.

    A matching is stable if there's no blocking pair: a (man, woman) who:
    1. Are not matched to each other
    2. Both prefer each other to their current partners

    Args:
        matching: Dict {man: woman}
        men_pref: Men's preferences
        women_pref: Women's preferences

    Returns:
        Tuple (is_stable, blocking_pairs)

    TODO: Check stability.
    """
    blocking_pairs = []

    # Reverse matching for easy lookup
    reverse_matching = {woman: man for man, woman in matching.items()}

    # TODO: Check all possible pairs for blocking
    for man in men_pref:
        current_woman = matching[man]
        man_preferences = men_pref[man]

        # Check all women this man prefers over current partner
        for woman in man_preferences:
            if woman == current_woman:
                break  # No more preferred women

            # Would this woman also prefer this man?
            current_man_of_woman = reverse_matching.get(woman)

            if current_man_of_woman is None:
                continue

            woman_preferences = women_pref[woman]

            if woman_preferences.index(man) < woman_preferences.index(current_man_of_woman):
                # This is a blocking pair!
                blocking_pairs.append((man, woman))

    is_stable = len(blocking_pairs) == 0

    return is_stable, blocking_pairs


def proposer_optimal_property(men_pref, women_pref):
    """
    Demonstrate that Gale-Shapley produces proposer-optimal stable matching.

    The matching is optimal for proposers (men) among all stable matchings.
    Each man gets the best partner he can have in ANY stable matching.

    It's also pessimal for receivers (women) - worst stable matching for them.

    Args:
        men_pref: Men's preferences
        women_pref: Women's preferences

    Returns:
        Analysis of optimality

    TODO: Analyze proposer-optimality.
    """
    # Find stable matching with men proposing
    matching_men_propose = gale_shapley_algorithm(men_pref, women_pref)

    # Find stable matching with women proposing (swap roles)
    matching_women_propose = gale_shapley_algorithm(women_pref, men_pref)
    # Reverse to get man -> woman format
    matching_women_propose = {woman: man for man, woman in matching_women_propose.items()}

    analysis = {
        'men_propose': matching_men_propose,
        'women_propose': matching_women_propose,
        'property': 'Men-proposing gives men-optimal, women-pessimal stable matching'
    }

    return analysis


def count_stable_matchings_small(men_pref, women_pref):
    """
    For small instances, enumerate all matchings and count stable ones.

    This demonstrates that stable matchings may not be unique!

    Args:
        men_pref: Men's preferences (small instance)
        women_pref: Women's preferences

    Returns:
        List of all stable matchings

    TODO: Enumerate and check all possible matchings.
    """
    from itertools import permutations

    men = list(men_pref.keys())
    women = list(women_pref.keys())

    stable_matchings = []

    # TODO: Generate all possible matchings
    for women_perm in permutations(women):
        # Create matching
        matching = {men[i]: women_perm[i] for i in range(len(men))}

        # Check if stable
        is_stable, _ = is_stable_matching(matching, men_pref, women_pref)

        if is_stable:
            stable_matchings.append(matching)

    return stable_matchings


def test_solution():
    """Test function - Do not modify."""
    # Simple example with 3 men and 3 women
    men_pref = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'X', 'Z'],
        'C': ['X', 'Y', 'Z'],
    }

    women_pref = {
        'X': ['B', 'A', 'C'],
        'Y': ['A', 'B', 'C'],
        'Z': ['A', 'B', 'C'],
    }

    # Run Gale-Shapley
    matching = gale_shapley_algorithm(men_pref, women_pref)

    print("Stable Matching (men proposing):")
    for man, woman in sorted(matching.items()):
        print(f"  {man} - {woman}")

    # Check stability
    is_stable, blocking = is_stable_matching(matching, men_pref, women_pref)

    assert is_stable == True, f"Gale-Shapley should produce stable matching, but found blocking pairs: {blocking}"

    # Test with a known unstable matching
    unstable_matching = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    }

    is_stable_test, blocking_test = is_stable_matching(unstable_matching, men_pref, women_pref)

    print(f"\nTest unstable matching: {unstable_matching}")
    print(f"  Is stable: {is_stable_test}")
    if not is_stable_test:
        print(f"  Blocking pairs: {blocking_test}")

    assert is_stable_test == False, "Should detect instability"

    # Test proposer-optimality
    analysis = proposer_optimal_property(men_pref, women_pref)

    print(f"\nProposer-Optimality:")
    print(f"  Men propose: {analysis['men_propose']}")
    print(f"  Women propose: {analysis['women_propose']}")

    # The matchings may differ, showing different stable matchings exist
    if analysis['men_propose'] != analysis['women_propose']:
        print("  Different stable matchings exist!")

    # Count all stable matchings for small example
    all_stable = count_stable_matchings_small(men_pref, women_pref)

    print(f"\nTotal number of stable matchings: {len(all_stable)}")
    for i, sm in enumerate(all_stable):
        print(f"  Stable matching {i+1}: {sm}")

    print("\nKey insights:")
    print("1. Gale-Shapley always finds a stable matching")
    print("2. Stable matchings always exist")
    print("3. The matching is optimal for proposing side")
    print("4. Multiple stable matchings may exist")
    print("5. Algorithm runs in O(n²) time")

    return True


if __name__ == '__main__':
    test_solution()
