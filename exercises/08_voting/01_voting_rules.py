"""
Exercise 26: Voting Rules - Plurality, Borda Count, Condorcet

Different voting systems can produce different winners from the same preferences!

- Plurality: Most first-place votes wins
- Borda Count: Weighted scoring based on ranking
- Condorcet: Winner who beats all others pairwise

TODO: Implement and compare voting methods.
"""


def plurality_voting(preferences):
    """
    Determine winner by plurality (most first-place votes).

    Args:
        preferences: Dict {voter: [ranked list of candidates]}

    Returns:
        Winner (candidate with most first-place votes)

    TODO: Implement plurality voting.
    """
    votes = {}
    for voter, ranking in preferences.items():
        if ranking:
            first_choice = ranking[0]
            votes[first_choice] = votes.get(first_choice, 0) + 1
    
    if not votes:
        return None
    
    winner = max(votes.items(), key=lambda x: x[1])[0]
    return winner


def borda_count(preferences):
    """
    Determine winner by Borda count.
    """
    scores = {}
    for voter, ranking in preferences.items():
        n = len(ranking)
        for i, candidate in enumerate(ranking):
            points = n - i - 1
            scores[candidate] = scores.get(candidate, 0) + points
    
    if not scores:
        return None
    
    winner = max(scores.items(), key=lambda x: x[1])[0]
    return winner


def pairwise_comparison(cand1, cand2, preferences):
    """Compare two candidates head-to-head."""
    count = 0
    for voter, ranking in preferences.items():
        if cand1 in ranking and cand2 in ranking:
            if ranking.index(cand1) < ranking.index(cand2):
                count += 1
    return count


def condorcet_winner(preferences):
    """Find Condorcet winner if one exists."""
    all_candidates = set()
    for ranking in preferences.values():
        all_candidates.update(ranking)
    
    for candidate in all_candidates:
        is_condorcet_winner = True
        for other in all_candidates:
            if candidate == other:
                continue
            votes_for_candidate = pairwise_comparison(candidate, other, preferences)
            votes_for_other = pairwise_comparison(other, candidate, preferences)
            if votes_for_candidate <= votes_for_other:
                is_condorcet_winner = False
                break
        if is_condorcet_winner:
            return candidate
    
    return None


def test_solution():
    """Test function - Do not modify."""
    prefs = {
        'V1': ['A', 'B', 'C'],
        'V2': ['A', 'B', 'C'],
        'V3': ['B', 'C', 'A'],
    }
    
    p_winner = plurality_voting(prefs)
    b_winner = borda_count(prefs)
    c_winner = condorcet_winner(prefs)
    
    print(f"Plurality: {p_winner}, Borda: {b_winner}, Condorcet: {c_winner}")
    print("Different voting methods can produce different winners!")
    
    return True

if __name__ == '__main__':
    test_solution()
