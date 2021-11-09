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
    np.array(13)
    np.array([1,2,3,4])
    np.array([[1,2],[1,3],[1,4]])
    np.array([(1,2,3),(1.1,2,3)])
    ```

    ```python
    np.array(12,dtype=complex) 复数
    ```

