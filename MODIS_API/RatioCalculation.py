import numpy as np

def ndvi_calculation(arr1, arr2):
    """
        Calculates the R/G ratios using the NDVI formula:
        NDVI = (Band 1 - Band 5) / (Band 1 + Band 5)
    """

    sub_arr = np.subtract(arr1, arr2)
    add_arr = np.add(arr1, arr2)
    div_arr = np.divide(sub_arr, add_arr)

    return div_arr


def evi_calculation(blue, red, infrared):
    """
        Calculates the Enhanced Vegetation Index:
        EVI = 2.5*(Red - IR)/(Red + 6*IR - 7.5*Blue + 1)
    """
    num_arr = np.subtract(red, infrared)

    d1_arr = np.add(red, 6 * infrared)
    d2_arr = np.add(-7.5 * blue, np.ones(blue.shape, dtype=float))
    denom_arr = np.add(d1_arr, d2_arr)

    EVI_arr = 2.5 * np.divide(num_arr, denom_arr)

    return EVI_arr


def add_ratio_bands(rgb):
    ndvi_band = ndvi_calculation(rgb[1], rgb[0])  # pass in red, IR
    #evi_band = evi_calculation(rgb[2], rgb[1], rgb[0])  # pass in blue, red, IR
    rgb.append(ndvi_band)
    #rgb.append(evi_band)

    # return a numpy array instead of a list
    numpy_arr = np.array(rgb)

    # get rid of -inf and inf
    # numpy_arr[4][numpy_arr[4] == inf] = 1
    # numpy_arr[4][numpy_arr[4] == -inf] = -1

    return numpy_arr


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
import os
from numpy import inf
from pathlib import Path
import matplotlib.pyplot as plt

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__))  # This is your Project Root
IMG_DIR = Path("../pictures/test/")  # relative path from ROOT_DIR
FILE_EXT = ".tiff"
EXT_LENGTH = 5


def show_image(img):
    plt.imshow(img)
    plt.show()

def calculate_ratios(file_name_1, file_name_2):
    file_1 = generate_file_path(file_name_1)
    file_2 = generate_file_path(file_name_2)

    img_arr1 = plt.imread(file_1)
    img_arr2 = plt.imread(file_2)

    save_file = generate_save_name(file_name_1, file_name_2)

    ndvi_calculation(img_arr1, img_arr2, save_file)


def generate_file_path(file):
    #Returns the path to the given file
    path = ROOT_DIR / IMG_DIR / (file + ".tiff")
    return path


def generate_save_name(file1, file2):
    #Returns a name for the save file of the calculation results
    save_file = file1 + '_' + file2
    return save_file

def ndvi_calculation(arr1, arr2, save_file):
    
        #Calculates the R/G ratios using the NDVI formula:
        #NDVI = (Band 1 - Band 5) / (Band 1 + Band 5)

    sub_arr = np.subtract(arr1, arr2)
    add_arr = np.add(arr1, arr2)
    div_arr = np.divide(sub_arr, add_arr)

    np.save(save_file, div_arr)
    # load_print_file("img1-img2")
"""