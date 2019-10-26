#assuming the water class is index 3 and the ARVI layer is the 5th layer

#This code will receive the 5-layer-image (from Chi) and its 1-d classification array (from Ben)
#and output the average ARVI of pixels classified as water.
#In main.py, call this function n times, where n is the number of images and populate
#the array with the output data. That array may then be exported as a csv for the front end
import numpy as np

def graphData(img, labels, water_label):
    #receive the image containing (IR, red, green) and NDVI data in the shape 4 x 2400 x 2400
    #as well as the KMeans labels (as 1D array) and an indicator for which label is for water
    
    NDVI_layer = np.zeros((2400,2400), dtype = float)
    red_layer = np.zeros((2400,2400), dtype = float)
    
    #Make all the labels 1 if water, else 0. Then reshape it to the 2400x2400 image
    for i, label in enumerate(labels):
        labels[i] = (label == water_label)
        
    labels = labels.reshape(2400,2400)
    
    #separate out the NDVI and red bands of interest from the original image, omitting non-water pixels
    NDVI_layer = np.multiply(img[3,:,:], labels)
    red_layer = np.multiply(img[1,:,:], labels)
    
    #calculate the mean, 90th percentile, and 10th percentile of NDVI and chlorophyll
    NDVI_avg = np.mean(NDVI_layer)
    Chl_avg = np.mean(red_layer)
    
    NDVI_lower, NDVI_upper = np.percentile(NDVI_layer, [10,90])
    Chl_lower, Chl_upper = np.percentile(red_layer, [10,90])
    
    graph_data = [NDVI_avg, NDVI_upper, NDVI_lower, Chl_avg, Chl_upper, Chl_lower]
    
    return graph_data



#to be included in main:
    #file name will include lat, long, and end date of the images
graphCSV = np.zeros(6, dtype = float)

#integrate this with whatever loop generates each of the 6 images
for j in range(6):
    #... Chi & Ben's code before
    graphCSV[j] = graphData(rgb, labels, water)

np.savetxt(lat+"-"+long+"-"+date+".csv", graphCSV, delimiter = ",")