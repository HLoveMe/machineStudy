# NumPy [DOC](https://www.numpy.org.cn/user/quickstart.html) [Dome](https://blog.csdn.net/a373595475/article/details/79580734)

* 数组的算数和逻辑运算。
* 傅立叶变换和用于图形操作的例程。
* 与线性代数有关的操作。 NumPy 拥有线性代数和随机数生成的内置函数。

# numpy.ndarray

* ndarray 的 N 维数组类型。 它描述相同类型的元素集合

* ndarray中的每个元素在内存中使用相同大小的块。 ndarray中的每个元素是数据类型对象的对象（称为 dtype）

  ```tex
  shape - 数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有 n 行和 m 列的矩阵，shape 将是 (n,m)
  ndim - 数组的轴（维度）的个数 np.array(24).reshape(2,3,4).ndim  3 
  size - 数组元素总数 为shape 元素乘积
  dtype - 一个描述数组中元素类型的对象。 n每个元素的大小是固定的 可以为内置类型 也可以为自定义类型
  data - 该缓冲区包含数组的实际元素
  ```

  


* 创建
  * numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

    * object [任何暴露数组接口方法的对象]都会返回一个数组或任何（嵌套）序列。
    *  dtype 数组的所需数据类型，可选。
    * copy 可选，默认为true，对象是否被复制。
    * order C（按行）、F（按列）或A（任意，默认）。
    * subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
    * ndmin 指定返回数组的最小维数。

    ```python
    import numpy as np
    # array
    np.array(13)
    np.array([1,2,3,4])
    np.array([[1,2],[1,3],[1,4]])
    np.array([(1,2,3),(1.1,2,3)])
    
    # empty(shape,dtype,order) 创建一个指定shape 的数组 值为随机值
    # empty_like(ndarray,dtype,order) 创建一个和指定数组相同shape的空数组
    	np.empty((2,3),dtype=np.float64)
    # zeros(shape, dtype = float, order = 'C') 创建指定shape的数组 值为0
    # zeros_like(ndarray,dtype,order) 创建一个和指定数组相同shape的0数组
    # ones(shape, dtype = float, order = 'C') 创建指定shape的数组 值为1
    # ones_like(ndarray,dtype,order) 创建一个和指定数组相同shape的1数组
    	np.zeros((19,),dtype=np.int8)	
    # asarray(a, dtype = None, order = None) a 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
    	np.asarray(((1,2),(2,3)))
    # arange(start,end,step)  创建数组 >=start开头 end< 结尾 step步长
     	np.arange(1,10,2) =>1,3,5,7,9
     	np.arange(1,2,0.2)=> 由于精度问题 不能发准确的预测元素数量 建议使用linspace
    # linspace(start,end,num) 创建数组 >=start开头 end< 结尾 数据数量为num 默认为float64
    	np.linspace(1,2,7)
    
    # eye(N, M=N, k=0, dtype=<class 'float'>, order='C') 创建一个对角线为1 其他元素为0的矩阵
    # eye_like
    	N 为 多少行 ，M (默认等于N)为多少列。
         K 为对角线起始索引（第一行 第K个为对角线开始）
         np.eye(5,5,k=0)
            [[1 0 0 0 0]
             [0 1 0 0 0]
             [0 0 1 0 0]
             [0 0 0 1 0]
             [0 0 0 0 1]]
          np.eye(5,5,k=1)
           [[0 1(K) 0 0 0]
             [0 0 1 0 0]
             [0 0 0 1 0]
             [0 0 0 0 1]
             [0 0 0 0 0]]
    ```
    
    
    
    ```python
    #随机数
    
    	
    ```
    
    ```python
    np.array([22,12],dtype=complex) 复数
    np.array([1.0,2.3.0],dtype=np.float64)
    # dtype
    np.dtype('int8') np.int8 np.dtype('i1')
    np.dtype('int16') np.int16 np.dtype('i2')
    np.dtype('int32') np.int32 np.dtype('i3')
    
    # 自定义
    Student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    data = np.array([('rolf', 21, 75),
                      ('anna', 19, 65),
                      ('ethan', 18, 75)], dtype=Student)
    data['age']=>nnumpy.ndarray([21,19,18])
    
    1.	bool_ 存储为一个字节的布尔值（真或假）
    2.	int_ 默认整数，相当于 C 的long，通常为int32或int64
    3.	intc 相当于 C 的int，通常为int32或int64
    4.	intp 用于索引的整数，相当于 C 的size_t，通常为int32或int64
    5.	int8 字节（-128 ~ 127）
    6.	int16 16 位整数（-32768 ~ 32767）
    7.	int32 32 位整数（-2147483648 ~ 2147483647）
    8.	int64 64 位整数（-9223372036854775808 ~ 9223372036854775807）
    9.	uint8 8 位无符号整数（0 ~ 255）
    10.	uint16 16 位无符号整数（0 ~ 65535）
    11.	uint32 32 位无符号整数（0 ~ 4294967295）
    12.	uint64 64 位无符号整数（0 ~ 18446744073709551615）
    13.	float_ float64的简写
    14.	float16 半精度浮点：符号位，5 位指数，10 位尾数
    15.	float32 单精度浮点：符号位，8 位指数，23 位尾数
    16.	float64 双精度浮点：符号位，11 位指数，52 位尾数
    17.	complex_ complex128的简写
    18.	complex64 复数，由两个 32 位浮点表示（实部和虚部）
    19.	complex128 复数，由两个 64 位浮点表示（实部和虚部）
    
    ```
    
    ```python
    
    ```
    
    