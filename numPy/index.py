import numpy as np

# Student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# data = np.array([('rolf', 21, 75),
#                   ('anna', 19, 65),
#                   ('ethan', 18, 75)], dtype=Student)
# print(type(data['age']))


# data = np.arange(10, 30, 5)
# print(type(data))

# random =  np.arange(24).reshape(2,3,4)
# random = np.random.randint(0,100,(2,3,4))
# print(random,)
# print('11111111111')
# print(random.max(axis=0))

# print('222222222222222')
# print(random.max(axis=1))
# print('333333333333')
# print(random.max(axis=2))


# print(np.random.randint(0,100,(2,3,4)))
# print(np.arange(9).reshape(3,3).ravel() )
# print(np.ravel(np.arange(9).reshape(3,3)))
# np.ceil

# a = np.array([1,2,3])
# b= np.array([4,5,6])
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))

a = np.arange(24).reshape(2,3,4)
b = np.arange(24).reshape(2,3,4)
print(np.hstack((a,b)))
print(a.shape,b.shape,np.hstack((a,b)).shape)
