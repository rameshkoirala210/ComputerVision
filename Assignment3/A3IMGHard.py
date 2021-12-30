import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('rkoirala_hard.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

identity = np.array(([0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 0.0]), np.float32)
edgeDetection = np.array(([-1.0, -1.0, -1.0],
                          [-1.0, 8.0, -1.0],
                          [-1.0, -1.0, -1.0]), np.float32)
gb = np.ones((5, 5), np.float32)/25

outputI = cv2.filter2D(img, -1, identity)
outputED = cv2.filter2D(img, -1, edgeDetection)
outputGB = outputED = cv2.filter2D(img, -1, gb)

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(outputI)
plt.title("Identity Image")

plt.subplot(2, 2, 3)
plt.imshow(outputED)
plt.title("Edge Detection Image")

plt.subplot(2, 2, 4)
plt.imshow(outputGB)
plt.title("Gaussian Blur(5x5) Image")

plt.show()
