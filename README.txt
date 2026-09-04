# Students

- Responsible of the codes: <SAMSON Ethan>
- Responsible of the documentation: <CAIL Mathéo>
- Responsible of the unit tests: <JAROSZEK Tom>



# Players

*Please write here a few lines on the players you wrote.*
*Precise which choices you made, and why.*
*If you chose to create some functions, which ones and why?*
*What is the complexity of these functions?*
*Did you use defensive programming? if so, where and how?*

We created three types of players: DFS, BFS, and Dijkstra. The BFS player uses a FIFO  structure, while the DFS player uses a LIFO  structure. After testing both methods, we decided to focus on Dijkstra, because it’s generally considered the most efficient for finding the shortest path, especially when edge weights in the graph vary.

So, we created three main functions to implement the Dijkstra algorithm: find_route, traversal, and Dijkstra. The find_route function reconstructs the path once the shortest distances are calculated, and its complexity depends on the number of nodes explored, so it has a worst-case time complexity of O(n). Both traversal and Dijkstra also have a time complexity of O(n).

We didn’t use defensive programming in our implementation. We assumed that the game state and the maze would always be valid and properly formatted.



# Games

*Please write here a few lines on the game scripts you created.*
*What are they made for?*
*Did you change some game parameters? If so, which ones and why?*

The game scripts we created are designed to manage the maze environment and the interactions between the players. They handle tasks like player movement, pathfinding, and decision-making based on the state of the game (such as the player's position, the location of the cheese, and obstacles in the maze). Initially, we didn’t change many game parameters, but later we adjusted the maze settings to create more diverse challenges for our players. For example, we modified the density of walls and mud in the maze to test how different levels of difficulty affect the performance of the pathfinding algorithms.

The game scripts are crucial for simulating the players' actions in real-time, testing the efficiency of different algorithms, and ensuring that the players' logic is working correctly.



# Unit tests

*Please write here a few lines on the tests you designed.*
*What are they testing?*
*Do you test some error use cases?*
*Are there some missing tests you would have liked to make?*

For the unit tests, we created several test cases to evaluate the performance and correctness of the Dijkstra algorithm. The tests mainly check that the traversal_Dijkstra function correctly calculates the shortest path between two points in the maze. We ensure that the computed path starts and ends at the correct points, and that each step in the path is valid (i.e., it corresponds to a neighbor of the previous point).

We also tested edge cases, such as when the start and end points are the same, or when there’s no valid path between them. We didn’t test more complex error cases, such as invalid maze structures or inconsistent game states, as we didn’t implement defensive programming.



# Utils

*Did you provide anything in the `utils` directory?*
*What are those files?*

Nothing



# Documentation

*Anything to say regarding the documentation?*

Nothing



# Others

*If you had to answer particular questions in the practical session, write your answers here*
*Did you make some interesting analyses?*
*Does your code have particular dependencies we should install ?*
*Anything else to add?*

Nothing