import os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__))  # This is your Project Root
IMG_DIR = Path("../pictures/test/")  # relative path from ROOT_DIR
FILE_EXT = ".tiff"
EXT_LENGTH = 5


def calculate_ratios(file_name_1, file_name_2):

    file_1 = generate_file_path(file_name_1)
    file_2 = generate_file_path(file_name_2)

    img_arr1 = plt.imread(file_1)
    img_arr2 = plt.imread(file_2)

    save_file = generate_save_name(file_name_1, file_name_2)

    ndvi_calculation(img_arr1, img_arr2, save_file)


def generate_file_path(file):
    """ Returns the path to the given file """

    path = ROOT_DIR / IMG_DIR / (file + ".tiff")
    return path


def generate_save_name(file1, file2):
    """ Returns a name for the save file of the calculation results """

    save_file = file1 + '_' + file2
    return save_file


def ndvi_calculation(arr1, arr2, save_file):
    """ 
        Calculates the R/G ratios using the NDVI formula:
        NDVI = (Band 1 - Band 5) / (Band 1 + Band 5)
    """

    sub_arr = np.subtract(arr1, arr2)
    add_arr = np.add(arr1, arr2)
    div_arr = np.divide(sub_arr, add_arr)

    np.save(save_file, div_arr)
    #load_print_file("img1-img2")


def evi_calculation(band1, band3, band5, band6):
    """ 
        Does ratio calculation using the EVI formula
        EVI = 2.5 * (Band1-Band5) / (Band1 + (6 * Band5) - (7.5 * Band3) + 1)
    """

    # create arrays of same shape to do the operations with
    a1 = np.full((2400, 2400, 4), 1)
    a2 = np.full((2400, 2400, 4), 2.5)
    a6 = np.full((2400, 2400, 4), 6)
    a7 = np.full((2400, 2400, 4), 7.5)

    # caclulating: (band1 - band5)
    num = np.subtract(band1, band5)

    # caclulating: (band1 + (6 * band5)) - ((7.5 * band3) + 1)
    a6_band5 = np.multiply(a6, band5)
    a7_band3 = np.multiply(a7, band3)
    band1_b5 = np.add(band1, a6_band5)
    a7_band3_a1 = np.add(a7_band3, a1)
    denum = np.subtract(band1_b5, a7_band3_a1)

    quotient = np.divide(num, denum)

    evi = np.multiply(a2, quotient)

    # can save and then call load_print_file("arvi") to see result
    # np.save("evi.npy", evi)
    return evi


def arvi_calculation(band1, band3, band5):
    """ 
        Does ratio calculation using the ARVI formula
        ARVI = (Band1 - 2 * Band5 + Band3) / (Band1 + 2 * Band5 - Band3)
    """
    # calculating: (Band1 - (2 * Band5) + Band3)
    a2 = np.full((2400, 2400, 4), 2)
    a2_b5 = np.multiply(a2, band5)
    bs1_a2_b5 = np.subtract(band1, a2_b5)
    num = np.add(bs1_a2_b5, band3)

    # Calculating: (Band1 + (2 * Band5) - Band3)
    ba1_a2_b5 = np.add(band1, a2_b5)
    denum = np.subtract(ba1_a2_b5, band3)

    arvi = np.divide(num, denum)

    # can save and then call load_print_file("arvi") to see result
    # np.save("arvi.npy", arvi)
    return arvi


def load_print_file(file):
    """ 
        loads and prints a given .npy file 
        (do not add an extension to file name) 
    """

    infile = np.load(file + ".npy")
    print(file + ' ')
    print(infile)


### Function call ###
# calculate_ratios("img1", "img2")
"""
# setup for example method calls
"""
""" <-- uncomment this
i1 = generate_file_path("img1")
i2 = generate_file_path("img2")
i3 = generate_file_path("img3")

# generate arrays from images
a1 = plt.imread(i1)
a2 = plt.imread(i2)
a3 = plt.imread(i3)
 uncomment this --> """
"""<-- uncomment this for EVI
#This is an example of how to use the evi_calculation method
evi_calculation(a1, a2, a3, a1)
load_print_file("evi")
 uncomment this for EVI --> """
"""<-- uncomment this for ARVI
# This is an example of how to use the arvi_calculation method
arvi_calculation(a1, a2, a3)
load_print_file("arvi")
 uncomment this for ARVI --> """