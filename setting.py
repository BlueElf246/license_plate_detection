params = {}
params['color_space'] = 'RGB'  # Can be RGB, HSV, LUV, HLS, YUV, YCrCb
params['orient'] = 9  # HOG orientations
params['pix_per_cell'] = 4  # HOG pixels per cell
params['cell_per_block'] = 2  # HOG cells per block
params['hog_channel'] = 'ALL'  # Can be 0, 1, 2, or "ALL"
params['spatial_size'] = (16, 16)  # Spatial binning dimensions
params['hist_bins'] = 16  # Number of histogram bins
params['spatial_feat'] = True  # Spatial features on or off
params['hist_feat'] = True  # Histogram features on or off
params['hog_feat'] = True  # HOG features on or off
params['size_of_window']=(108,36,3)
params['test_size']=0.8


win_size={}
win_size['scale_0']=(375,1000,0.5)
win_size['scale_1']=(375,1000,0.9)
win_size['scale_2']=(375,1000,1.4)
win_size['scale_3']=(375,1000,2.2)
win_size['thresh']=100
win_size['overlap_thresh']= 0.05
# 0.5, 1.3
win_size['use_scale']=(0,1,2,3)