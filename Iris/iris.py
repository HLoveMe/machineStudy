from sklearn.neighbors import KNeighborsClassifier
# 使用 KNeighborsClassifier 对iris 数据进行Knn算法预测
        # n_neighbors: int, 可选参数(默认为 5)
        # weights（权重）: str or callable(自定义类型), 可选参数(默认为 ‘uniform’)
        #         用于预测的权重函数。可选参数如下:
        #                - ‘uniform’ : 统一的权重. 在每一个邻居区域里的点的权重都是一样的。
        #                - ‘distance’ : 权重点等于他们距离的倒数。使用此函数，更近的邻居对于所预测的点的影响更大。
        #                - [callable] : 一个用户自定义的方法，此方法接收一个距离的数组，然后返回一个相同形状并且包含权重的数组。
        # algorithm（算法）: {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, 可选参数（默认为 'auto'）
        #         计算最近邻居用的算法：
        #                - ‘ball_tree’ 使用算法[BallTree](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree)
        #                - ‘kd_tree’ 使用算法[KDTree](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree)
        #                - ‘brute’ 使用暴力搜索.
        #                - ‘auto’ 会基于传入[fit](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.fit)方法的内容，选择最合适的算法。
        #         注意 : 如果传入fit方法的输入是稀疏的，将会重载参数设置，直接使用暴力搜索。
        #  leaf_size（叶子数量）: int, 可选参数(默认为 30)
        #         传入BallTree或者KDTree算法的叶子数量。此参数会影响构建、查询BallTree或者KDTree的速度，以及存储BallTree或者KDTree所需要的内存大小。 此可选参数根据是否是问题所需选择性使用。
        #  p: integer, 可选参数(默认为 2)
        #         用于Minkowski metric（[闵可夫斯基空间](https://zh.wikipedia.org/wiki/%E9%96%94%E8%80%83%E6%96%AF%E5%9F%BA%E6%99%82%E7%A9%BA)）的超参数。p = 1, 相当于使用[曼哈顿距离](https://zh.wikipedia.org/wiki/%E6%9B%BC%E5%93%88%E9%A0%93%E8%B7%9D%E9%9B%A2) (l1)，p = 2, 相当于使用[欧几里得距离](https://zh.wikipedia.org/wiki/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E8%B7%9D%E7%A6%BB)(l2)  对于任何 p ，使用的是[闵可夫斯基空间](https://zh.wikipedia.org/wiki/%E9%96%94%E8%80%83%E6%96%AF%E5%9F%BA%E6%99%82%E7%A9%BA)(l_p)
        #  metric（矩阵）: string or callable, 默认为 ‘minkowski’
        #         用于树的距离矩阵。默认为[闵可夫斯基空间](https://zh.wikipedia.org/wiki/%E9%96%94%E8%80%83%E6%96%AF%E5%9F%BA%E6%99%82%E7%A9%BA)，如果和p=2一块使用相当于使用标准欧几里得矩阵. 所有可用的矩阵列表请查询 DistanceMetric 的文档。
        #  metric_params（矩阵参数）: dict, 可选参数(默认为 None)
        #         给矩阵方法使用的其他的关键词参数。
        #  n_jobs: int, 选参数(默认为 1)
        #         用于搜索邻居的，可并行运行的任务数量。如果为-1, 任务数量设置为CPU核的数量。不会影响[fit](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.fit)方法。

from sklearn import datasets

iris_data = datasets.load_iris()
print(iris_data)

