# python 3.8
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Import images
img = [cv2.imread('./src/1. HE/img_2nd_from_top.jpg', 0), cv2.imread('./src/1. HE/img_bottom_left.jpg', 0),
       cv2.imread('./src/1. HE/img_third_from_top.jpg', 0), cv2.imread('./src/1. HE/img_top_left.jpg', 0)]

# Apply histogram equalization
HE_img = [cv2.equalizeHist(beforeImage) for beforeImage in img]

# Print images
for i in range(4):
    dst = np.hstack((img[i], HE_img[i]))
    cv2.imshow('img', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Check histogram changes
# fig, ax = plt.subplots(4, 2)
# for a in range(len(ax)-2):
#     for b in range(len(ax[a])):
#         index = a.__lshift__(1) | b
#         ax[index, 0].set_title("Before fig" + str(index+1))
#         ax[index, 0].hist(img[index].flatten(), 256, [0, 256], color='r')
# for a in range(2, len(ax)):
#     for b in range(len(ax[a])):
#         index = (a%2).__lshift__(1) | (b%2)
#         ax[index, 1].set_title("After fig" + str(index + 1))
#         ax[index, 1].hist(HE_img[index].flatten(), 256, [0, 256], color='r')
# plt.xlim([0, 256])
# plt.show()
