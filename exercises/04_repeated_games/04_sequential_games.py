"""
Exercise 14: Sequential Games and Backward Induction

In sequential games, players move in turns. We solve these using backward induction:
start from the end and work backwards to find the subgame perfect equilibrium.

TODO: Implement game trees and backward induction.
"""


class GameNode:
    """Represents a node in a game tree."""

    def __init__(self, player, name=""):
        self.player = player  # Which player moves at this node (or None for terminal)
        self.name = name
        self.children = {}  # Maps action -> child node
        self.payoffs = None  # For terminal nodes: tuple of payoffs

    def add_child(self, action, child_node):
        """Add a child node for a given action."""
        self.children[action] = child_node

    def set_payoffs(self, payoffs):
        """Set payoffs for a terminal node."""
        self.payoffs = payoffs
        self.player = None  # Terminal nodes have no player

    def is_terminal(self):
        """Check if this is a terminal node."""
        return self.payoffs is not None


def backward_induction(node, player_index):
    """
    Solve a sequential game using backward induction.

    Args:
        node: Current GameNode
        player_index: Index of the player we're analyzing (0 or 1)

    Returns:
        Tuple (best_action, payoff) for the current player at this node

    TODO: Implement backward induction.
    HINT: Recursively solve subgames, working backwards from terminal nodes.
    """
    # Base case: terminal node
    if node.is_terminal():
        return None, node.payoffs[player_index]

    # Recursive case: find best action
    # TODO: For each possible action, recursively compute value
    # Choose action that maximizes current player's payoff

    # Determine which player moves at this node
    current_player = node.player

    best_action = None
    best_value = float('-inf') if current_player == player_index else float('inf')

    for action, child in node.children.items():
        _, value = backward_induction(child, player_index)

        # If it's our turn, maximize. If opponent's turn, they minimize our payoff
        if current_player == player_index:
            if value > best_value:
                best_value = value
                best_action = action
        else:
            # Opponent's move - they choose what's best for them
            _, opponent_value = backward_induction(child, current_player)
            # We need to think about what they'll actually choose
            pass

    # Actually, let's reconsider the approach
    # We should compute equilibrium path for each player

    best_action = None
    best_payoff = float('-inf')

    for action, child in node.children.items():
        _, payoff = backward_induction(child, player_index)

        # Current player chooses action that maximizes their own payoff
        if current_player == player_index:
            if payoff > best_payoff:
                best_payoff = payoff
                best_action = action
        else:
            # It's the other player's turn - they'll choose their best action
            # We need to see what that leads to for us
            other_player = 1 - player_index
            other_action, _ = backward_induction(child, other_player)
            # But we need to reconsider...

    # Cleaner approach: compute best response for current player
    if not node.children:
        return None, 0

    # Find the action that gives current player (node.player) the best payoff
    best_action = None
    best_payoff = float('-inf')

    for action, child in node.children.items():
        # Recursively solve the subgame
        _, payoff_from_child = backward_induction(child, node.player)

        if payoff_from_child > best_payoff:
            best_payoff = payoff_from_child
            best_action = action

    return best_action, best_payoff


def solve_game_tree(root):
    """
    Solve a game tree and return the equilibrium path.

    Args:
        root: Root node of the game tree

    Returns:
        Dictionary mapping player -> list of equilibrium actions

    TODO: Implement full game tree solution.
    """
    # Find equilibrium path by backward induction
    path = {0: [], 1: []}

    def find_path(node):
        if node.is_terminal():
            return node.payoffs

        # Find best action for current player
        best_action, _ = backward_induction(node, node.player)

        if best_action:
            path[node.player].append(best_action)

            # Continue down the equilibrium path
            return find_path(node.children[best_action])

        return None

    equilibrium_payoffs = find_path(root)

    return path, equilibrium_payoffs


def create_entry_game():
    """
    Create the Entry Game tree.

    Incumbent (player 0) decides: Fight or Accommodate
    Entrant (player 1) decides: Enter or Stay Out

    If Entrant stays out: (2, 0)
    If Entrant enters and Incumbent fights: (-1, -1)
    If Entrant enters and Incumbent accommodates: (1, 1)

    TODO: Build and return the game tree.
    """
    # Root: Entrant decides
    root = GameNode(player=1, name="Entrant")

    # Entrant chooses "Enter"
    enter_node = GameNode(player=0, name="Incumbent (after Enter)")
    root.add_child("Enter", enter_node)

    # If entered, Incumbent chooses Fight or Accommodate
    fight_node = GameNode(player=None, name="Fight outcome")
    fight_node.set_payoffs((-1, -1))  # (Incumbent, Entrant)
    enter_node.add_child("Fight", fight_node)

    accommodate_node = GameNode(player=None, name="Accommodate outcome")
    accommodate_node.set_payoffs((1, 1))
    enter_node.add_child("Accommodate", accommodate_node)

    # Entrant chooses "Stay Out"
    stay_out_node = GameNode(player=None, name="Stay Out outcome")
    stay_out_node.set_payoffs((2, 0))
    root.add_child("Stay Out", stay_out_node)

    return root


def test_solution():
    """Test function - Do not modify."""
    # Create and solve Entry Game
    game_tree = create_entry_game()

    # Solve using backward induction
    print("\nSolving Entry Game by Backward Induction:")
    print("Entrant decides: Enter or Stay Out")
    print("If Enter, Incumbent decides: Fight or Accommodate")
    print("\nPayoffs (Incumbent, Entrant):")
    print("  Enter + Fight: (-1, -1)")
    print("  Enter + Accommodate: (1, 1)")
    print("  Stay Out: (2, 0)")

    # At Incumbent's node (after Entry)
    incumbent_action, incumbent_payoff = backward_induction(
        game_tree.children["Enter"], player_index=0
    )
    print(f"\nIncumbent's best response to Entry: {incumbent_action}")
    print(f"  Gives Incumbent payoff: {incumbent_payoff}")

    assert incumbent_action == "Accommodate", "Incumbent should accommodate (1 > -1)"

    # At root (Entrant's decision)
    # Entrant anticipates Incumbent will accommodate
    path, payoffs = solve_game_tree(game_tree)
    print(f"\nSubgame Perfect Equilibrium:")
    print(f"  Entrant: {path[1]}")
    print(f"  Incumbent: {path[0]}")
    print(f"  Equilibrium payoffs: {payoffs}")

    print("\nKey insights:")
    print("1. Backward induction finds subgame perfect equilibrium")
    print("2. Incredible threats are eliminated (Incumbent won't actually fight)")
    print("3. Sequential games often have first-mover or second-mover advantage")

    return True


if __name__ == '__main__':
    test_solution()
