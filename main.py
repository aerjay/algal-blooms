from MODIS_API import MODIS_Module


# Let's look at the tile containing Chicago, IL, on May 15, 2019 (day of year 135)
product = 'MCD43A4'  # Surface reflectance
dayNum = '2011252'
lat = 42.124753
lon = -81.769110
remove_files_on_finish = False

# comment out if files already exist in MODIS_API/MODIS_Images
# MODIS_Module.download_data_to_folder(product, lat, lon, dayNum, remove_files_on_finish)

MODIS_Module.show_modis_image()
