# python 3.8
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./src/3. Negative/img.tif', 0)
print(image)
negative_image = 255 - image
print(negative_image)
dst = np.hstack((image, negative_image))
cv2.imwrite('result/3. Negative/img.png', negative_image)
# cv2.imshow('3. Negative Test', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

fig, ax = plt.subplots(1, 2)
fig.tight_layout()
ax[0].set_title('Before fig')
ax[0].hist(image.flatten(), 256, [0, 256], color='r')
ax[1].set_title('After fig')
ax[1].hist(negative_image.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.savefig('result/3. Negative/histogram/히스토그램 비교 사진.png')

