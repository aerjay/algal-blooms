from MODIS_API import MODIS_Module
from MODIS_API import RatioCalculation
from MODIS_API import k_means_method
from MODIS_API import rgbbw
import numpy as np

# Let's look at the tile containing Chicago, IL, on May 15, 2019 (day of year 135)
product = 'MCD43A4'  # Surface reflectance
dayNum = '2011252'
lat = 42.124753
lon = -81.769110
remove_files_on_finish = False

# uncomment below line if you need to re-query images from the API
# MODIS_Module.download_data_to_folder(product, lat, lon, dayNum, remove_files_on_finish)

rgb = MODIS_Module.get_modis_bands_array()  # 3 x 2400 x 2400

# This just combines the original .tiff files into a false-colour image
# MODIS_Module.show_modis_image()

# chi's code - calculate ratios(rgb) -> output 5 x 2400 x 2400
rgb = RatioCalculation.add_ratio_bands(rgb)

rgb = rgb*10
# [0] is IR band
# [1] is Red band
# [2] is Blue band
# [3] is a ratio band NDVI
# [4] is a ratio band EVI

# bens code - k_means_method.create_labels_colors(reshaped array)
# returns colours, labels
cluster, label = k_means_method.create_labels_colors(rgb)

# rgb = rgbbw.create_rgbwb_class_colors(colours)
rgb = rgbbw.create_rgbwb_class_colors(cluster)

# blurs 2d image
# aerjays code - polarizing the image(flattened image, labels, rgb)
rgb = rgbbw.paint_by_colours(label, cluster, 2400, 2400)
#  resize image to 5 x 2400 x 2400

medianBlur = rgb.reshape((rgb.shape[0], rgb.shape[1], rgb.shape[2]))

RatioCalculation.show_image(medianBlur)


