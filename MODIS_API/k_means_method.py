from sklearn.cluster import KMeans

def create_labels_colors(input_image, clusters=5):
    """
    Receive a image and groups the colours in the image into n = 5 (default) buckets using K-Means
    @param: input_image - Receives a 2D array representation of an image in the form of (layers, x,y)
    @param: clusters - Defines amount of clusters desired for kmeans classification
    @return: colors_array, length 'clusters' array of (1,layers) vectors representing the classifications OR empty array on failure
    @return: labels_array, (1,x,y) image assigning each pixel to a colour classification OR empty array on failure
    """
    reshaped_img = input_image.reshape((input_image.shape[0], input_image.shape[1] * input_image.shape[2]))

    kmeans = KMeans(clusters, precompute_distances=True).fit(reshaped_image)

    colors_array = kmeans.cluster_centers_.astype(int)

    labels_array = kmeans.labels_
    labels_array = labels_array.reshape(((input_image.shape[0], input_image.shape[1], input_image.shape[2])))

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
