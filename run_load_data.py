import os

from load_data import *
from setting import params
import matplotlib.image as mpimg
import numpy as np
import random
#os.chdir("/Users/datle/Desktop/license_plate_detection")
car, non_car= load_dataset()
random.shuffle(car)
random.shuffle(non_car)
car=car[:2000]
non_car=non_car[:2000]
os.chdir("/Users/datle/Desktop/license_plate_detection")
car_feature=extract_feature(car, params['color_space'])
os.chdir("/Users/datle/Desktop/nhan_dien_xe")
non_car_feature= extract_feature(non_car, params['color_space'])
X,y= combine(car_feature, non_car_feature)
sc, X_scaled= normalize(X)
X_train, X_test, y_train, y_test= split(X_scaled, y)
model= train_model(X_train, X_test, y_train, y_test)
save_model('lp_detect.p', model, sc, params=params,y=y)