"""LEAVE ME ALONE PYLINTER"""
from sklearn.cluster import KMeans

def create_labels_colors(input_image, clusters=5):
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

    kmeans = KMeans(clusters)
    kmeans.fit(input_image)

    colors_array = kmeans.cluster_centers_.astype(int)

    labels_array = kmeans.labels_

    return (colors_array, labels_array)
    
# Use Example
# TEST_IMAGE = [
#     [3, 4, 2, 2], [3, 2, 44, 0.5], [4, 25, 62, 0.5], [23, 54, 66, 0.3], [52, 122, 240, 0.1],
#     [3, 4, 2, 2], [3, 2, 44, 0.5], [4, 25, 62, 0.5], [23, 54, 66, 0.3], [52, 122, 240, 0.1],
#     [3, 4, 2, 2], [3, 2, 44, 0.5], [4, 25, 62, 0.5], [23, 54, 66, 0.3], [52, 122, 240, 0.1],
#     [3, 4, 2, 2], [3, 2, 44, 0.5], [4, 25, 62, 0.5], [23, 54, 66, 0.3], [52, 122, 240, 0.1],
#     [3, 4, 2, 2], [3, 2, 44, 0.5], [4, 25, 62, 0.5], [23, 54, 66, 0.3], [52, 122, 240, 0.1],
#     [3, 4, 2, 2], [3, 2, 44, 0.5], [4, 25, 62, 0.5], [23, 54, 66, 0.3], [52, 122, 240, 0.1]]
   
# COLORS, LABELS = create_labels_colors(TEST_IMAGE, 5)
# print(COLORS)
# print(LABELS)