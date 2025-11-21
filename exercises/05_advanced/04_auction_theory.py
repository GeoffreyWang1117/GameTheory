"""
Exercise 18: Auction Theory

Auctions are mechanisms for allocating resources. Different auction formats
lead to different strategic behavior and outcomes.

Types of auctions:
- First-price sealed-bid: Highest bidder wins, pays their bid
- Second-price (Vickrey): Highest bidder wins, pays second-highest bid
- English (ascending): Price rises until one bidder remains
- Dutch (descending): Price falls until someone accepts

TODO: Implement auction mechanisms and analyze bidding strategies.
"""


def second_price_auction(bids):
    """
    Run a second-price (Vickrey) auction.

    Args:
        bids: Dictionary mapping bidder -> bid value

    Returns:
        Tuple (winner, price_paid)

    TODO: Implement second-price auction.
    """
    if not bids:
        return None, 0

    # TODO: Find highest bidder and second-highest bid
    sorted_bids = sorted(bids.items(), key=lambda x: x[1], reverse=True)

    winner = sorted_bids[0][0]
    price = sorted_bids[1][1] if len(sorted_bids) > 1 else sorted_bids[0][1]

    return winner, price


def first_price_auction(bids):
    """
    Run a first-price sealed-bid auction.

    Args:
        bids: Dictionary mapping bidder -> bid value

    Returns:
        Tuple (winner, price_paid)

    TODO: Implement first-price auction.
    """
    if not bids:
        return None, 0

    # TODO: Find highest bidder
    winner = max(bids.items(), key=lambda x: x[1])

    return winner[0], winner[1]


def optimal_bid_second_price(true_value):
    """
    Find optimal bid in second-price auction.

    In second-price auction, it's dominant strategy to bid your true value!

    Args:
        true_value: Bidder's true valuation

    Returns:
        Optimal bid

    TODO: Return optimal bid.
    """
    # TODO: In second-price auction, truthful bidding is dominant
    return true_value


def optimal_bid_first_price(true_value, num_bidders, value_distribution='uniform'):
    """
    Find optimal bid in first-price auction (simplified).

    With symmetric risk-neutral bidders with values uniform on [0, v_max],
    optimal bid is: b(v) = (n-1)/n * v

    Args:
        true_value: Bidder's true valuation
        num_bidders: Total number of bidders
        value_distribution: Type of value distribution

    Returns:
        Optimal bid

    TODO: Calculate optimal shaded bid.
    """
    if value_distribution == 'uniform':
        # TODO: With n bidders, bid (n-1)/n of your value
        n = num_bidders
        optimal = ((n - 1) / n) * true_value
        return optimal

    return true_value * 0.7  # Rough heuristic


def revenue_equivalence(values, num_bidders, auction_type='second_price'):
    """
    Calculate expected revenue for different auction types.

    Revenue Equivalence Theorem: With symmetric, risk-neutral bidders,
    all standard auction formats yield the same expected revenue.

    Args:
        values: List of bidder valuations
        num_bidders: Number of bidders
        auction_type: Type of auction

    Returns:
        Expected revenue

    TODO: Calculate expected revenue.
    """
    if not values:
        return 0

    sorted_values = sorted(values, reverse=True)

    if auction_type == 'second_price':
        # Winner pays second-highest value
        revenue = sorted_values[1] if len(sorted_values) > 1 else sorted_values[0]

    elif auction_type == 'first_price':
        # With optimal bidding, expected revenue equals second-highest value
        # (by revenue equivalence)
        revenue = sorted_values[1] if len(sorted_values) > 1 else sorted_values[0]

    else:
        revenue = sorted_values[1] if len(sorted_values) > 1 else sorted_values[0]

    return revenue


def analyze_auction_efficiency(values, bids, auction_type):
    """
    Analyze if auction is efficient (allocates to highest-value bidder).

    Args:
        values: Dictionary mapping bidder -> true value
        bids: Dictionary mapping bidder -> bid
        auction_type: Type of auction

    Returns:
        Dictionary with efficiency analysis

    TODO: Analyze efficiency.
    """
    # Run auction
    if auction_type == 'second_price':
        winner, price = second_price_auction(bids)
    else:
        winner, price = first_price_auction(bids)

    # Find bidder with highest value
    highest_value_bidder = max(values.items(), key=lambda x: x[1])[0]

    # Check efficiency
    is_efficient = (winner == highest_value_bidder)

    # Calculate welfare
    winner_surplus = values[winner] - price if winner else 0
    seller_revenue = price

    return {
        'winner': winner,
        'price': price,
        'is_efficient': is_efficient,
        'winner_surplus': winner_surplus,
        'seller_revenue': seller_revenue,
        'total_welfare': winner_surplus + seller_revenue,
    }


def test_solution():
    """Test function - Do not modify."""
    # Test second-price auction
    bids = {'Alice': 100, 'Bob': 80, 'Charlie': 90}
    winner, price = second_price_auction(bids)

    print("Second-Price Auction:")
    print(f"  Bids: {bids}")
    print(f"  Winner: {winner}, Pays: {price}")

    assert winner == 'Alice', "Highest bidder should win"
    assert price == 90, "Should pay second-highest bid"

    # Test optimal bidding in second-price
    true_value = 100
    optimal = optimal_bid_second_price(true_value)
    assert optimal == true_value, "Should bid true value in second-price auction"

    # Test optimal bidding in first-price
    optimal_fp = optimal_bid_first_price(100, num_bidders=3)
    print(f"\nFirst-Price Auction:")
    print(f"  True value: 100")
    print(f"  Optimal bid with 3 bidders: {optimal_fp:.2f}")
    assert optimal_fp < 100, "Should shade bid below true value in first-price"
    assert abs(optimal_fp - 66.67) < 1, "With 3 bidders, should bid (2/3)*value"

    # Test efficiency
    values = {'Alice': 100, 'Bob': 80, 'Charlie': 90}
    bids_truthful = {'Alice': 100, 'Bob': 80, 'Charlie': 90}

    analysis = analyze_auction_efficiency(values, bids_truthful, 'second_price')
    print(f"\nEfficiency Analysis:")
    print(f"  Winner: {analysis['winner']}")
    print(f"  Efficient: {analysis['is_efficient']}")
    print(f"  Winner surplus: {analysis['winner_surplus']}")
    print(f"  Seller revenue: {analysis['seller_revenue']}")

    assert analysis['is_efficient'] == True, "Should be efficient"

    # Test revenue equivalence
    rev_sp = revenue_equivalence([100, 80, 90], 3, 'second_price')
    rev_fp = revenue_equivalence([100, 80, 90], 3, 'first_price')
    print(f"\nRevenue Equivalence:")
    print(f"  Second-price expected revenue: {rev_sp}")
    print(f"  First-price expected revenue: {rev_fp}")

    print("\nKey insights:")
    print("1. Second-price auction: Truthful bidding is dominant strategy")
    print("2. First-price auction: Bid shading is optimal")
    print("3. Revenue Equivalence: Different formats can yield same expected revenue")
    print("4. Efficiency: Standard auctions allocate to highest-value bidder")

    return True


if __name__ == '__main__':
    test_solution()
