
## Knn 算法

  ```
  邻近算法，或者说K最邻近（KNN，K-NearestNeighbor）分类算法是数据挖掘分类技术中最简单的方法之一。
  所谓K最近邻，就是K个最近的邻居的意思，说的是每个样本都可以用它最接近的K个邻近值来代表。
  近邻算法就是将数据集合中每一个记录进行分类的方法
  ```
  * 图解
    ![03087bf40ad162d95867202e15dfa9ec8a13cd73](C:\Users\zihao.zhu\Desktop\work\GITHUB\machineStudy\iris_test\iris_csdn\03087bf40ad162d95867202e15dfa9ec8a13cd73.jpg)
    
    ```python
    》存在w1,w2,w3三种可能性结果
    》Knn 算法。处理给定预测数据Xu，计算出该预测数据属于哪一类结果的可能性。
    ```
    
    ```python

     方式1：
        1:计算[预测数据]到所有训练集数据的距离
        2:指定K值 取前K个距离最近的数据
        3:评估最近的K个 到各个预测结果的概率 。便可预测数据的类别
        4:调整K值 重复2,3步骤。以得到合适和K和预测的准确性的平衡
      import numpy as np
      from sklearn import datasets
      from sklearn.model_selection import train_test_split
      # 读取iris数据
      iris = datasets.load_iris()
      # 数据源处理
      # data 和 target 进行合并
      iris_data = np.hstack((iris.data, iris.target.reshape(-1, 1)))
      # 拆分数据为 训练集和测试集
      train, test = train_test_split(iris_data, test_size=0.2)
      # 指定K值
      K = 5
      def forecast_data(item):
          forecast = item[:-1]
          distance_arr = []
          for data in train:
              target = data[-1]
              current = data[:-1]
              # 计算预测数据到训练数据的距离
              distance = np.sqrt(np.sum((current - forecast) ** 2))
              distance_arr.append([distance, target])

          distance_arr.sort(key=lambda item: item[0], reverse=False)
          # 取得距离最近的前K个数据
          use_data = distance_arr[0:K]
          result = np.array([0, 0, 0])
          for index in range(K):
              if use_data[index][1] == 0.0:
                  result[0] = result[0]+1
              elif use_data[index][1] == 1.0:
                  result[1] = result[1]+1
              elif use_data[index][1] == 2.0:
                  result[2] = result[2]+1
          # 得到预测结果
          result = np.stack((np.array([0, 1, 2]), result), axis=1).tolist()
          result.sort(
              key=lambda item: item[1], reverse=True)
          return result[0][0]
      # 
      if __name__ == '__main__':
          success, fail = 0, 0
          for item in test:
              exec = item[-1]
              forecast = forecast_data(item)
              if exec == forecast:
                  success += 1
              else:
                  fail += 1
      print('样本总数:', len(iris.data),'训练样本：'，len(train),'测试样本：',len(test))
      print('success:', success, 'fail:', fail,'预测成功概率:',success/(success+fail))

      # 样本总数: 150 训练样本： 120 测试样本： 30
      # success: 28 fail: 2 预测成功概率: 0.9333333333333333
      
    ```