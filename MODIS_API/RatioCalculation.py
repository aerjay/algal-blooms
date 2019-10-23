import os
import numpy
from pathlib import Path
import matplotlib.pyplot as plt

project_folder = os.path.dirname(os.path.abspath(__file__))
img_folder = Path("../pictures/test/")
file_name1 = project_folder / img_folder / "img1.tiff"
file_name2 = project_folder / img_folder / "img2.tiff"

img_arr1 = plt.imread(file_name1)
img_arr2 = plt.imread(file_name2)
#plt.imshow(img_arr)
#plt.show()


def calculate_ratio(arr1, arr2):
    # create an int array of size 2400 x 4 filled with 0's
    ratio_arr = numpy.zeros((2400, 4))

    # loop through the 3D arrays and calculate the ratios then store the result
    i = 0
    for outer_arr in arr1:
        j = 0
        for inner_arr in arr1[i]:
            k = 0
            for value in arr1[i][j]:
                ratio = arr1[i][j][k] / arr2[i][j][k]
                print('i = ', i, 'j = ', j, 'k = ', k, 'ratio = ', ratio)
                k += 1
            j += 1
        i += 1


calculate_ratio(img_arr1, img_arr2)
