from operator import itemgetter
import numpy as np

DEFAULT_COLOR_VALUES = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [0, 0, 255]]

def create_legend_using_ndvi(cluster, ndvi_index=3, polarized_color_values=DEFAULT_COLOR_VALUES):
    """
    @param : cluster - the cluster values from classifier
    @param : ndvi_index - position for ndvi data
    @param : polarized_color_values - color template for polarization targeted
            to dvi arranged from lowest dvi to highest
    @return : output - legend with polarized values
    """
    # return if cluster is not the same length as amount of polarized colors
    if not len(cluster) == len(polarized_color_values):
        return []

    # Position of index reference in indexed_cluster data
    reference_index = len(cluster[0])

    # Array that is a copy of clusters but with index appended for referece
    indexed_cluster = create_indexed_array(cluster)

    #Create an array that is sorted by lowest ndvi value to highest, with reference to its original position
    ndvi_sorted_input = sorted(indexed_cluster, key=itemgetter(ndvi_index))

    #Initialize empty 2D output array
    output = np.zeros((len(cluster), 3))

    # Create a legend by using ndvi sorted array and mapping it back to its
    # original index using the template polarized_color_values
    for i in range(len(cluster)):
        original_index = int(ndvi_sorted_input[i][reference_index])
        output[original_index] = polarized_color_values[i]

    return output

# Create array with its index attached to end of each
# Expects 2D array
def create_indexed_array(arr):
    indexed_arr = np.zeros((len(arr), len(arr[0]) + 1))
    index = 0
    for i in range(len(arr)):
        indexed_arr[i] = np.append(arr[i], index)
        index += 1

    return indexed_arr
