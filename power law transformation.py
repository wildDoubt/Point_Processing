# python 3.8
# s = c*r^γ
# c, γ: positive constants
# s, r: output, input values
import cv2
import numpy as np
from matplotlib import pyplot as plt

images = [cv2.imread('src/2. Power law transformation/img1.tif', 0),
          cv2.imread('src/2. Power law transformation/img2.tif', 0),
          cv2.imread('src/2. Power law transformation/img3.tif', 0),
          cv2.imread('src/2. Power law transformation/img4.tif', 0)]
gamma_images = []
gamma = [0.4, 2.2]
for g in gamma:
    gamma_images.append([np.array(255 * (image / 255) ** g, dtype='uint8') for image in images])

for j in range(len(gamma)):
    for i in range(4):
        dst = np.hstack((images[i], gamma_images[j][i]))
        # cv2.imshow('2. Power law transformation ' + str(i + 1) + " gamma = " + str(gamma[j]), dst)
        cv2.imwrite('result/2. Power law transformation/gamma'
                    + str(gamma[j]) + '/img' + str(i + 1) + '.png', gamma_images[j][i])
# cv2.waitKey()
# cv2.destroyAllWindows()
