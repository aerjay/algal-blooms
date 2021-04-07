import cv2
import numpy as np


def assign_rgb(source_arr, target_rgb, output_arr, output_exempt_indices):
    """
    Matches a closest RGB value from a source and maps it onto an output array and records its index
    @Param: source_arr - data source from classifier, expects a 2d array of dimensions [5][3]
    @Param: target_rgb - 1D array representing [R, G, B] values
    @Param: output_arr - persistent output of new color classifications, [5][3]
    @Param: output_exempt_indices - records indexes that have been chosen already
    @Return: output_arr
    @Return: output_exempt_indices
    """
    index = -1
    score = 999
    for i in range(5):
        if i in output_exempt_indices:
            continue
        c_score = abs(target_rgb[0] - source_arr[i][0]) + \
                  abs(target_rgb[1] - source_arr[i][1]) + abs(target_rgb[2] - source_arr[i][2])
        if c_score < score:
            score = c_score
            index = i

    output_arr[index] = target_rgb
    output_exempt_indices.append(index)

    return output_arr, output_exempt_indices


# @Param: class_colors - Classifier output, must be 2D array with [5][3] dimensions [[R, G, B],...]
# @Return:  - Array of length 5 which will contain values of color classification
def create_rgbwb_class_colors(class_colors):
    """
    @Param: class_colors - Classifier output, must be 2D array with
    [5][3] dimensions [[R, G, B],...]
    @Return:  - Array of length 5 which will contain values of color classification"""

    print("Classifying values into distinct RGB groups")

    # Initialize arrays
    output_colors_arr = np.zeros((5, 3))
    exempt_indices = []

    # Look for closest black score
    output_colors_arr, exempt_indices = assign_rgb(class_colors, [0, 0, 0], output_colors_arr, exempt_indices)

    # Look for closest white score
    output_colors_arr, exempt_indices = assign_rgb(class_colors, [255, 255, 255], output_colors_arr, exempt_indices)

    # Look for closest red score
    output_colors_arr, exempt_indices = assign_rgb(class_colors, [0, 0, 255], output_colors_arr, exempt_indices)

    # Look for closest green score
    output_colors_arr, exempt_indices = assign_rgb(class_colors, [0, 255, 0], output_colors_arr, exempt_indices)

    # Look for closest blue score
    output_colors_arr, exempt_indices = assign_rgb(class_colors, [255, 0, 0], output_colors_arr, exempt_indices)

    # kmeans outputs random groups, use this function to assign consistent  false colours corresponding to each
    # between runs
    return output_colors_arr


def paint_by_colours(labels, clusters):
    print("Swapping classified labels in image with distinct colours ")
    w, h = 2400, 2400

    image = np.zeros((w, h, 3))
    rgb_cluster = np.zeros((5, 3), dtype=float)
    label_idx = 0

    for i in range(4):
        rgb_cluster[i][0] = clusters[i][0]
        rgb_cluster[i][1] = clusters[i][1]
        rgb_cluster[i][2] = clusters[i][2]

    for i in range(w):
        for j in range(h):
            image[i][j] = rgb_cluster[labels[label_idx]]
            label_idx += 1

    # blur to get rid of salt + pepper noise
    # image = image.astype(np.uint8)
    image = np.array(image, dtype=np.uint8)
    medianBlur = cv2.medianBlur(image, 5)

    return medianBlur

# Use Example
# TEST_ARRAY = [[255,255,255, 2],[25,255,25, 0],[1,1,1, 0],[255,25,25, 0],[25,25,255, 0]]
# print(create_rgbwb_class_colors(TEST_ARRAY))
