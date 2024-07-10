import curses
from curses import wrapper
import queue
import time

maze = [
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

def print_maze(maze, stdscr, path=[]):
  BLUE = curses.color_pair(1)
  RED = curses.color_pair(2)

  for i, row in enumerate(maze):
    for j, value in enumerate(row):
      stdscr.addstr(i, j*2, value, BLUE)
  
def find_start(maze, start):
  for i, row in enumerate(maze):
    for j, value in enumerate(row):
      if value == start:
        return i, j
      
  return None

def find_path(maze, stdscr):
  start = "O"
  end = "X"
  start_pos = find_start(maze,start)

  q = queue.Queue()
  q.put((start_pos, [start_pos]))

  visited = set()

  while not q.empty():
    current_pos, path = q.get()
    row, col = current_pos

    if maze[row][col] == end:
      return path
    
    neighbors = find_neighbors(maze, row, col)
    for neighbor in neighbors:
      if neighbors in visited:
        continue

      r, c = neighbor
      if maze[r][c] == "#":
        continue

      new_path = path + [neighbor]
      q.put((neighbor, new_path))
      visited.add(neighbor)
    
def find_neighbors(maze, row, col):
  neighbors = []

  if row > 0: # UP
    neighbors.append((row - 1, col))
  if row + 1 < len(maze): # DOWN
    neighbors.append((row + 1, col))
  if col > 0: # LEFT
    neighbors.append((row, col - 1))
  if col + 1 < len(maze[0]): # RIGHT
    neighbors.append(row, col + 1)

  return neighbors



def main(stdscr):
  curses.init_pair(1, curses.COLOR_BLUE,curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_RED,curses.COLOR_BLACK)

  stdscr.clear()
  print_maze(maze, stdscr)
  stdscr.refresh()
  stdscr.getch()

wrapper(main)