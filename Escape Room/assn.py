import random
from collections import deque
import numpy as np

GOAL = 8                             # goal state
N = 9                                # number of states
GAMMA = 0.85
WALL, DOOR, FREEDOM = -10, -1, 100

DOORS = [(0,1),(1,2),(2,8),(2,3),(3,4),(3,6),(4,5),(5,8),(5,6),(6,7),(8,8)]
R = np.full((N, N), WALL)
Q = np.zeros((N, N), dtype=float)

for a, b in DOORS:
    for i,j in [(a,b), (b,a)]:
        R[i][j] = FREEDOM if j == GOAL else DOOR

def episode(current_state):
    while True:
        action = random.randrange(N)

        # set next state if the agent is not hitting a wall
        next_state = current_state if R[current_state][action] == WALL else action
        if next_state == GOAL:
            Q[current_state][action] = R[current_state][action]
        else:
            Q[current_state][action] = (R[current_state][action]
            + GAMMA * Q[next_state].max())

        if current_state == GOAL:
            return
            
        current_state = next_state


for _ in range(1000):
    episode(random.randrange(N))

def model_path(current_state):
    path = [current_state]
    while current_state != GOAL and len(path) <= N:
        current_state = int(np.argmax(Q[current_state]))
        path.append(current_state)
    return path

def bfs_path(start):
    prev = {start: None}
    q = deque([start])
    while q:
        current = q.popleft()
        if current == GOAL:
            break
        for nxt in range(N):
            if R[current][nxt] in (DOOR, FREEDOM) and nxt not in prev:
                prev[nxt] = current
                q.append(nxt)
    path, current = [], GOAL
    while current is not None:
        path.append(current)
        current = prev[current]
    return path[::-1]

fmt = lambda p:" -> ".join("out" if x == GOAL else str(x + 1) for x in p)
for room in range(N):
    a, b = model_path(room), bfs_path(room)
    print(f"Room {room+1}: agent [{fmt(a)}]  BFS [{fmt(b)}]  {'OK' if a == b else 'MISMATCH'}")
