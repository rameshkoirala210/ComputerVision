import cv2
import matplotlib.pyplot as plt
import numpy as np

# Instructions to run your code
# open python Ide (I used pycharm)
# run the program ans you get RGB graph
# I saved it and named it as easy, medium and hard chart

# Description of what I did are in comments

# First I got the image and set it as img after that I split the image to blue, green, red.
img = cv2.imread('rkoirala_easy.jpg')
blue, green, red = cv2.split(img)

cv2.imshow("Image", img)
# I was watching a video on opencv and saw it had calcHist function and since instructions said "you are free to do
# whatever you want" I decided to use calcHist to calculate and normalize the frequency by multiplying it by 256*256
histblue = (cv2.calcHist([blue], [0], None, [256], [0, 256])) / (256 * 256)
histgreen = (cv2.calcHist([green], [0], None, [256], [0, 256])) / (256 * 256)
histred = (cv2.calcHist([red], [0], None, [256], [0, 256])) / (256 * 256)

# This makes it so that there are 3 plots and set the title as RGB Chart
fig, im = plt.subplots(3)
fig.suptitle('RGB Chart')

# This Plots the graph, first it creates the red frequency one, then green and blue in the end.
# I gave each histogram their specific color and also labeled it.
im[0].plot(histred, 'tab:red')
im[0].set_title("RED Plot")

im[1].plot(histgreen, 'tab:green')
im[1].set_title("Green Plot")

im[2].plot(histblue)
im[2].set_title("Blue Plot")

# This commented out makes it so all three graph would be plotted it in one,
# if you change fig, im = plt.subplots(3) <-- 3 to 4 it will plot all three in one

# im[3].set_title("All 3 RGB Chart")
# im[3].plot(histblue)
# im[3].plot(histgreen)
# im[3].plot(histred)

# This makes it so there is some space in between each chart and it also shows you the charts
plt.tight_layout()
plt.show()
