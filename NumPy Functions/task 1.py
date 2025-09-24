'''Task 1: Array Creation and Diagonal Modification
Objective: Learn to create arrays and modify diagonal elements.

Problem:

Create a 3×3 array filled with 7 (np.full).
Replace the diagonal elements with 0 (np.diagonal).
Print the final array.

Expected Output:

[[0 7 7]
 [7 0 7]
 [7 7 0]]

Functions Used: np.full, np.diagonal'''

import numpy as np
arr=np.full((3,3),7)
a=np.fill_diagonal(arr,0)
print(arr)
