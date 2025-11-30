import cv2
import numpy as np
#创建全黑画布 然后中间染白 切片
canvas = np.zeros((400,400),dtype=np.uint8)#图像处理用unit8
#代替双向循环canvas[y1:y2,x1:x2]行，列
canvas[100:300,100:300] = 255
print(canvas.shape)
print(canvas.dtype)
print(canvas[0,0])
print(canvas[200,200])

#彩色噪点图
random_matrix = np.random.randint(0,256,(300,300,3)).astype(np.uint8)
print(random_matrix.shape)
print(random_matrix.dtype)

#显示黑白图和彩色噪点图
cv2.imshow("B/W Square",canvas)
cv2.waitKey(0)
cv2.imshow("Color Noise",random_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()