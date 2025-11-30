import numpy as np
#创建全黑画布 然后中间染白 切片
canvas = np.zeros((400,400),dtype=np.uint8)#图像处理用unit8
#代替双向循环canvas[y1:y2,x1:x2]行，列
canvas[100:300,100:300] = 255
print(canvas.shape)
print(canvas.dtype)
print(canvas[0,0])
print(canvas[200,200])