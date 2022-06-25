import cv2
from itertools import cycle
import random

from cv2 import setWindowProperty
index = 0
img_list = []
for i in range(1,97):
    img_path = "/home/xiaoguzai/图片/学习资料man1/照片"+str(i)+".jpg"
    img_list.append(img_path)
index = 0
random.shuffle(img_list)

while 1:
	img = cv2.imread(img_list[index])
	index = index+1
	cv2.namedWindow('myPicture',cv2.WINDOW_FULLSCREEN)
	cv2.moveWindow('myPicture',850,10)
	cv2.setWindowProperty('myPicture',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_AUTOSIZE)
	cv2.resizeWindow('myPicture',1000,1000)
	cv2.imshow('myPicture',img)
	cv2.waitKey(180000)
	
cv2.destroyAllWindows()
