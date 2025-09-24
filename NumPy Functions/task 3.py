'''Task 3: Stack and Concatenate

Create arrays: a=[1,2,3], b=[4,5,6], c=[[7,8],[9,10]].

Horizontally and vertically stack a & b.

Concatenate c with itself along rows and columns.

Functions: np.hstack, np.vstack, np.concatenate'''

import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([[7,8],[9,10]])
print("hstack:\n",np.hstack((a,b)))
print("vstack:\n",np.vstack((a,b)))
print("Concatenate Axis=0:\n",np.concatenate((c,c),axis=0))
print("Concatenate Axis=1:\n",np.concatenate((c,c),axis=1))

