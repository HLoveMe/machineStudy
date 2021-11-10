

*  ndarray操作 
  * 所有操作都是是针对元素 np.ones((2,2)) - 1 => np.zeros((2,2),dtype=np.int16)
  * 操作都是针对所有元素 `axis` 参数可以指定轴 对应shape 的维度   见属性含义
  * 操作数组的类型对应于更一般或更精确的数组 int + float =>float
  
* 通函数 sin，cos和exp

  ```python
  # np.floor 所有元素向下取整
  # np.ceil
  # np.ravel 扁平化 = ndaray.ravel
  ```

  

* 切片

  * **一维**的数组可以进行索引、切片和迭代操作的，

    ```python
    import numpy as np
    dome_data =  np.arange(10) =>[0,1,2,3,4,5,6,7,8,9]
    dome_data*3 =>[ 0  3  6  9 12 15 18 21 24 27]
    dome_date[::-1] [9 8 7 6 5 4 3 2 1 0]
    ```

    

  * **多维**的数组每个轴可以有一个索引。这些索引以逗号分隔的元组给出：

    ```python
    import numpy as np
    dome_data =  np.arange(0,24,1).reshape(4,6)
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]
     [12 13 14 15 16 17]
     [18 19 20 21 22 23]]
    dome_data[2,3] =>15
    dome_date[1]
    =>dome_data[1,:]
    =>dome_data[1,...] = > [ 6  7  8  9 10 11]
    ```

  * 对多维数组进行 **迭代（Iterating）** 是相对于第一个轴完成的。使用flat属性对所有属性迭代

    ```python
    for row in data:
    	pass
    for item in data.flat
    	pass
    ```

    

