import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('rkoirala_hard.jpg')
blue, green, red = cv2.split(img)


cv2.imshow("Image", img)

histblue = (cv2.calcHist([blue], [0], None, [256], [0, 256]))
histgreen = (cv2.calcHist([green], [0], None, [256], [0, 256]))
histred = (cv2.calcHist([red], [0], None, [256], [0, 256]))

fig, im = plt.subplots(3)
fig.suptitle('RGB Chart')

im[0].plot(histred, 'tab:red')
im[0].set_title("RED")

im[1].plot(histgreen, 'tab:green')
im[1].set_title("Green")

im[2].plot(histblue)
im[2].set_title("Blue")

plt.show()