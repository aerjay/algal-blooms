from sklearn.cluster import KMeans

def create_labels_colors(input_image, clusters=5):
    """
    Receive a image and groups the colours in the image into n = 5 (default) buckets using K-Means
    @param: input_image - Receives a 2D array representation of an image in the form of (layers, x,y)
    @param: clusters - Defines amount of clusters desired for kmeans classification
    @return: colors_array, length 'clusters' array of (1,layers) vectors representing the classifications OR empty array on failure
    @return: labels_array, (1,x,y) image assigning each pixel to a colour classification OR empty array on failure
    """
    
    #Convert a 5 x 2400 x 2400 image into a (2400*2400) x 5 image
    reshaped_img = np.zeros((input_image.shape[1], input_image.shape[2], input_image.shape[0]), dtype = float)
    for i in range(input_image.shape[0]):
        reshaped_img[:,:,i] = input_image[i,:,:]
 
    reshaped_img = reshaped_img.reshape((input_image.shape[1] * input_image.shape[2], input_image.shape[0]))

    labels_array = KMeans(clusters, precompute_distances=True).fit_predict(reshaped_image)
    labels_array = labels_array.reshape(((1, input_image.shape[1], input_image.shape[2])))

    colors_array = kmeans.cluster_centers_.astype(int)

    
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
