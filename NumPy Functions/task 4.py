'''Task 4: Array Splitting

Create

[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]]


Split into 3 equal parts.

Split horizontally into 2 parts.

Split vertically into 3 parts.

Functions: np.split, np.hsplit, np.vsplit'''

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
s=np.split(arr,3)
sh=np.hsplit(arr,2)
vs=np.vsplit(arr,3)
print("Split into 3 equal parts:\n",s)
print("Split horizontally into 2 parts:\n",sh)
print("Split vertically into 3 parts:\n",vs)
