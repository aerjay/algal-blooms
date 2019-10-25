#assuming the water class is index 3 and the ARVI layer is the 5th layer

#This code will receive the 5-layer-image (from Chi) and its 1-d classification array (from Ben)
#and output the average ARVI of pixels classified as water.
#In main.py, call this function n times, where n is the number of images and populate
#the array with the output data. That array may then be exported as a csv for the front end
import numpy as np

def graphData(img, classifications):
    ARVI = 0
    n = 0
    
    #take the 5th layer of the image and make it a 1x(2400*2400) linear array
    imgData = img[:,:,4].reshape(1,-1)

    for i in range(imgData.shape[1]):
        #for each pixel that was classified as 'Water', sum its NDVI, then average
        if classifications[i] == 3:
            ARVI += imgData[0,i]
            n += 1
    
    ARVI = ARVI/n
    
    return ARVI



#to be included in main:
    #file name will include lat, long, and end date of the images
graphCSV = np.zeros(6, dtype = float)

#integrate this with whatever loop generates each of the 6 images
for j in range(6):
    #... Chi & Ben's code before
    graphCSV[j] = graphData(recent_img, classification_array)

np.savetxt(lat+"-"+long+"-"+date+".csv", graphCSV, delimiter = ",")