from collections import deque

def is_valid(state):
    m, c, boat = state
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

def successors(state):
    m, c, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    next_states = []
    for dm, dc in moves:
        if boat: new_state = (m - dm, c - dc, 0)
        else: new_state = (m + dm, c + dc, 1)
        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and is_valid(new_state):
            next_states.append(new_state)
    return next_states

def solve():
    queue, visited = deque([((3, 3, 1), [])]), set()
    while queue:
        (state, path) = queue.popleft()
        if state == (0, 0, 0): return path + [state]
        if state not in visited:
            visited.add(state)
            for next_state in successors(state):
                queue.append((next_state, path + [state]))
    return None

solution = solve()
print(solution)
