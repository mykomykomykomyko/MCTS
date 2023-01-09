# Monte Carlo Tree Search

**Monte Carlo Tree Search (MCTS)** is a heuristic search algorithm that is used to find the best move in a two-player, turn-based, perfect-information game such as chess, Go, or tic-tac-toe. It works by constructing a tree of possible moves and using random simulations to evaluate the potential outcomes of each move.

# How does it work?

At each step, MCTS selects the next move to explore using a combination of the current win rate and the number of visits for each child node. This helps to balance the exploration of new moves with the exploitation of known good moves. MCTS is a form of best-first search, meaning that it prioritizes moves that are most likely to lead to a win.

MCTS is an iterative algorithm, meaning that it continually refines its search as it runs. It can be run for a fixed number of iterations or until a certain time limit is reached. The more iterations it is run for, the more accurate the search will be, but at the cost of increased computational time. MCTS has been very successful in a number of different games, and is often used as the primary search algorithm in modern chess engines. It can also be used in other settings where the goal is to find the best solution to a problem with a large search space, such as in decision-making tasks or optimization problems.

# *Pseudocode*:

The itself code is written in Python, so the pseudocode will be based on it.

```
function monte_carlo_tree_search(root_node)
  for i = 1 to max_iterations do
    node = root_node
    while node is not a leaf do
      node = select_child(node)
    if node is a leaf then
      expand(node)
    result = play_random_simulation(node)
    backpropagate(node, result)
  return best_child(root_node)

function select_child(node)
  best_score = -infinity
  best_child = null
  for each child in node.children do
    score = child.wins / child.visits + exploration_factor * sqrt(ln(node.visits) / child.visits)
    if score > best_score then
      best_score = score
      best_child = child
  return best_child

function expand(node)
  legal_moves = get_legal_moves(node.state)
  for each move in legal_moves do
    child_state = apply_move(node.state, move)
    child = MCTSNode(child_state, node)
    node.children.add(child)

function play_random_simulation(node)
  current_state = copy(node.state)
  while current_state is not terminal do
    move = random_move(current_state)
    current_state = apply_move(current_state, move)
  return get_result(current_state)

function backpropagate(node, result)
  node.visits = node.visits + 1
  node.wins = node.wins + result
  if node.parent is not null then
    backpropagate(node.parent, result)

function best_child(node)
  best_score = -infinity
  best_child = null
  for each child in node.children do
    score = child.wins / child.visits
    if score > best_score then
      best_score = score
      best_child = child
  return best_child

```

