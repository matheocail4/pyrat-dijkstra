"""
This module implements a Dijkstra pathfinding player for the PyRat game.
The player finds the shortest path to cheese in a maze using Dijkstra's algorithm.
"""

# External imports
from typing import Any, Dict, List, Tuple
from typing_extensions import Self
import heapq as hp

# PyRat imports
from pyrat import Player, Maze, GameState, Action, Graph


class Dijkstra(Player):
    """
    A PyRat player that uses Dijkstra's algorithm to find the shortest path to cheese.
    
    This player implements the Player interface with preprocessing, turn, and postprocessing methods.
    The main algorithm is implemented in the traversal_Dijkstra method.
    """

    def __init__(self: Self, *args: Any, **kwargs: Any) -> Self:
        """
        Initialize the Dijkstra player.

        Args:
            self: Reference to the current object.
            args: Arguments to pass to the parent constructor.
            kwargs: Keyword arguments to pass to the parent constructor.

        Returns:
            A new instance of the class.
        """
        # Inherit from parent class
        super().__init__(*args, **kwargs)

        print("Constructor")
        self.actions: List[Action] = []

    def preprocessing(self: Self, maze: Maze, game_state: GameState) -> None:
        """
        Preprocessing phase: compute the shortest path to the first cheese.

        This method is called once at the beginning of the game.
        It calculates the shortest path from the player's starting position to the first cheese.

        Args:
            self: Reference to the current object.
            maze: An object representing the maze in which the player plays.
            game_state: An object representing the state of the game.

        Returns:
            None.
        """
        print("Preprocessing")

        start_location = game_state.player_locations[self.name]
        end_location = game_state.cheese[0]
        vertices_list = self.traversal_Dijkstra(maze, start_location, end_location)
        print(vertices_list)
        self.actions = maze.locations_to_actions(vertices_list)

    def turn(self: Self, maze: Maze, game_state: GameState) -> Action:
        """
        Execute one turn of the game by returning the next action.

        This method is called at each turn of the game. It returns the next action
        from the precomputed path, or STAY if no more actions are available.

        Args:
            self: Reference to the current object.
            maze: An object representing the maze in which the player plays.
            game_state: An object representing the state of the game.

        Returns:
            One of the possible actions.
        """
        print("Turn", game_state.turn)

        if len(self.actions) > 0:
            return self.actions.pop(0)
        return Action.STAY

    def postprocessing(
        self: Self,
        maze: Maze,
        game_state: GameState,
        stats: Dict[str, Any],
    ) -> None:
        """
        Postprocessing phase: called once at the end of the game.

        Args:
            self: Reference to the current object.
            maze: An object representing the maze in which the player plays.
            game_state: An object representing the state of the game.
            stats: Statistics about the game.

        Returns:
            None.
        """
        print("Postprocessing")

    def traversal_Dijkstra(
        self: Self, maze: Maze, start: Tuple[int, int], end: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Compute the shortest path between two points using Dijkstra's algorithm.

        This implementation uses a priority queue (min-heap) to always process the node
        with the smallest distance first. It handles weighted edges (e.g., mud cells).

        Args:
            self: Reference to the current object.
            maze: An object representing a maze with mud and walls.
            start: Starting point (tuple of coordinates).
            end: Ending point (tuple of coordinates).

        Returns:
            A list of coordinates representing the shortest path from start to end.
            
        Complexity:
            Time: O((V + E) log V) where V is vertices and E is edges
            Space: O(V) for the visited set, distances, and parent dictionaries
        """
        # Initialize the priority queue with the start node
        priority_queue: List[Tuple[float, Tuple[int, int]]] = []
        hp.heappush(priority_queue, (0, start))

        # Track visited nodes and distances
        visited_nodes: set = set()
        distances: Dict[Tuple[int, int], float] = {start: 0}
        parent: Dict[Tuple[int, int], Tuple[int, int] | None] = {start: None}

        # Main Dijkstra loop
        while priority_queue:
            current_distance, current_node = hp.heappop(priority_queue)

            # Skip if already visited
            if current_node in visited_nodes:
                continue

            # Early termination if we reach the destination
            if current_node == end:
                break

            # Mark as visited
            visited_nodes.add(current_node)

            # Explore neighbors
            for neighbor in maze.get_neighbors(current_node):
                if neighbor not in visited_nodes:
                    # Calculate the distance to this neighbor
                    edge_weight = maze.get_weight(current_node, neighbor)
                    updated_distance = current_distance + edge_weight

                    # Update if we found a shorter path
                    if neighbor not in distances or updated_distance < distances[neighbor]:
                        distances[neighbor] = updated_distance
                        hp.heappush(priority_queue, (updated_distance, neighbor))
                        parent[neighbor] = current_node

        # Reconstruct the path from start to end
        current_node = end
        shortest_route: List[Tuple[int, int]] = []

        while current_node is not None:
            shortest_route.append(current_node)
            current_node = parent.get(current_node)

        shortest_route.reverse()

        return shortest_route
