import cv2
import numpy as np

#彩色噪点图
random_matrix = np.random.randint(0,256,(300,300,3)).astype(np.uint8)
print(random_matrix.shape)
print(random_matrix.dtype)

cv2.imshow("Color Noise",random_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()

success = cv2.imwrite("noise_art.jpg",random_matrix)
if success:
    print("success")