import numpy as np
#彩色噪点图
random_matrix = np.random.randint(0,256,(300,300,3)).astype(np.uint8)
print(random_matrix.shape)
print(random_matrix.dtype)