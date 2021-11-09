import numpy as np

# Student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# data = np.array([('rolf', 21, 75),
#                   ('anna', 19, 65),
#                   ('ethan', 18, 75)], dtype=Student)
# print(type(data['age']))


data = np.arange(10, 30, 5)

a_data = np.arange(1,100,3)
np.empty_like