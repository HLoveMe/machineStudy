
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()
# 数据源处理
# data 和 target 进行合并
iris_data = np.hstack((iris.data, iris.target.reshape(-1, 1)))
# 拆数据
train, test = train_test_split(iris_data, test_size=0.2)

# Knn 数据训练 使用distance 来作为数据分类依据
# from sklearn.neighbors import KNeighborsClassifier
'''
方式1：
  1:计算当前点到所有训练集数据的距离
  2:指定K值 取前K个距离最近的数据
  3:取出这K个数据的distance 
  4:看距离哪个最近 最近的为预测数据的类别
'''
K = 3


def getdistance(item):
    # print(item.shape)
    x_0, x_1, x_2, x_3,_ = item
    distance_arr = []
    for data in train:
        d_0, d_1, d_2, d_3, target = data
        # print(np.square(d_0-x_0))
        distance = np.sqrt(
            np.sum((np.square(d_0-x_0),
                    np.square(d_1-x_1),
                    np.square(d_2-x_2),
                    np.square(d_3-x_3))))
        distance_arr.append([distance, target])
    # print(distance_arr[0])
    distance_arr.sort(key=lambda item: item[0], reverse=False)

    use_data = distance_arr[0:K]
    result = [0, 0, 0]
    for index in range(K):
        if use_data[index][1] == 0.0:
            result[0] = result[0]+1
        elif use_data[index][1] == 1.0:
            result[1] = result[1]+1
        elif use_data[index][1] == 2.0:
            result[2] = result[2]+1

    return np.array(result) / K


for index in range(len(test)):
    item = test[index]
    forecast = item[-1]
    result = getdistance(item)
    print(result,forecast)
