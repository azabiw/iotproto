import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('kuva1.jpg',0)
img2 = cv2.imread('kuva2.jpg',0)
plt.imshow(img2),plt.savefig('foo.png')
orb = cv2.ORB_create()
keypoints1 = orb.detect(img1,None)
keypoints2 = orb.detect(img2, None)
keypoints1, descriptions1 = orb.compute(img1, keypoints1)
keypoints2, descriptions2 = orb.compute(img2, keypoints2)
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(descriptions1,descriptions2) 
img3 = cv2.drawMatches(img1,keypoints1,img2,keypoints2,matches,None,flags=2)
plt.imsave('vertailu.png', img3)

