# python 3.8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Import images
images = [cv2.imread('src/1. HE/img1.jpg', 0), cv2.imread('src/1. HE/img2.jpg', 0),
          cv2.imread('src/1. HE/img3.jpg', 0), cv2.imread('src/1. HE/img4.jpg', 0)]

# Apply histogram equalization
HE_images = [cv2.equalizeHist(image) for image in images]

# Print images
for i in range(4):
    dst = np.hstack((images[i], HE_images[i]))
    # cv2.imshow('1. Histogram Equalization '+str(i+1), dst)
    cv2.imwrite('result/1. HE/HE_images/HE_img'+str(i+1)+'.jpg', HE_images[i])
# cv2.waitKey()
# cv2.destroyAllWindows()

# Check histogram changes
fig, ax = plt.subplots(4, 2)
fig.tight_layout()
for a in range(len(ax)-2):
    for b in range(len(ax[a])):
        index = a.__lshift__(1) | b
        ax[index, 0].set_title("Before fig" + str(index+1))
        ax[index, 0].hist(images[index].flatten(), 256, [0, 256], color='r')
for a in range(2, len(ax)):
    for b in range(len(ax[a])):
        index = (a%2).__lshift__(1) | (b%2)
        ax[index, 1].set_title("After fig" + str(index + 1))
        ax[index, 1].hist(HE_images[index].flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
# plt.show()
plt.savefig('result/1. HE/histogram/히스토그램 비교 사진.png')