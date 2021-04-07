from MODIS_API import MODIS_Module
from MODIS_API import RatioCalculation
from MODIS_API import k_means_method
from MODIS_API import rgbbw
from MODIS_API import graphCSV
import matplotlib.pyplot as plt
import numpy as np
import cv2

# Let's look at the tile containing Chicago, IL, on May 15, 2019 (day of year 135)
#
product = 'MCD43A4'  # Surface reflectance
dayNum = '2011246'
lat = 42.124753
lon = -81.769110

# for gotland algae bloom
# product = 'MCD43A4'  # Surface reflectance
# dayNum = '2005194'
# lat = 57.4684
# lon = 18.4867
remove_files_on_finish = True

# uncomment below line if you need to re-query images from the API
rgb = MODIS_Module.download_data_to_folder(product, lat, lon, dayNum, remove_files_on_finish)

# This just combines the original .tiff files into a false-colour image
MODIS_Module.show_image(rgb)

# chi's code - calculate ratios(rgb) -> output 5 x 2400 x 2400
rgb = RatioCalculation.add_ratio_bands(rgb)

# show only the ratio band
plt.imshow(rgb[3])
plt.show()

# save that ratio band image
# cmap = plt.get_cmap('jet')
# rgba_img = cmap(rgb[3])
# rgb_img = np.delete(rgba_img, 3, 2)
# cv2.imwrite('NDVI_' + dayNum, rgb_img)

rgb_copy = rgb * 25
# no modis aqua data, this is terra data
# [0] is IR band (MODIS 5)
# [1] is Red band (MODIS 1)
# [2] is Green band (MODIS 4)
# [3] is a ratio band NDVI
# [4] is a ratio band EVI

# bens code - k_means_method.create_labels_colors(reshaped array)
# returns colours, labels
cluster, label = k_means_method.create_labels_colors(rgb_copy)

# rgb = rgbbw.create_rgbwb_class_colors(colours)
false_colour_legend = rgbbw.create_rgbwb_class_colors(cluster)

# aerjays code - polarizing the image(flattened image, labels, rgb)
false_colour = rgbbw.paint_by_colours(label, false_colour_legend)

#  resize image to 5 x 2400 x 2400
# false_colour = false_colour.reshape((rgb.shape[0], rgb.shape[1], rgb.shape[2]))
# np.clip(false_colour, 0, 1, false_colour)
plt.imshow(false_colour)
plt.show()

# james code - calculating average NDVI & red reflectance for plots

#### We need to figure out which colour cluster labels as water and put that index number into graphData()
timeseriesdata = np.zeros(6, dtype=float)
for i in range(6):
    timeseriesdata[i] = graphCSV.graphData(rgb, label, 2)

np.savetxt(lat + "-" + lon + ".csv", timeseriesdata, delimiter=",")
RatioCalculation.show_image(false_colour)
