import numpy as np

# Student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# data = np.array([('rolf', 21, 75),
#                   ('anna', 19, 65),
#                   ('ethan', 18, 75)], dtype=Student)
# print(type(data['age']))


# data = np.arange(10, 30, 5)
# print(type(data))

random =  np.arange(24).reshape(2,3,4)
print(random,)
print('11111111111')
print(random.max(axis=0))
print(random.max(axis=1))
print(random.max(axis=2))
