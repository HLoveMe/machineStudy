

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
      # np.c_ === np.hstack  numpy.r_====p.vstack
      	np.c_[[],[]] == np.hstack([],[])
      	
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
              4: axis=2  沿第三个轴拼接 =>dstack
      	# numpy.concatenate()~=appand() 更高效 更适合多数组拼接
          
     # 切割 把大数组切割为多个小数组
  		# hsplit 沿着第二轴切割 维度不变 (ary, indices_or_sections)
              np.hsplit(shape(4,4),2) => shape(4,2)+shape(4,2)
              np.hsplit(shape(4,4),4) => shape(4,1)+shape(4,1)+shape(4,1)+shape(4,1)
              np.hsplit(shape(4,8),(m,n)) 沿着第二轴拆分为 [0.m), [m n),[n,-0) 三个数组
              np.hsplit(shape(4,8),(m,n,k)) 沿着第二轴拆分为 [0.m), [m n),[n,k) [k,-0) 四个数组
           # vsplit 沿着第一轴切割 (ary, indices_or_sections)
              np.vsplit(shape(4,4),2) => shape(2,4)+shape(2,4)
              np.vsplit(shape(4,4),4) => shape(1,4)+shape(1,4)+shape(1,4)+shape(1,4)
              np.vsplit(shape(4,8),(m,n)) 沿着第一轴拆分为 [0.m), [m n),[n,-0) 三个数组
              np.vsplit(shape(4,8),(m,n,k)) 沿着第一轴拆分为 [0.m), [m n),[n,k) [k,-0) 四个数组
           # dsplit 第三轴切割   (ary, indices_or_sections)
              np.dsplit(shape(2,3,4)) => (2,3,1) + (2,3,1) + (2,3,1) + (2,3,1)
              np.dsplit(shape(4,8，10),(m,n)) 沿着第三轴拆分为 [0.m), [m n),[n,-0) 三个数组
              np.dsplit(shape(4,8，10),(m,n,k)) 沿着第三轴拆分为 [0.m), [m n),[n,k) [k,-0) 四个数组                                                  
           # split  array_split(等于split 区别在于可以拆为多个长度不同的数组 (8->3)=>(3,2,2))
              split(ary, indices_or_sections, axis=0)
              hsplit ==  split(axis=1)
              vsplit ==  split(axis=0)
              dsplit ==  split(axis=2)
                                                                            
    # 插入insert
        numpy.insert(arr, obj, values, axis=None)
            arr:源数据
            obj:索引 或 索引集合  1,[1,3],(1,3) 第一个and三个索引
            value：值
            axis： None 全部一维化 在插入。或0,1,2
        # axis=  None 全部扁平化 在插入
        # axis = 0
          shape(4,5) => shape(A,B) axis=0 则数据必须为5(B)列                                                                  
          np.insert(shape(4,5),1|[1]|(1),value,0)
          1|[1]|(1) => 插入一个位置 value为 (?,B) 或者转为(?,B)的数据 。如 value=9 ,value=shape(3,B)
         	[0,3]|(0,1)=>插入2(C)个位置 value为(C,B) 或可转为(C,B)的数据。 如 value 10,value=shape(2,B) ,shape(1,B)
        # axis = 1
           shape(4,5) => shape(A,B) axis=1 则数据必须为4(A)行
           np.insert(shape(4,5),1|[1]|(1),value,1)   
           1|[1]|(1) => 插入一个位置 value为 (A,?) 或者转为(A,?)的数据 。如 value=9 ,value=shape(A,4)
           [0,1,3]|(0,1,2) => 插入3(C)个位置 value为(A,C) 或可转为(A,C)的数据。 如 value= 10 ,shape(A,1)
                                                                            
     # np.dot 计算两个数组的点积 
         结果:C(i,j)等于A中第i行所有元素跟B中第j列所有元素一一对应的乘积之和
         np.dot([0,1],[1,2]) 一维数组为内积 对应相乘相加
         np.dot([[0,1],[2,3]],[[3,4],[4,5]])多维数组为矩阵积                                                 
             =>shape(2,2)
               [[ 4  5] [18 23]] 
               (0,0)=>第一个数组0行(0,1) 第二个数组0列[3，4] =>0*3 + 1*4 = 4
  			(1,1)=>第一个数组1行(2，3) 第二个数组1列列[4，5] =>2*4+3*5 = 23
      # np.dnarray.T  把数组进行转置
          shape(2,10).T = > shape(10,2)
              [
                  [0,1],
                  [2,3]
              ].T      
              [
                  [0,2],
                  [1,3]
              ]                                                                 
          不同于                                                                  
          shape(2,10).reshape(10,2).reshape(4,5) 会把数组一维化再进行求取
      # np.mean(shape(m,n),axis=None,) 求平均值
          axis=None 求所有平均值 返回一个值                                                                 axis = 0 沿着第一轴求平均值 求各列的平均值 shape(1,n)
          axis = 1 沿着第二轴求平均值 求各行的平均值 shape(m,1)                                                                  
                                                                            
  ```

  

* 切片

  ​	

  ```
  结构：ndarray[,] 逗号分隔表示多个操作
  	ndarray[3,4] 表示取3行，在其基础上取第四列
  	分步：第一步的结果为第二步的初始值
  切片：ndarry[:] === ndaarry[::] === ndaarry[::1]
  	一步操作对应这[起始index:结束index:步长]
  	分步：第一步的结果为第二步的初始值
  索引：
  	>索引一个行 返回的是一个行向量
  	>索引一个列 针对(第一步索引行)每一行的(列)索引 返回的也是一个行向量。 列索引的个数 要和 第一步行索引一致
  	分步：第一步的结果为第二步的初始值
  	ndarray[[1,2]] 表示对第一轴取第一行和第二行
  	ndarray[[1,2]A,[3,4]B]  len(A) 要等于 len(B)
  		第一步取横轴的第一行和第二行
  		第二步分别取第一行的第3列，第二行的第4列
  		=> [A,B] A == 1行3列, B== 2行4列
  	ndarray[[0,1],[1,2],[0,0]] =>[(0行,1列,0纵),(1,2,0纵)]
  	
  切片+索引:
  	触发广播
  np.newaxis 
  	见下
  ```

  

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
    #切片 [:::]
    dome_data[2,3] =>15
    dome_date[1]
    =>dome_data[1,:]
    =>dome_data[1,...] = > [ 6  7  8  9 10 11]
    
    dome_date[1:] ==dome_data[1::] == dome_data[1::1] 沿着第一轴 从第一个开始取 到最后一个 步长为1
    dome_data[0:2,1:3] =第一步[0:2]=>[[0  1  2  3  4  5],[6  7  8  9 10 11]]=第二步[1:2]=>[[1,2], [7,8]]
    
    #索引 [[2,3],[1,2]]
        dome_data[:,1] == dome_data[:,1:] != dome_data[:,[1]]
        索引列:
           dome_data[:2,1:3] ==>[[1,2], [7,8]]
           dome_data[[0,1],[1,3]]
        	==>[(0行1列),(1行,3列)]
            ==>[1,9]
           类似 === dome_data[[0,1],[[1],[3]]]
    # 索引+切片
    	dome_data[[0,1],1:3] 不触发广播
    	dome_data[0:2,[1,3]] 触发广播
       	==>dome_data[0:2,[[1,3],[1,3]]
    # np.newaxis = None 在指定位置增加一维
        dome_data[None] =>shape(4,6)===>shape(1,4,6)
        dome_data[:,None]=>shape(4,6)===>shape(4,1,6)
    ```

  * 对多维数组进行 **迭代（Iterating）** 是相对于第一个轴完成的。使用flat属性对所有属性迭代

    ```python
    for row in data:
    	pass
    for item in data.flat
    	pass
    ```

