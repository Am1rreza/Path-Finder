import curses
from curses import wrapper
import queue
import time

# Define the maze as a global variable
MAZE = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# Constants for start and end points
START = "O"
END = "X"


def initialize_curses():
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            color = RED if (i, j) in path else BLUE
            stdscr.addstr(i, j * 2, value if (i, j)
                          not in path else 'X', color)


def find_start(maze, start_symbol):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_symbol:
                return i, j
    return None


def find_neighbors(maze, row, col):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]):
            neighbors.append((r, c))

    return neighbors


def find_path(maze, stdscr):
    start_pos = find_start(maze, START)
    if start_pos is None:
        return []

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == END:
            return path

        for neighbor in find_neighbors(maze, row, col):
            if neighbor not in visited:
                r, c = neighbor
                if maze[r][c] != "#":
                    visited.add(neighbor)
                    q.put((neighbor, path + [neighbor]))

    return []


def main(stdscr):
    initialize_curses()
    path = find_path(MAZE, stdscr)
    stdscr.getch()


wrapper(main)
