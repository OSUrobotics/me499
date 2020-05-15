import numpy as np

# Basic array definition, and shortcuts for creating common arrays

array_1d = np.array([1, 2, 3])
array_2d = np.array([[1, 4, 3], [1, 5, 9]])   # 2 x 3 array
zeros = np.zeros((3, 4))
identity = np.identity(4)
rand = np.random.uniform(0, 1, size=(100, 3))
points = np.linspace(1, 2, 100)

# Basic info
array_1d.shape          # (3,)
array_2d.shape          # (3, 2)
array_2d.size           # 6

# Element access/assignment
array = np.array([[1,-1], [2, -2], [3, -3]])    # 3 x 2 array
array[0]        # [1, -1]               - Row access
array[:,1]      # [-1, -2, 3]           - Column access
array[:,0:1]    # [[-1], [-2], [-3]]    - Slicing notation - Note that you still have a 2D array of shape 3x1
array[0,0]      # 1
array[0,0] = 5                          # Single element assignment
array[1:,0:] = np.identity(2)           # Multiple element assignment - Must have consistent shape
                                        # Final array: [[5, -1], [1, 0], [0, 1]]

# Resizing array
# None of these operations are in-place, so you must assign to a new variable to have an effect!
mat_1 = np.random.uniform(size=(6, 4))      # 6x2 array
mat_1.T                                     # Transpose, 4x6 array
np.reshape(mat_1, (24,))                    # 24-vector
np.reshape(mat_1, (-1,))                    # -1 means "infer this dimension based off the others" - Also a 24-vector
np.reshape(mat_1, (4, -1))                  # Inferred dimension is 24/4 = 6, so get 4x6 array
np.reshape(mat_1, (-1, 2, 3))               # Inferred dimension is 24/(2*3) = 4, so get 4x2x3 array

# Basic arithmetic
array_a = np.array([1, 2, -3.5])
array_b = np.array([3, 1, 2])

array_a + array_b   # [4, 3, -1.5]
array_a * array_b   # [3, 2, -7.0]
array_a - 3         # [-2, -1, -6.5]
2 ** array_b        # [8, 2, 4]

# Arithmetic operations involving an NxD array and a D-vector
# Will do "row-wise" operations to the NxD array
array_2d - array_1d     # [[0, 2, 0], [0, 3, 6]]

# Matrix operations
mat_1 = np.random.uniform(size=(3, 2))
mat_2 = np.random.uniform(size=(2, 2))
np.linalg.inv(mat_2)    # Inverse
mat_1 @ mat_2           # Matrix multiplication - equivalent to mat_1.dot(mat_2)

# Truth operations and truth-based subsetting
truth_index = array_1d > 1.5        # Boolean array of [False, True, True]
array_1d[truth_index]               # [2, 3]
np.all(truth_index)                 # False, because not all of the values in the array are True
np.any(truth_index)                 # True, because at least one of the values in the array is True

# Index-based subsetting
vals = np.array([[2, 3], [4, 5], [1, 1]])   # 3x2 array
to_index = np.array([0, 2])
vals[to_index]                              # [[2, 3], [1, 1]]
sorting_index = np.array([1, 0, 2])
vals[sorting_index]                         # [[4, 5], [2, 3], [1, 1]]

# Summary stats
stats = np.array([[1, 2, 3], [-1, 5, 4], [3, 4, 1], [9, 8, 3]])     # 4x3 array
stats.mean()                    # 3.5                           - Mean over all 12 elements
stats.mean(axis=0)              # [3, 4.75, 2.75]               - Condenses column-wise to get a 3-vector
stats.mean(axis=1)              # [2, 2.667, 2.667, 6.667]      - Condenses row-wise to get a 4-vector
np.linalg.norm(stats, axis=1)   # [3.74, 6.48, 5.10, 12.41]     - Point norms