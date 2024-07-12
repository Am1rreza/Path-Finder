"""
This module provides utilities for navigating and visualizing a maze using curses.

It includes functions to print a maze, find the start position, find a path through the maze,
initialize curses, and handle navigation logic.

Author: Your Name
Version: 1.0
"""

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
    """
    Initialize the curses environment.

    Sets up the color pairs used for displaying the maze.
    """
    curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


def print_maze(maze, stdscr, path=[]):
    """
    Print the maze to the given curses window.

    Args:
        maze (list): A 2D list representing the maze.
        stdscr: The curses window object where the maze is displayed.
        path (list): A list of tuples representing the path to highlight.
    """
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            color = RED if (i, j) in path else BLUE
            stdscr.addstr(i, j * 2, value if (i, j)
                          not in path else 'X', color)


def find_start(maze, start_symbol):
    """
    Find the start position in the maze.

    Args:
        maze (list): A 2D list representing the maze.
        start_symbol (str): The symbol representing the start position.

    Returns:
        tuple: A tuple of (row, col) for the start position, or None if not found.
    """
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_symbol:
                return i, j
    return None


def find_neighbors(maze, row, col):
    """
    Find the neighboring cells in the maze.

    Args:
        maze (list): A 2D list representing the maze.
        row (int): The row index of the current cell.
        col (int): The column index of the current cell.

    Returns:
        list: A list of tuples representing the neighboring cells' coordinates.
    """
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT

    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]):
            neighbors.append((r, c))

    return neighbors


def find_path(maze, stdscr):
    """
    Find the path through the maze from the start to the end.

    Args:
        maze (list): A 2D list representing the maze.
        stdscr: The curses window object where the maze is displayed.

    Returns:
        list: A list of tuples representing the path from start to end, or an empty list if no path is found.
    """
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
    """
    The main function to run the maze navigation.

    Args:
        stdscr: The curses window object.
    """
    initialize_curses()
    path = find_path(MAZE, stdscr)
    stdscr.getch()


wrapper(main)
