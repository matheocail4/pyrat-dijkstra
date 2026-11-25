# PyRat player with Dijkstra's algorithm

A player for the PyRat maze game that uses Dijkstra's algorithm to find the shortest path to the cheese, taking weighted cells (such as mud) into account.

IMT Atlantique algorithms course project, fall 2024.

## Team and roles

- **Code**: Ethan Samson
- **Documentation**: Mathéo Cail
- **Unit tests**: Tom Jaroszek

## Approach

The team first wrote breadth-first search (FIFO queue) and depth-first search (LIFO stack) players, then focused on Dijkstra's algorithm, which finds the shortest path when moves have different costs, as with mud in the maze.

- **Preprocessing**: computes the shortest path from the starting position to the first cheese.
- **Turn**: plays the next move of the precomputed path.
- **Postprocessing**: cleans up after the game.

The search uses a min-heap priority queue (`heapq`): time complexity O((V + E) log V), memory O(V), where V is the number of cells and E the number of connections between them.

## Tests

The unit tests (`test_Dijkstra.ipynb`) check, on randomly generated mazes of different sizes and densities, that:

- the path starts and ends at the right cells;
- each step moves to a neighbouring cell;
- edge cases are handled, such as identical start and end cells.

Inputs are assumed to be valid: the player does not check for malformed mazes or inconsistent game states.

## Files

- `Dijkstra.py`: the player and the Dijkstra implementation
- `test_Dijkstra.ipynb`: unit tests
- `visualize_Dijkstra.ipynb`: visualisation of a game

## Getting started

```bash
pip install -r requirements.txt
jupyter notebook test_Dijkstra.ipynb
```
