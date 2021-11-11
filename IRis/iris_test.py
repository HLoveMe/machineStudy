
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()
data_all = np.empty((len(iris.data), 5), dtype=np.float64)
# print(data_all.shape)
for index in range(len(iris.data)):
    item = iris.data[index]
    one_iris = np.empty(5)
    
    print(one_iris)
    # one_iris[4] = iris.target[index]
    # np.append(one_iris, iris.target[index])
    # print(one_iris)
    # data_all[index] = (one_iris)
# #  X_train, X_test, y_train, y_test
# result = train_test_split(data_all, test_size=0.2)
# print(result)