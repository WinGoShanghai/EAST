from PIL import Image
import os
import cv2
import time
import matplotlib.pyplot as plt
def label2picture(cropImg,framenum,tracker):
    pathnew ="/home/yimu/Desktop/products-images-medium/"
    # cv2.imshow("image", cropImg)
    # cv2.waitKey(1)
    if (os.path.exists(pathnew + tracker)):
        cv2.imwrite(pathnew + tracker+'\\'+framenum + '.jpg', cropImg,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
 
    else:
        os.makedirs(pathnew + tracker)
        cv2.imwrite(pathnew + tracker+'\\'+framenum + '.jpg', cropImg,[int(cv2.IMWRITE_JPEG_QUALITY), 100])
 
f = open("E:\\hypotheses.txt","r")
lines = f.readlines()
for line in lines:
    li  = line.split(',')
    print(li[0],li[1],li[2],li[3],li[4],li[5])
    filename = li[0]+'.jpg'
    img = cv2.imread("E:\\DeeCamp\\img1\\" + filename)
    crop_img = img[int(li[3][:-3]):(int(li[3][:-3]) + int(li[5][:-3])),
               int(li[2][:-3]):(int(li[2][:-3]) + int(li[4][:-3]))]
    # print(int(li[2][:-3]),int(li[3][:-3]),int(li[4][:-3]),int(li[5][:-3]))
    label2picture(crop_img, li[0], li[1])

