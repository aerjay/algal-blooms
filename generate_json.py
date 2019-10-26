from MODIS_API import MODIS_Module
from MODIS_API import RatioCalculation
from MODIS_API import k_means_method
from MODIS_API import rgbbw
from MODIS_API import graphCSV
import matplotlib.pyplot as plt
import numpy as np
import json


# ratio_band is a single array of ratios
def generate_json(ratio_band):
    #convert arrays to list so json can serialize
    ir = ratio_band[0].tolist()
    red = ratio_band[1].tolist()
    green = ratio_band[2].tolist()

    data = {"IR": ir, "Red": red, "Green": green}

    with open('ratios.json', 'w') as outfile:
        json.dump(data, outfile)


# ratio_bands is an array of ratios arrays
# dates is an array of dates corresponding to the ratio array
def generate_json(ratio_bands, dates):
    #convert arrays to list so json can serialize
    ir = ratio_bands[0].tolist()
    red = ratio_bands[1].tolist()
    green = ratio_bands[2].tolist()

    data = {}
    data[dates[0]] = []
    data[dates[0]].append({"IR": ir, "Red": red, "Green": green})

    with open('ratios_dates.json', 'w') as outfile:
        json.dump(data, outfile)


### Code to example run ###

#Let's look at the tile containing Chicago, IL, on May 15, 2019 (day of year 135)
product = 'MCD43A4'  # Surface reflectance
dayNum = '2011252'
lat = 42.124753
lon = -81.769110
date = ["05/15/2019"]

# for gotland algae bloom
# product = 'MCD43A4'  # Surface reflectance
# dayNum = '2005194'
# lat = 57.4684
# lon = 18.4867
remove_files_on_finish = False

# uncomment below line if you need to re-query images from the API
# MODIS_Module.download_data_to_folder(product, lat, lon, dayNum, remove_files_on_finish)

rgb = MODIS_Module.get_modis_bands_array()  # 3 x 2400 x 2400

# This just combines the original .tiff files into a false-colour image
# MODIS_Module.show_modis_image()

# chi's code - calculate ratios(rgb) -> output 5 x 2400 x 2400
rgb = RatioCalculation.add_ratio_bands(rgb)
band_ratios = rgb * 25

generate_json(rgb[3], date)
