# Function to check if the state is valid
def is_valid(state):
    farmer, goat, wolf, cabbage = state
    # Check for invalid states based on the rules
    if (wolf == goat and farmer != wolf) or (goat == cabbage and farmer != goat):
        return False
    return True

# Function to generate possible moves
def generate_moves(state):
    moves = []
    farmer, goat, wolf, cabbage = state
    # Possible movements of the farmer
    possible_farmer_moves = [0, 1]
    for move in possible_farmer_moves:
        new_farmer = farmer ^ move
        for passenger in range(4):
            # Exclude illegal states
            if passenger != farmer:
                new_state = (new_farmer, goat, wolf, cabbage)
                new_state = list(new_state)
                new_state[passenger] = 1 - new_state[passenger]
                new_state = tuple(new_state)
                moves.append(new_state)
    return moves

# Depth-First Search algorithm with step-wise output
def depth_first_search(current_state, visited, actions):
    visited.add(current_state)
    if all(item == 1 for item in current_state):
        return actions

    possible_moves = generate_moves(current_state)
    for move in possible_moves:
        if move not in visited and is_valid(move):
            print("Step:", move)  # Output each step
            result = depth_first_search(move, visited, actions + [move])
            if result:
                return result
    return None

# Starting state and solving the problem using DFS
start_state = (0, 0, 0, 0)
visited = set()
dfs_solution = depth_first_search(start_state, visited, [start_state])

if dfs_solution:
    print("\nFinal Solution:")
    for move in dfs_solution:
        print(move)
else:
    print("DFS Solution not found.")
