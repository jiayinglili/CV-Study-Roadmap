import numpy as np
list1 = [10,20,30]
data1 = np.array(list1) #转化成numpy
print(data1.shape,data1.dtype)#
data1 -= 5   #向量化能力 作为一个整体-5
print(data1)
