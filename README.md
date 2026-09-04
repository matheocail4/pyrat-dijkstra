# Dijkstra PyRat Player

A PyRat game player implementation using Dijkstra's algorithm to find the shortest path to cheese in a maze.

## Overview

This project implements a player for the PyRat game that uses Dijkstra's shortest path algorithm to navigate mazes and collect cheese. The algorithm efficiently handles weighted edges (such as mud cells) to find optimal paths.

## Students

- **Code**: SAMSON Ethan
- **Documentation**: CAIL Mathéo  
- **Unit Tests**: JAROSZEK Tom

## Features

- **Dijkstra's Algorithm**: Efficient shortest path computation using a min-heap priority queue
- **Weighted Graph Support**: Handles maze terrain variations (walls, mud, regular cells)
- **PyRat Integration**: Fully compatible with the PyRat game framework

## Algorithm Complexity

- **Time Complexity**: O((V + E) log V) where V is the number of vertices and E is the number of edges
- **Space Complexity**: O(V) for storing visited nodes, distances, and parent pointers

## How It Works

1. **Preprocessing**: Computes the shortest path from the player's starting position to the first cheese
2. **Turn**: Executes each step of the precomputed path
3. **Postprocessing**: Cleanup after the game ends

## Files

- `Dijkstra.py` - Main player implementation with the Dijkstra algorithm
- `test_Dijkstra.ipynb` - Unit tests for the pathfinding algorithm
- `visualize_Dijkstra.ipynb` - Visualization of the algorithm's execution
- `README.md` - This documentation

## Testing

The project includes comprehensive unit tests that verify:
- Correct path start and end points
- Valid neighbor transitions in the path
- Edge cases with random mazes of varying configurations

Run tests with:
```bash
jupyter notebook test_Dijkstra.ipynb
```

## Installation

Ensure you have PyRat installed:
```bash
pip install -r requirements.txt
```

## License

This is a school project for IMT (Institut Mines-Télécom).
