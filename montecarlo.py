import random

class MCTSNode:
  def __init__(self, state, parent=None):
    self.state = state
    self.parent = parent
    self.children = []
    self.visits = 0
    self.wins = 0
  
  def select_child(self):
    max_ucb = -float('inf')
    best_child = None
    total_visits = sum(child.visits for child in self.children)
    for child in self.children:      
      win_rate = child.wins / child.visits
      exploration_factor = math.sqrt(2 * math.log(total_visits) / child.visits)
      ucb = win_rate + exploration_factor
      if ucb > max_ucb:
        max_ucb = ucb
        best_child = child
    return best_child
  
  def expand(self, legal_moves):
    for move in legal_moves:
      next_state = self.state.apply_move(move)
      child = MCTSNode(next_state, self)
      self.children.append(child)
  
  def backpropagate(self, result):
    self.visits += 1
    self.wins += result
    if self.parent:
      self.parent.backpropagate(result)


def monte_carlo_tree_search(state):
  root = MCTSNode(state)
  for _ in range(max_iterations):
    node = root
    while node.children:
      node = node.select_child()
    if node.state.is_game_over():
      result = node.state.get_result()
      node.backpropagate(result)
    else:
      legal_moves = node.state.get_legal_moves()
      node.expand(legal_moves)
      result = node.state.play_random_simulation()
      node.backpropagate(result)
  
  best_child = root.select_child()
  return best_child.state.last_move
