#a-star 
import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic cost from current node to goal node

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def heuristic(state, goal):
    # Heuristic function: manhattan distance between current state and goal state
    return abs(state - goal)

def get_neighbors(current_state, board):
    neighbors = []
    for i in range(1, 7):
        next_state = current_state + i
        if next_state <= len(board):
            if board[next_state] != -1:
                next_state = board[next_state]
            neighbors.append(next_state)
    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def astar(start, goal, board):
    open_set = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors(current_node.state, board):
            if neighbor_state in closed_set:
                continue

            g = current_node.g + 1  # Cost from start to neighbor is always 1
            h = heuristic(neighbor_state, goal)
            neighbor_node = Node(neighbor_state, current_node, g, h)

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

    return None

if __name__ == "__main__":
    # Example board: -1 indicates no ladder/snake, otherwise indicates the destination
    board = [-1] * 101
    board[3] = 15  # Snake
    board[11] = 25  # Ladder
    board[19] = 39  # Ladder
    board[31] = 55  # Ladder
    board[37] = 17  # Snake
    board[53] = 63  # Ladder
    board[61] = 38  # Snake
    board[73] = 82  # Ladder
    board[81] = 98  # Ladder
    board[87] = 49  # Snake
    board[91] = 72  # Snake

    start = 1
    goal = 100

    path = astar(start, goal, board)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")
