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


# a = np.arange(24).reshape(2,3,4)
# b = np.arange(24).reshape(2,3,4)
# print(np.hstack((a,b)))
# print(a.shape,b.shape,np.hstack((a,b)).shape)

# a = np.arange(24).reshape(2,3,4)
# b = np.arange(24).reshape(2,3,4)
# print(a.shape,b.shape)
# print(np.vstack((a,b)),np.vstack((a,b)).shape)


# a = np.array([[1,2],
#               [3,4]])
# b= np.array([[5,6],
#               [7,8]])
# c= np.array([[5,6],
#               [7,8]])
# print(a.shape,b.shape,c.shape)
# result = np.dstack((a,b,c))
# print(result,result.shape)


# a = np.array([[1, 1,7],[1, 1,7]])
# b = np.array([[1, 1,7],[1, 1,7]])
# c = np.array([[1, 1,7],[1, 1,7]])
# d = np.array([[1, 1,7],[1, 1,7]])
# print(a.shape)
# print(np.stack((a, b, c,d), axis=1).shape)

# ar1 = np.array([[1,2,3], [4,5,6]]) # 2,3
# ar2 = np.array([[7,8,9], [11,12,13]]) # 2,3

# print(np.append(ar1,ar2,1))


# a = np.arange(16).reshape(4,4)
# print(a.shape)
# sp1, sp2,sp3,sp4 = np.hsplit(a, 4)
# print(sp1.shape, sp2.shape,sp3.shape,sp4.shape)


# a = np.arange(16).reshape(4,4)
# print(a.shape)
# sp1, sp2,sp3,sp4 = np.vsplit(a, 4)
# print(sp1.shape, sp2.shape,sp3.shape,sp4.shape)


a = np.arange(24).reshape(2,3,4)
print(a.shape)
sp1, sp2,sp3,sp4 = np.dsplit(a, 4)
print(sp1.shape, sp2.shape,sp3.shape,sp4.shape)