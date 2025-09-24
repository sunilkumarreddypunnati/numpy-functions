'''Task 2: Array Appending and Conditional Replacement
Objective: Append elements to an array and 
apply a condition to modify values.

Problem:

Create a 1D array [10, 20, 30].
Append [40, 50] to it (np.append).
Replace all values greater than 25 with 1, else 0 (np.where).
Print the final array.

Expected Output:
[0 0 1 1 1]

Functions Used: np.append, np.where'''

import numpy as np
arr=np.array([10,20,30])
a=np.append(arr,[40,50])
b=np.where(a>25,1,0)
print(b)