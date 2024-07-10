# Path Finder in Maze using BFS

This Python project demonstrates how to find the shortest path from a starting point ('O') to an endpoint ('X') in a maze using the Breadth-First Search (BFS) algorithm.

## Features
Maze Representation: The maze is represented as a 2D grid where '#' represents walls, ' ' represents empty spaces, 'O' is the starting point, and 'X' is the endpoint.

Path Finding: The find_path function implements the BFS algorithm to find the shortest path from the starting point to the endpoint in the maze.

Visualization: The print_maze function visualizes the maze and the path found using the curses library, showing the progress step by step in the terminal.

## Usage
1- Installation:

Clone the repository: git clone https://github.com/your-username/path-finder-maze.git

Navigate into the project directory: cd path-finder-maze

Install dependencies (curses is required for terminal visualization): pip install -r requirements.txt

2- Run the Program:

Execute the main script: python path_finder.py

Follow the on-screen instructions to see the maze visualization and the path finding process.

## Example
Here's a simple example of a maze represented in the code:

```python
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

# Running the path finding algorithm
path = find_path(maze)
print("Path found:", path)
```
## Credits
Author: Amirreza Mousavifard

Contact: amirrezamousavi9130@gmail.com

Feel free to customize the README.md with additional information or sections based on your preferences and project details.
