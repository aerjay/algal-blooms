import os
import tempfile
import numpy as np
import shutil
import urllib
import matplotlib.pyplot as plt
import rasterio
import cv2
from sklearn.cluster import KMeans



class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def dominantColors(self):
        # read image
        img = cv2.imread(self.IMAGE)

        # convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))

        # save image after operations
        self.IMAGE = img

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)

        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_

        # save labels
        self.LABELS = kmeans.labels_

        # returning after converting to integer from float
        return self.COLORS.astype(int)

colors = "Figure_1.png"
clusters = 5
dc = DominantColors(colors, clusters)
colors = dc.dominantColors()
print(colors)
print(dc.LABELS.shape)

# for i in range(100):
#     print(dc.LABELS[i])

rows,cols = dc.IMAGE.shape

for i in range(rows):
    for j in range(cols):
        if dc.LABELS[i+j] == 0:
            dc.IMAGE[i, j, :] = [255, 0, 0]
        if dc.LABELS[i+j] == 1:
            dc.IMAGE[i, j, :] = [255, 255, 255]
        if dc.LABELS[i + j] == 2:
            dc.IMAGE[i, j, :] = [0, 0, 0]
        if dc.LABELS[i + j] == 3:
            dc.IMAGE[i, j, :] = [0, 255, 0]
        if dc.LABELS[i + j] == 4:
            dc.IMAGE[i, j, :] = [0, 0, 255]

plt.imshow(dc.IMAGE)
plt.show()