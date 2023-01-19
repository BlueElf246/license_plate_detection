import os
os.chdir("/Users/datle/Desktop/license_plate_detection")
import matplotlib.image as mpimg
import glob
from sliding_window1 import *
import pickle
from setting import win_size
import cv2
import numpy as np
imgs=[]
params= load_classifier()
data_test= glob.glob("dataset_test/images/*.png")
for img in data_test:
    i= mpimg.imread(img)
    name=img.split('/')
    imgs.append((name[-1],i))
os.chdir("/Users/datle/Desktop/license_plate_detection/result")
text= open('text.txt','a')
for img in imgs[:2]:
    bbox, bbox_nms= find_car_multi_scale(img[1],params, win_size)
    im= img[1].copy()
    heatmap = draw_heatmap(bbox, img[1])
    heatmap_thresh = apply_threshhold(heatmap, thresh=win_size['thresh'])
    bbox_heatmap = get_labeled(heatmap_thresh)
    img_final= draw(im, bbox_heatmap)
    text.writelines(str(img[0])+str(bbox_heatmap)+'\n')
    cv2.imwrite(img[0],img_final)







