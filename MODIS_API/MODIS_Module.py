import os
import tempfile
import numpy as np
import shutil
import urllib
import matplotlib.pyplot as plt
import rasterio
import cv2
from sklearn.cluster import KMeans
import scipy.misc
from azure.storage.blob import BlockBlobService

# Storage locations are documented at http://aka.ms/ai4edata-modis
modis_blob_root = 'http://modissa.blob.core.windows.net/modis'
modis_container_name = 'modis'
modis_account_name = 'modissa'

modis_temp_path = os.path.join(tempfile.gettempdir(), 'modis')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
modis_temp_path = os.path.join(ROOT_DIR, 'MODIS_Images')
os.makedirs(modis_temp_path, exist_ok=True)

# This file is provided by NASA; it indicates the lat/lon extents of each
# MODIS tile.
#
# The file originally comes from:
#
# https://modis-land.gsfc.nasa.gov/pdf/sn_bound_10deg.txt
modis_tile_extents_url = modis_blob_root + '/sn_bound_10deg.txt'

# Read-only shared access signature (SAS) URL for the MODIS container
modis_sas_url = 'st=2019-07-26T17%3A21%3A46Z&se=2029-07-27T17%3A21%3A00Z&sp=rl&sv=2018-03-28&sr=c&sig=1NpBV6P8SIibRcelWZyLCpIh4KFiqEzOipjKU5ZIRrQ%3D'

# Load this file into a table, where each row is (v,h,lonmin,lonmax,latmin,latmax)
modis_tile_extents = np.genfromtxt(modis_tile_extents_url,
                                   skip_header=7,
                                   skip_footer=3)

modis_blob_service = BlockBlobService(account_name=modis_account_name,
                                      sas_token=modis_sas_url)


# %matplotlib inline

def lat_lon_to_modis_tiles(lat, lon):
    """
    Get the modis tile indices (h,v) for a given lat/lon

    https://www.earthdatascience.org/tutorials/convert-modis-tile-to-lat-lon/
    """

    found_matching_tile = False
    i = 0
    while not found_matching_tile:
        found_matching_tile = modis_tile_extents[i, 4] <= lat <= modis_tile_extents[i, 5] \
                              and modis_tile_extents[i, 2] <= lon <= modis_tile_extents[i, 3]
        i += 1

    v = int(modis_tile_extents[i - 1, 0])
    h = int(modis_tile_extents[i - 1, 1])

    return h, v


def list_blobs_in_folder(container_name, folder_name):
    """
    List all blobs in a virtual folder in an Azure blob container
    """

    files = []
    generator = modis_blob_service.list_blobs(modis_container_name,
                                              prefix=folder_name,
                                              delimiter="")
    for blob in generator:
        files.append(blob.name)
    return files


def list_tiff_blobs_in_folder(container_name, folder_name):
    """"
    List .tiff files in a folder
    """

    files = list_blobs_in_folder(container_name, folder_name)
    files = [fn for fn in files if fn.endswith('.tiff')]
    return files


def download_url(url, destination_filename):
    """
    Utility function for downloading a URL to a local file
    """

    print('Downloading file {}'.format(os.path.basename(url)), end='')
    urllib.request.urlretrieve(url, destination_filename)
    assert (os.path.isfile(destination_filename))
    nBytes = os.path.getsize(destination_filename)
    print('...done, {} bytes.'.format(nBytes))


def download_url_to_temp_file(url):
    fn = os.path.join(modis_temp_path, next(tempfile._get_candidate_names()))
    print("MODIS file downloaded to: " + modis_temp_path)
    download_url(url, fn)
    return fn


# Files are stored according to:
# http://modissa.blob.core.windows.net/[product]/[htile]/[vtile]/[year][day]/kifilename


def download_data_to_folder(product, lat, long, day_num, delete_on_finish):
    h, v = lat_lon_to_modis_tiles(lat, long)
    folder = product + '/' + '{:0>2d}/{:0>2d}'.format(h, v) + '/' + day_num

    # Find all .tiff files from this tile on this day, one file per channel
    files = list_tiff_blobs_in_folder(modis_container_name, folder)

    # Channel 7 in a MCD43A4 file corresponds to MODIS band 1.
    #
    # Let's map bands 5, 1, and 3 (channels 7,9,11), corresponding to infrared, red, and blue to RGB.
    channels = [11, 7, 9]
    for ifn in channels:
        remote_fn = files[ifn]
        url = modis_blob_root + '/' + remote_fn
        fn = download_url_to_temp_file(url)

    if delete_on_finish:
        shutil.rmtree(modis_temp_path)


def show_modis_image():
    image_data = get_modis_bands_array()

    rgb = np.dstack((image_data[0], image_data[1], image_data[2]))
    np.clip(rgb, 0, 1, rgb)
    plt.imshow(rgb)
    plt.show()


def get_modis_bands_array():
    norm_value = 4000
    directory = modis_temp_path
    image_data = []

    for filename in os.listdir(directory):
        file = os.path.join(directory, str(filename))
        raster = rasterio.open(file, 'r')
        band_array = raster.read(1)
        raster.close()
        band_array = band_array / norm_value
        image_data.append(band_array)

    return image_data

# Todo: remove all commented code below into their own respective classes and call them in main.py
#
# class DominantColors:
#     CLUSTERS = None
#     IMAGE = None
#     COLORS = None
#     LABELS = None
#
#     def __init__(self, image, clusters=3):
#         self.CLUSTERS = clusters
#         self.IMAGE = image
#
#     def dominantColors(self):
#         # read image
#         img = cv2.imread(self.IMAGE)
#
#         # convert to rgb from bgr
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#         # reshaping to a list of pixels
#         print("image shape:" + str(img.shape[0]) + " by " + str(img.shape[1]))
#         img = img.reshape((img.shape[0] * img.shape[1], 3))
#
#         # save image after operations
#         self.IMAGE = img
#
#         # using k-means to cluster pixels
#         kmeans = KMeans(n_clusters=self.CLUSTERS)
#         kmeans.fit(img)
#
#         # the cluster centers are our dominant colors.
#         self.COLORS = kmeans.cluster_centers_
#
#         # save labels
#         self.LABELS = kmeans.labels_
#
#         # returning after converting to integer from float
#         return self.COLORS.astype(int)
#
# colors = "Figure_1.png"
# clusters = 5
# dc = DominantColors(colors, clusters)
# colors = dc.dominantColors()
# print(colors)
# print(dc.LABELS.shape)
#
# length, colors = dc.IMAGE.shape
#
# for i in range(length):
#     if dc.LABELS[i] == 1:
#         dc.IMAGE[i] = [255, 0, 0]
#     if dc.LABELS[i] == 0:
#         dc.IMAGE[i] = [255, 255, 255]
#     if dc.LABELS[i] == 4:
#         dc.IMAGE[i] = [0, 0, 0]
#     if dc.LABELS[i] == 2:
#         dc.IMAGE[i] = [0, 255, 0]
#     if dc.LABELS[i] == 3:
#         dc.IMAGE[i] = [0, 0, 255]
#
# dc.IMAGE = dc.IMAGE.reshape((476, 640, 3))
#
# medianBlur = cv2.medianBlur(dc.IMAGE, 3)
#
# plt.imshow(medianBlur)
# plt.show()
