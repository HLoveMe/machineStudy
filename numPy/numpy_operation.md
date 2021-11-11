

*  ndarray操作 
  * 所有操作都是是针对元素 np.ones((2,2)) - 1 => np.zeros((2,2),dtype=np.int16)
  * 操作都是针对所有元素 `axis` 参数可以指定轴 对应shape 的维度   见属性含义
  * 操作数组的类型对应于更一般或更精确的数组 int + float =>float
  * 视图  修改后会影响原数组。拷贝 修改后不会修改原数组
  
* 通函数 

  *  堆叠思路 [Go](https://blog.csdn.net/Riverhope/article/details/78922006)

  ```python
  # np.floor 所有元素向下取整
  # np.ceil
  # ndarray.flat 属性 一维化 
  # ndarray.flatten() => 数组一维化为 拷贝
  # np.ravel 扁平化 = ndaray.ravel 为一维数组 试图
  # 将不同数组堆叠在一起  
          concatenate	提供了axis参数，用于指定拼接方向
          append	默认先ravel再拼接成一维数组，也可指定axis
          stack	提供了axis参数，用于生成新的维度
          hstack	水平拼接，沿着行的方向，对列进行拼接
          vstack	垂直拼接，沿着列的方向，对行进行拼接
          dstack	沿着第三个轴（深度方向）进行拼接
          column_stack	水平拼接，沿着行的方向，对列进行拼接
          row_stack	垂直拼接，沿着列的方向，对行进行拼接
          r_	垂直拼接，沿着列的方向，对行进行拼接
          c_	水平拼接，沿着行的方向，对列进行拼接
      # stack  会增加一个维度 
      	np.stack((a, b, c), axis=0)
          	shape(3,) + shape(3,) + shape(3,)=>shape(3(0=>3个),3,)
           np.stack((a, b, c), axis=1)
              shape(3,) + shape(3,) + shape(3,)=>shape(3,3(1=>3个),)
           np.stack((a, b, c,d), axis=2)
              shape(3,2) + shape(3,2)+ shape(3,2) + shape(3,2)=>(3,2,4(2=>4个))
           np.stack((a, b, c,d), axis=?)
            axis=0  shape(3,2) + shape(3,2)+ shape(3,2) + shape(3,2)=>shape(4(0=>4个),2,3)
            axis=1  shape(3,2) + shape(3,2)+ shape(3,2) + shape(3,2)=>shape(2,4(1=>4个),3)
            axis=2  shape(3,2) + shape(3,2)+ shape(3,2) + shape(3,2)=>shape(3,2,4(2=>4个))
      #  保持相同维度 np.vstack np.hstack np.dstack
      # np.vstack(垂直的上下排列 y) np.hstack(水平的左右排列 x) np.dstack(垂直高低排列 z) 
      	# hstack 一维数组时 按照第一个轴进行堆叠。 其它数组堆叠时 数组堆叠都是按照第二个轴堆叠(第二轴可以长度不一致)
              a = np.array((1,2,3)) shape(3) 一维数组时
              b = np.array((2,3,4)) shape(3)
              np.hstack((a,b))=>array([1, 2, 3, 2, 3, 4])=>shape(6)
              
              a = np.array([[1],[2],[3]]) shape(3,1) 它数组堆叠时 第二个轴堆叠。
              b = np.array([[2],[3],[4]]) shape(3,1)
              np.hstack((a,b))=>
                  array([ [1, 2],
                  		[2, 3],
                  		[3, 4]])  =>shape(3,2)
                  
              np.hstack(shape(2, 3, 4),shape(2, 3, 4)) =>(2, 6, 4)
                
          # vstack 沿着第一个轴堆叠数组。 一维数组进行堆叠，则数组长度必须相同。其它数组堆叠时 第一个轴的长度可以不一样
              a = np.array((1,2,3)) shape(3) 一维数组时 沿着第一个轴纵向堆叠数组
              b = np.array((2,3,4)) shape(3)
              np.vstack((a,b))   =>shape(2,3)
              
              a = np.array([[1],[2],[3]]) shape(3,1) 沿着第一个轴纵向堆叠数组
              b = np.array([[2],[3],[4]]) shape(3,1)
              np.vstack((a,b))
              	[[1]
                   [2]
                   [3]
                   [2]
                   [3]
                   [4]] shape(6, 1)
              
              np.hstack(shape(2, 3, 4),shape(2, 3, 4)) =>(4,3, 4) 沿着第一个轴纵向堆叠数组
            
          # dstack 对数组进行第三轴堆叠 结果维度至少为3
              当数组为（M,N）转为(M,N,1) 第三轴堆叠
              当数组为(M,) 转为 (1,M,1)  第三轴堆叠
              a = np.array((1,2,3)) =>shape(1,3,1)
              b = np.array((2,3,4)) =>shape(1,3,1)
              np.dstack((a,b)) => shape(1,3,2)
              
              
          # np.column_stack ~~== hstack ?
          # np.row_stack === vstack
      
      	# appand(arr,value,axis=None)
              1: axis=None ravel扁平化,再拼接
              2：axis=0  沿第一个轴拼接 =>vstack
              3：axis=1  沿第二个轴拼接 =>hstack
              4:axis=2  沿第三个轴拼接 =>dstack
      	# numpy.concatenate()~=appand() 更高效 更适合多数组拼接
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

    

