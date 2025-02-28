from collections import deque

# Define the state of the problem
class State:
    def __init__(self, m, c, boat, m_goal=3, c_goal=3):
        # m: number of missionaries on the starting side
        # c: number of cannibals on the starting side
        # boat: 1 if the boat is on the starting side, 0 if it is on the goal side
        self.m = m
        self.c = c
        self.boat = boat
        self.m_goal = m_goal
        self.c_goal = c_goal

    def is_valid(self):
        # The number of missionaries and cannibals on either side should never allow cannibals
        # to outnumber missionaries, unless there are no missionaries on that side.
        if self.m < 0 or self.c < 0 or self.m > self.m_goal or self.c > self.c_goal:
            return False
        if (self.m > 0 and self.m < self.c) or (self.m_goal - self.m > 0 and self.m_goal - self.m < self.c_goal - self.c):
            return False
        return True

    def is_goal(self):
        # The goal is when all missionaries and cannibals are on the other side
        return self.m == 0 and self.c == 0

    def __repr__(self):
        return f"State(M={self.m}, C={self.c}, Boat={'Start' if self.boat == 1 else 'Goal'})"

# Possible boat moves
def possible_moves(state):
    moves = []
    # Boat can carry one or two people, so check combinations of moves
    if state.boat == 1:
        # Boat is on the starting side (1), can move missionaries (M) or cannibals (C)
        # and combinations of them
        if state.m > 0:
            moves.append(State(state.m - 1, state.c, 0))  # 1 missionary
        if state.c > 0:
            moves.append(State(state.m, state.c - 1, 0))  # 1 cannibal
        if state.m > 1:
            moves.append(State(state.m - 2, state.c, 0))  # 2 missionaries
        if state.c > 1:
            moves.append(State(state.m, state.c - 2, 0))  # 2 cannibals
        if state.m > 0 and state.c > 0:
            moves.append(State(state.m - 1, state.c - 1, 0))  # 1 missionary and 1 cannibal
    else:
        # Boat is on the goal side (0), can move missionaries or cannibals back
        if state.m < state.m_goal:
            moves.append(State(state.m + 1, state.c, 1))  # 1 missionary
        if state.c < state.c_goal:
            moves.append(State(state.m, state.c + 1, 1))  # 1 cannibal
        if state.m < state.m_goal - 1:
            moves.append(State(state.m + 2, state.c, 1))  # 2 missionaries
        if state.c < state.c_goal - 1:
            moves.append(State(state.m, state.c + 2, 1))  # 2 cannibals
        if state.m < state.m_goal and state.c < state.c_goal:
            moves.append(State(state.m + 1, state.c + 1, 1))  # 1 missionary and 1 cannibal

    return [move for move in moves if move.is_valid()]

# BFS Search to find the solution
def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])  # (state, path to get to that state)

    while queue:
        state, 