*  对照表 [Link]

|           函数           | 说明                                                         |
| :----------------------: | ------------------------------------------------------------ |
|       numpy.copyto       |                                                              |
|       numpy.shape        | 得到shape                                                    |
|      numpy.reshape       | 重置shape                                                    |
|       numpy.ravel        | 扁平化 为一维数组 试图                                       |
|    numpy.ndarray.flat    | 得到该数组的一维对象 试图                                    |
|  numpy.ndarray.flatten   | 数组一维化为 拷贝                                            |
|      numpy.moveaxis      |                                                              |
|      numpy.rollaxis      |                                                              |
|      numpy.swapaxes      |                                                              |
|     numpy.ndarray.T      | 获取该数组的转置                                             |
|     numpy.transpose      | 获取该数组的转置                                             |
|    "numpy.atleast_1d     |                                                              |
|    "numpy.atleast_2d     |                                                              |
|    "numpy.atleast_3d     |                                                              |
|     "numpy.broadcast     |                                                              |
|   "numpy.broadcast_to    |                                                              |
|  numpy.broadcast_arrays  |                                                              |
|    numpy.expand_dims     |                                                              |
|      "numpy.squeeze      |                                                              |
|      "numpy.asarray      |                                                              |
|    "numpy.asanyarray     |                                                              |
|     "numpy.asmatrix      |                                                              |
|     "numpy.asfarray      |                                                              |
|  "numpy.asfortranarray   |                                                              |
| "numpy.ascontiguousarray |                                                              |
| "numpy.asarray_chkfinite |                                                              |
|     "numpy.asscalar      |                                                              |
|      "numpy.require      |                                                              |
|    "numpy.concatenate    |                                                              |
|       "numpy.stack       | 堆叠(合并)数组                                               |
|       "numpy.block       |                                                              |
|      "numpy.vstack       | 堆叠(合并)数组 第一轴堆叠                                    |
|      "numpy.hstack       | 堆叠(合并)数组 第二轴堆叠                                    |
|      "numpy.dstack       | 堆叠(合并)数组 第三轴堆叠                                    |
|   "numpy.column_stack    | ~==hstack                                                    |
|     "numpy.row_stack     | === vstack                                                   |
|       "numpy.split       | 拆分为小数组                                                 |
|    "numpy.array_split    | 等于split 区别在于可以拆为多个长度不同的数组 (8->3)=>(3,2,2) |
|      "numpy.dsplit       | 第三轴切割                                                   |
|      "numpy.hsplit       | 第二轴切割                                                   |
|      "numpy.vsplit       | 第一轴切割                                                   |
|       "numpy.tile        |                                                              |
|      "numpy.repeat       |                                                              |
|      "numpy.delete       |                                                              |
|      "numpy.insert       |                                                              |
|      "numpy.append       | 拼接 堆叠数组                                                |
|      "numpy.resize       |                                                              |
|    "numpy.trim_zeros     |                                                              |
|      "numpy.unique       |                                                              |
|       "numpy.flip        |                                                              |
|      "numpy.fliplr       |                                                              |
|      "numpy.flipud       |                                                              |
|      "numpy.reshape      |                                                              |
|       "numpy.roll        |                                                              |
|       "numpy.rot90       |                                                              |

