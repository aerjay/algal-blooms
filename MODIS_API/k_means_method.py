"""LEAVE ME ALONE PYLINTER"""
from sklearn.cluster import KMeans

def create_labels_colors(input_image, clusters=5, ratio_array1=None, ratio_array2=None):
    """
    Create labels and colors array from k-means classifier
    @param: input_image - Receives a 2D array representation of an image in the form of 
    [x*y][R,G,B,G/R]
    @param: clusters - Defines amount of clusters desired for kmeans classification
    @return: colors_array, classification array of length clusters OR empty array on failure
    @return: labels_array, array of category of input array OR empty array on failure
    """
    
    if (not isinstance(clusters, int) or not isinstance(input_image, list)):
        return ([], [])

    reshaped_image = reshape_data(input_image, ratio_array1, ratio_array2)
    

    kmeans = KMeans(clusters)
    kmeans.fit(reshaped_image)

    colors_array = kmeans.cluster_centers_.astype(int)

    labels_array = kmeans.labels_

    return (reshaped_image, colors_array, labels_array)


# Assuming the (0, 0) and row major.
def reshape_data(input_data, ratio_array1=None, ratio_array2=None):
    reshaped_image = []
    x_length = len(input_data[0][0])
    y_length = len(input_data[0])


    for row in range(y_length):
        for col in range(x_length):
            rgb_and_ratios = [input_data[0][row][col], input_data[1][row][col], input_data[2][row][col]]
            if ratio_array1 is None:
                rgb_and_ratios.append(ratio_array1[row][col])

            if ratio_array2 is None:
                rgb_and_ratios.append(ratio_array2[row][col])

            reshaped_image.append(rgb_and_ratios)
    
    return reshaped_image
