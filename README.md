## Coding challenge

The following coding challenge is a test designed to evaluate programming and Python coding skills for a Data Scientist position,

Context: Saki and Trapattoni-san's latest project is Ordirale, a robotic system to automate and speed up the movement of heavy stacks of manga within a retail store. They envision the store as an 8x8 matrix, with each cell indicating if it's free (" "), occupied by a wall ("P"), manga stack ("M"), action figure column ("A"), or checkout ("C"). Ordirale needs to move from a starting cell to an ending cell, making the least number of moves possible, following the movement pattern of a knight in chess.

Task: Initially, a function is needed to take two integer values representing the initial and final positions within the store layout (specified using a list of lists). The function should return the minimum number of moves for Ordirale to traverse this path. If either cell is invalid or occupied, it should return np.nan. If no valid path exists between the cells, it should return np.inf. If the cells are both free and the same, it should return 0.

Generalization: Another function should be implemented to handle different store layouts. Given a new store configuration and two positions within it, this function should also return the minimum number of moves for Ordirale to traverse, following the same rules and exceptions as the initial function.
