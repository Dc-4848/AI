from collections import deque
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1
def generate_new_states(state):
    x, y = find_zero(state)
    new_states = []

    for dx, dy in MOVES:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state] 
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            new_states.append(new_state)
    return new_states
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)
def bfs(initial_state):
    queue = deque([(initial_state, [])])  
    visited = set() 
    visited.add(state_to_tuple(initial_state))
    while queue:
        current_state, path = queue.popleft()
        if current_state == GOAL_STATE:
            return path
        for new_state in generate_new_states(current_state):
            new_state_tuple = state_to_tuple(new_state)
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state, path + [new_state]))

    return None  
if __name__== "__main__":
    initial_state = [
        [1, 2, 3],
        [0, 4, 5],
        [7, 8, 6]
    ]
    
    solution = bfs(initial_state)
    
    if solution:
        print("Solution found!")
        for step in solution:
            for row in step:
                print(row)
            print()  
    else:
        print("No solution found.")
