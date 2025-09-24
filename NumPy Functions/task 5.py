'''Task 5: Comprehensive Operations

Create a 4×4 array filled with 5.

Replace diagonal with 1.

Append [6,7,8,9] as row.

Horizontally and vertically stack arrays.

Concatenate along rows & columns.

Split [0..7] into 4 parts.

Apply horizontal & vertical split.

Replace values >5 with 10, else 0.

Functions: All (np.full, np.diagonal, np.append, np.where, np.hstack, np.vstack, np.concatenate, np.split, np.hsplit, np.vsplit)'''

import numpy as np
arr=np.full((4,4),5)
np.fill_diagonal(arr,1)
print("original array after change diagnol to 1:\n",arr)
print("append:\n",np.append(arr,[[6,7,8,9]],axis=0))
print("hstack:\n",np.hstack((arr,arr)))
print("vstack:\n",np.vstack((arr,arr)))
print("Concatenate along rows:\n",np.concatenate((arr,arr),axis=0))
print("Concatenate along columns:\n",np.concatenate((arr,arr),axis=1))
n=np.arange(0,8)
print("split:\n",np.split(n,4))
arr2 = np.arange(16).reshape(4,4)
print("\nArray for splitting:\n", arr2)
print("hsplit:\n",np.hsplit(arr2,2))
print("vsplit:\n",np.vsplit(arr2,2))
print("Replace values:\n",np.where(n>5,10,0))

