```python
import numpy as np
np.random 随机数对象
# np.random.rand(d,d0,d1)  [0, 1)之间均匀分布的随机数，d行d0列 d1。
	# 作用： 产生一个给定形状的数组（其实应该是ndarray对象或者是一个单值），数组中的值服从[0, 1)之间的均匀分布。
    # 参数：d0, d, ..., dn : int，可选。如果没有参数则返回一个float型的随机数，该随机数服从[0, 1)之间的均匀分布。
	# 返回值：ndarray对象或者一个float型的值
    np.random.rand(3, 2)  
    np.random.rand() 一个0-1随机float

 # np.random.uniform(low=0.0, high=1.0, size=None)
	# 作用：返回一个在区间[low, high)中[均匀分布]的数组，size指定形状。
    # 参数：low high float型或者float型的类数组对象 。 size：int型或int型元组 不指定生成一个随机数
    np.random.uniform(1, 10, (3, 2)) [1,10) 数组形状为(3,2)的 
          [[5.16545387 6.3769087 ]
            [9.98964899 7.88833885]
            [1.37173855 4.19855075]]  均匀分布                          
    np.random.uniform(1, 10) 一个随机数
 
# np.random.randn(d0, d1, ..., dn)生成一个标准状态分布数组
	# 作用：返回一个指定形状的数组，数组中的值服从标准正态分布（均值为0，方差为1）。
	# 参数：d0, d, ..., dn : int，可选。如果没有参数，则返回一个服从标准正态分布的float型随机数。
    # 返回值：ndarray对象或者float
	np.random.randint(3, 3)  所有数组满足正态分布
     array([[ 2.29864491,  0.52591291, -0.80812825],
       [ 0.37035029, -0.07191693, -0.76625886],
       [-1.264493  ,  1.12006474, -0.45698648]])
 # randint(low, high, size, dtype) 生成维度size大小的产生[随机整数]数组 
     np.random.randint(1,10,(3,3))                               
       [[1 8 0]
        [4 0 1]
        [6 7 2]]       
 # random ranf sample =>  random_sample 在[0,1）内产生随机数
     np.random_sample(1)  [0.37035029]     
     np.random_sample(2,3)
```



*  ndarray操作
  * 所有操作都是是针对元素 np.ones((2,2)) - 1 => np.zeros((2,2),dtype=np.int16)
  * 操作都是针对所有元素 `axis` 参数可以指定轴 对应shape 的维度   见属性含义
  * 操作数组的类型对应于更一般或更精确的数组 int + float =>float