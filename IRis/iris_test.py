
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()
# 数据源处理
# data 和 target 进行合并
iris_data = np.hstack((iris.data, iris.target.reshape(-1, 1)))
# 拆数据
train,test = train_test_split(iris_data, test_size=0.2)

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
  x_0,x_1,x_2,x_3 = item[0],item[1],item[2],item[3]
  # y_0,y_1,y_2,y_3 = y[0],y[1],y[2],y[3]
  print(x_0,x_1,x_2,x_3)
  # print(y_0,y_1,y_2,y_3)
  # return np.sqrt(np.sum(np.square(x-y)))

getdistance(test[0])