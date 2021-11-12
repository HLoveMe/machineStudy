import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
# 数据源处理
# data 和 target 进行合并
iris_data = np.hstack((iris.data, iris.target.reshape(-1, 1)))
# 拆数据
train, test = train_test_split(iris_data, test_size=0.2)


'''
# Knn 数据训练 邻近算法
方式1：
  1:计算[预测数据]到所有训练集数据的距离
  2:指定K值 取前K个距离最近的数据
  3:评估最近的K个 到各个预测结果的概率 。便可预测数据的类别
'''
K = 5

def forecast_data(item):
    forecast = item[:-1]
    distance_arr = []
    for data in train:
        target = data[-1]
        current = data[:-1]
        distance = np.sqrt(np.sum((current - forecast) ** 2))
        distance_arr.append([distance, target])

    distance_arr.sort(key=lambda item: item[0], reverse=False)

    use_data = distance_arr[0:K]
    result = np.array([0, 0, 0])
    for index in range(K):
        if use_data[index][1] == 0.0:
            result[0] = result[0]+1
        elif use_data[index][1] == 1.0:
            result[1] = result[1]+1
        elif use_data[index][1] == 2.0:
            result[2] = result[2]+1
    result = np.stack((np.array([0, 1, 2]), result), axis=1).tolist()
    result.sort(
        key=lambda item: item[1], reverse=True)
    return result[0][0]


if __name__ == '__main__':
    success, fail = 0, 0
    for item in test:
        exec = item[-1]
        forecast = forecast_data(item)
        if exec == forecast:
            success += 1
        else:
            fail += 1
    print('样本总数:', len(iris.data),'训练样本：',len(train),'测试样本：',len(test))
    print('success:', success, 'fail:', fail,'预测成功概率:',success/(success+fail))
