from MODIS_API import MODIS_Module


# Let's look at the tile containing Chicago, IL, on May 15, 2019 (day of year 135)
product = 'MCD43A4'  # Surface reflectance
dayNum = '2011252'
lat = 42.124753
lon = -81.769110
remove_files_on_finish = False

# uncomment below line if you need to re-query images from the API
# MODIS_Module.download_data_to_folder(product, lat, lon, dayNum, remove_files_on_finish)

rgb = MODIS_Module.get_modis_bands_array()  # 2400 x 2400 x 3

# This just combines the original .tiff files into a false-colour image
# MODIS_Module.show_modis_image()

# chi's code - calculate ratios(rgb) -> output 2400 x 2400 x 5
# [0] is r band
# [1] is g band
# [2] is b band
# [3] is a ratio band NDVI
# [4] is a ratio band EVI

# reshape 2400 (x) x 2400 (y) x 5 (z) to [x*y, z]

# bens code - k_means_method.create_labels_colors(reshaped array)
# returns colours, labels

# rgb = rgbbw.create_rgbwb_class_colors(colours)

# blurs 2d image
# aerjays code - polarizing the image(flattened image, labels, rgb)
#  resize image to 2400 x 2400 x 5


