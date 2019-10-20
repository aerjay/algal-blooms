#This algorithm imports a 2400 x 2400 x 3 image to be classified alongside two 1x3 arrays of reference classes (should be extended to any number of classes)
#For each pixel in the test image, calculate an "alpha" value with respect to each of the references
#Search the alpha values for the smallest value and get the index of that value
#The pixel is classified as that index value

#Next: take this output image and false colour the different classes

import math
import numpy as np


testImg = #load in test image
r1 = #reference spectrum 1
r2 = #reference spectrum 2

n = 3 #number of spectral bands in image
alpha = np.empty(2, dtype = float)

output = np.empty([2400,2400], dtype = float)

SumTR1 = 0
SumTR2 = 0
SumT2 = 0
SumR21 = 0
SumR22 = 0

for j in range(2400):
    for k in range(2400):
        t = testImg[j,k,:]

        for i in range(n):
            SumTR1 = SumTR1 + t(i)*r1(i)
            SumTR2 = SumTR2 + t(i)*r2(i)
            
            SumT2 = SumT2 + t(i)**2
            
            SumR21 = SumR21 + r1(i)**2
            SumR22 = SumR22 + r2(i)**2

        alpha[0] = math.acos(SumTR1/(math.sqrt(SumT2)*math.sqrt(SumR21))) #spectral angle for R1
        alpha[1] = math.acos(SumTR2/(math.sqrt(SumT2)*math.sqrt(SumR22)))
        
        if alpha[0] < alpha[1]:
            output[j,k] = alpha[0]
        else:
            output[j,k] = alpha[1]