import heapq

class Node:
    def __init__(self, state, parent, move, cost, heuristic):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost  # g(n)
        self.heuristic = heuristic  # h(n)

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

def manhattan_distance(state, goal):
    distance = 0
    goal_positions = {goal[i][j]: (i, j) for i in range(3) for j in range(3)}
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = goal_positions[state[i][j]]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    neighbors = []
    if x > 0:
        neighbors.append((x - 1, y))
    if x < 2:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < 2:
        neighbors.append((x, y + 1))
    return neighbors

def apply_move(state, x, y, new_x, new_y):
    new_state = [list(row) for row in state]
    new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
    return new_state

def a_star(start, goal):
    open_list = []
    closed_set = set()
    start_node = Node(start, None, None, 0, manhattan_distance(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal:
            return reconstruct_path(current_node)

        closed_set.add(tuple(map(tuple, current_node.state)))

        for (new_x, new_y) in get_neighbors(current_node.state):
            x, y = next((i, j) for i in range(3) for j in range(3) if current_node.state[i][j] == 0)
            new_state = apply_move(current_node.state, x, y, new_x, new_y)
            if tuple(map(tuple, new_state)) not in closed_set:
                new_node = Node(new_state, current_node, (x, y, new_x, new_y), current_node.cost + 1, manhattan_distance(new_state, goal))
                heapq.heappush(open_list, new_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def get_puzzle_input(prompt):
    print(prompt)
    return [[int(x) for x in input(f'Enter row {i + 1} (three numbers separated by spaces): ').split()] for i in range(3)]

def print_solution(solution):
    if solution:
        print("Solution found:")
        for state in solution:
            for row in state:
                print(' '.join(str(x) for x in row))
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    start_state = get_puzzle_input("Enter the start state (use 0 for blank):")
    goal_state = get_puzzle_input("Enter the goal state (use 0 for blank):")
    if sorted(sum(start_state, [])) != sorted(sum(goal_state, [])) == list(range(9)):
        print("Invalid input: each number from 0 to 8 must appear exactly once.")
    else:
        solution = a_star(start_state, goal_state)
        print_solution(solution)
