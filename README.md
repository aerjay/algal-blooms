### To Bloom or Not to Bloom, NASA International Space Apps 2019 Challenge
Space Apps Project Page:
https://2019.spaceappschallenge.org/challenges/living-our-world/bloom-or-not-bloom/teams/bloomer-early-warning-system/project

Link to our video:
https://www.youtube.com/watch?v=J8gF4bBGcoE

# Bloomer: Early Warning System
## Table of Contents
  1. [Meet the Team](#meet-the-team)
  2. [Vision](#Vision)
  3. [What Are Algae Blooms](#what-are-algae-blooms)
  4. [Impact of Algae Blooms](#impact-of-algae-blooms)
  5. [Technical Background](#technical-background)\
    5.1 [Cause of Algae Blooms](#cause-of-algae-blooms)\
    5.2 [Existing Models & Datasets](#existing-models-&-datasets)
  6. [Back End](#back-end)\
    6.1 [Prediction Algorithm](#prediction-algorithm)
  7. [Front End](#front-end)
  8. [Next Steps](#next-steps)\
    8.1 [Prediction Model](#prediction-model)\
    8.2 [User Segment](#user-segment)\
    8.3 [Space Segment](#space-segment)
  9. [References](#references)

## Meet the Team
<p align="center">
<img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/74575087_2493828480873329_4569868799494324224_n.jpg" width="600">
</p>
From Left to Right:  

**Chi Nguyen, B. Sc. Computer Science & B. Sc. Biological Science**  
*Chi is a junior developer with Aucerna, with experience in software development and design. This is Chi's first time participating in a hackathon and was very interested in the topic that combined both her fields of study.*  

**Aerjay Italia, B. Sc. Computer Science, Information Security**  
*Aer Jay is a junior developer with Aucerna with experience in software and computer security*  

**Benjamin Lee, B. Sc. Computer Science**  
*Ben is a junior developer working in Alberta and this is second hackathon that he has participated in.*  

**James Xie, B. ASc. Engineering Chemistry**  
*James is an operations consultant at Stroud International, with experience in project management and process design. James  has led remote sensing and astrobiology payloads as part of the University Rover Challenge and Canadian Satellite Design Challenge, and is currently the assistant project manager for the SEDS Canada CAN-SBX Challenge.*  

**Kal Radikov, B. ASc. Computer Engineering**  
*Kal is a junior developer with McDaniel & Associates Consultants Ltd. with experience in software design. Kal has worked on two hackathon projects including foldable oragami wheels to be used on Mars rovers and an online machine learning diary to analyse trends in individuals. On the side, he is an avid painter working mainly with oil paints and 3D sculpture.*

## Vision
Bloomer is a web app that provides a service for alerting the public to aquatic events such as algae blooms which may pose a health risk. Government, research, and private agencies interested in algae bloom events may also subscribe to a region to access forecasting and predictive models which receive data from satellite images (NASA MODIS) and ground-based measurements.

<p align="center">
<img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/Bloomer_logo_cropped.png" width="250">
</p>
<p align="center">
<img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/App%20High%20Level%20Segmentation.png" width="400">
</p>

## What Are Algae Blooms
Algae blooms are rapid growths of photosynthetic eukaryotic organisms which can occur in fresh or marine environments. During a bloom, the algae will consume the available nutrients in a given body of water, allowing the population to quickly grow and dominate. Their rapid growth however leads into a rapid death, allowing bacteria to grow. This results in a dead zone as the bacteria consume the available oxygen and nutrients in the water.

**Harmful algae blooms (HABs)** contain algae species which additionally release toxins which can contaminate waterways, further causing health issues through contamination of drinking water and contact with wildlife.
<p align="center">
<img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/Bloom1.jpg" width="400">
</p>

*Figure A: Example of an algae bloom. Image taken from the National Centres for Coastal Ocean Science, Phytoplankton Monitoring Network (PMN) [12]*

## Impact of Algae Blooms
Overall, algae blooms represent a billion-dollar issue worldwide annually, and affect nearly all coastal/interior bodies of water worldwide.
### 1. Agriculture & Fishing
- Losses in the US amount to nearly $35 MM annually in fishing & agriculture industries [11]
- These industries compose 10-50% of the GDP in many southeast asian countries, making algae blooms incredibly disruptive to local economies.
### 2. Medical
- Direct medical costs are incurred through treatment of people and pets exposed to contaminated water. Exposure may cause pneumonia, gastrointestinal illnesses, and respiratory illnesses [10]. In the state of Florida alone, this represents a $22 MM annual loss [10].
### 3. Tourism & Recreation
- Revenue is lost through decrease in tourism and recreation to coastal/beach locations, representing a near $7 MM annually in the US, which directly impact hotels and restaurants as well as predominantly affecting smaller communities built near these natural attractions [11]. Cleanup and mitigation efforts amount to further costs associated with blooms ($2 MM/yr in the US) [11].
### 4. Environmental
- Damage to ecosystems further cause indirect costs through decreased biodiversity, harm to endangered species, and formations of dead zones which are difficult to reverse.

## Technical Background
### Cause of Algae Blooms
Algae are not a group of related species, resulting in different responses to environmental conditions for growth [4]. A variable analysis conducted through a literature search (below) has identified multiple key variables in algae growth which can be either directly measured from remote sensing satellites (blue) or estimated from spectral image data (orange). However, some must still be measured directly (brown) and are critical for calibrating a model for a particular water body. [2-8]

![variable analysis](https://github.com/aerjay/algal-blooms/blob/master/media_photos/Variable%20analysis.png "Variable analysis of algae blooms")

### Existing Models & Datasets
Research models already exist at the regional level, however multiple measurements across a growth season are needed (environment is highly dynamic) and there have not been any successful global algal models [2,3,4,7]. Models for critical variables such as available nutrition also exist at the region level (such as VEMALA [9]) and can be integrated into regional-level algal models, however their applicability again is not universal. The level of specificity required in each region to produce a sufficiently accurate forecast model will require water-body-specific calibration [5].

Remote sensing multispectral images of the earth are readily available through NASA's Moderate-Resolution Imaging Spectroradiometer (MODIS) which provides image bands in the VIS-NIR (459 - 2155 nm) at a spatial resolution of 250-500 m and spectral resolution of 20-50 nm. Each location is imaged once every 1-2 days. [13] MODIS has been successfully applied in monitoring blooms [1], however the spatial/temporal resolution is insufficient for prediction alone and must be augmented with additional imaging capability and ground-based measurements [7]:

![map of ground data](https://github.com/aerjay/algal-blooms/blob/master/media_photos/Ground%20Measurement%20Datasets.png "Global map of ground measurements")

## Back End
The proof-of-concept model only had access to the MODIS-Terra database and will classify regions in the image based on their NDVI characteristics.

The normalized difference vegetation index (NDVI) and MODIS Band 1 (620–670 nm, the closest match to the desired 683 nm chlorophyll fluorescence band [17]) in water-classified pixels is averaged for that region and shown over time alongside 10th and 90th percentile error bars as an example of time-series outputs available. In future implementations if multiple water bodies are present in an image, each can be segmented and output separately.

<p align="center">
  <img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/2011278%20Lake%20Erie2.png" width="280" />
  <img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/2011278%20NDVI.png" width="280" /> 
  <img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/2011278_false.png" width="280" />
</p>

*Figure B: MODIS image of Lake Erie, Oct. 5, 2011. Left: True colour image, Center: NDVI heatmap, Right: KMeans clustered false-colour*

K-Means classification of NDVI regions is non-optimal as it is an unsupervised method and cannot handle non-spherical groups. It has been shown that supervised methods such as support-vector machine (SVM) or spectral-angle mapping classifiers which are both supervised can provide more consistent and accurate classifications of land-cover information [16], however the team did not have sufficient resources to train a supervised model in the available time.

### Forecasting Algorithm
The proposed forecasting algorithm at full implementation would receive data from multiple sources to estimate variables of interest:
- Satellite spectral data on different surfaces (e.g. land vs. water) will be used to estimate different parameters
  - A SVM classifier rather than KMeans using key vegetation indices (NDVI and EVI) is used to cluster regions of similar surfaces
    - pixels identified as water will be considered in subsequent analysis and variable estimation to reduce the data load
- Ground-based measurements are combined with spectral estimates using linear interpolation to populate gaps in spatial data and Savitzky–Golay (S-G) filtering to smooth the time series due to its robustness towards varying time intervals of a measurement [16].
- A boosted regression tree will be used to forecast the algae population from the time series data.
   - An ensemble approach will be applied to the forecast by applying perturbations to model inputs and model parameters to handle the inherent uncertainty in model inputs and the model uncertainty due to the data resolution.
   - The resultant Monte Carlo output may then be used as a probabilistic forecast.

![system level diagram](https://github.com/aerjay/algal-blooms/blob/master/media_photos/System%20Level%20Diagram%20v2.png "system level diagram")

## Front End
A web app was developed using HTML, CSS, and JavaScript, and may be found https://github.com/aerjay/algal-blooms/tree/master/www. 

Users are able to search for locations and see satellite images of that area at any point in time. Users are then able to subscribe to alerts for that area including health warnings and forecast warnings. Users interested in forecasting and mitigation tools may also subscribe to locations as well as access the raw vegetation-indexed and spectrally clustered images and time-series data built with Chart.js. At full implementation, the ensemble forecast will be viewable similar to a weather report, listing key variables such as nutrition and water surface temperature.

The Google Maps API was integrated into the latitude/longitude search field to help users navigate and find their desired location. At full implementation, an alternate search method using the name or address of the desired location or the user's current location would increase user accessibility to data.

<p align="center">
<img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/Web%20App%20page%201.png" width="400">
<img src="https://github.com/aerjay/algal-blooms/blob/master/media_photos/Web%20App%20page%202.png" width="400">
</p>

## Next Steps
### Prediction Model
- [ ] Access to the MODIS-Aqua product to use spectral images of water bodies in the prediction model
  - the Bloomer team currently only has access to the MODIS-Terra database which does not include large bodies of water and the spectral data has been normalized for land-based uses, resulting in limited image quality over water bodies of interest
  - For inland water bodies, higher resolution databases such as MASTER, HICO, or AVIRIS would be more effective on the smaller spatial sized regions.
- [ ] Training a boosted regression tree (BRT) model for correlating hyperspectral images to key growth variables [6]
  - MacDougall et al. (2018) has shown that LAI, EVI, GEMI, and GVI indices may be correlated to nitrogen content with R<sup>2</sup> = 0.7
- [ ] Training an SVM for water-based vegetation identification [16]
- [ ] Leveraging spectral analysis of the 680 - 900 nm band to identify algal species to provide more specific models [17]
  - This would require both sufficient spatial resolution to omit non-water pixels and spectral resolution to distinguish reflectance peaks within the desired band [17]

### User Segment
- [ ] Allow users to subscribe to certain locations and receive email alerts
- [ ] Build two user groups, Public and Research, to provide tailored tools for each user segment
- [ ] Pull local water quality news for public users seeking awareness of health risks in their area

### Space Segment
- [ ] Increase spatial and temporal resolution of remote sensing data.
  - Frequent (2-3/day) imaging of equatorial regions (e.g. Southeast Asia) is difficult without either a constellation of sun-synchronous or near-equatorial orbiting satellites. To lower the cost, many researchers are now proposing SmallSat/CubeSat missions to fill this gap. Bloomer would seek to raise awareness and support for these initiatives to further improve its services

## References
I apologize ahead of time that this list of references is not in the order of appearance.

- [1] Mati Kahru and B. Greg Mitchell. MODIS Detects a Devastating Algal Bloom in Paracas Bay, Peru. Eos, Vol. 85, No. 45, 9 November 2004
- [2] Marieke Beaulieu, Frances Pick, Michelle Palmer, Sue Watson, Jenny Winter, Ron Zurawell, and Irene Gregory-Eaves. Comparing predictive cyanobacterial models from temperate regions. Can. J. Fish. Aquat. Sci. 71: 1830–1839 (2014)
- [3] Marieke Beaulieu, Frances Pick, and Irene Gregory-Eaves. Nutrients and water temperature are significant predictors of cyanobacterial biomass in a 1147 lakes data set. Limnol. Oceanogr., 58(5), 2013, 1736–1746
- [4] Dolman AM, Rucker J, Pick FR, Fastner J, Rohrlack T, et al. (2012) Cyanobacteria and Cyanotoxins: The Influence of Nitrogen versus Phosphorus. PLoS ONE 7(6): e38757.
- [5] Anurani D. Persaud, Andrew M. Paterson, Peter J. Dillon, Jennifer G. Winter, Michelle Palmer, Keith M. Somers. Forecasting cyanobacteria dominance in Canadian temperate lakes. Journal of Environmental Management 151 (2015) 343e352
- [6] J.-P. Descy, F. Leprieur, S. Pirlot, B. Leporcq, J. Van Wichelen, A. Peretyatko, S. Teissier, G.A. Codd, L. Triest, W. Vyverman, A. Wilmotte. Identifying the factors determining blooms of cyanobacteria in a set of shallow lakes. Ecological Informatics 34 (2016) 129–138
- [7] Annette BG Janssen, Jan H Janse, Arthur HW Beusen, Manqi Chang, John A Harrison, Inese Huttunen, Xiangzhen Kong, Jasmijn Rost, Sven Teurlincx, Tineke A Troost, Dianneke van Wijk, and Wolf M Mooij. How to model algal blooms in any lake on earth. Current Opinion in Environmental Sustainability 2019, 36:1–10
- [8] GERALD K. MOORE (1980) Satellite remote sensing of water turbidity / Sonde de télémesure par satellite de la turbidité de l'eau, Hydrological Sciences Bulletin, 25:4, 407-421, DOI: 10.1080/02626668009491950
- [9] Huttunen, I., Huttunen, M., Piirainen, V. et al. Environ Model Assess (2016) 21: 83. https://doi.org/10.1007/s10666-015-9470-6
- [10] Florida Department of Health. Harmful Algal Blooms – Economic Impacts. pdf. 2008.
- [11] Anderson DM, Hoagland P, Kaoru Y, White AW. Estimated annual economic impacts from harmful algal blooms (HABs) in the United States. 2000;WHOI-2000-11.
- [12] National Centre for Coastal Ocean Science. Phytoplankton Monitoring Network (PMN). Online. 2019. https://coastalscience.noaa.gov/research/stressor-impacts-mitigation/pmn/image-gallery/bloom-mortality-events/
- [13] MODIS Database. Microsoft Azure Open Datasets. 2019. https://azure.microsoft.com/en-ca/services/open-datasets/catalog/modis/
- [14] Palmer, S.C.J., Kutser, T. & Hunter, P.D. (2015) Remote sensing of inland waters: Challenges, progress and future directions. Remote Sensing of Environment. [Online] 157, 1–8. Available from: doi:10.1016/j.rse.2014.09.021.
- [15] Rashmi S, Swapna Addamani, Venkat, and Ravikiran S. Spectral Angle Mapper Algorithm for Remote Sensing Image Classification. IJISET - International Journal of Innovative Science, Engineering & Technology, Vol. 1 Issue 4, June 2014.
- [16] Long Zhao, Pan Zhang, Xiaoyi Ma, and Zhuokun Pan, “Land Cover Information Extraction Based on Daily NDVI Time Series and Multiclassifier Combination,” Mathematical Problems in Engineering, vol. 2017, Article ID 6824051, 13 pages, 2017. https://doi.org/10.1155/2017/6824051.
- [17] Shen, L.; Xu, H.; Guo, X. Satellite Remote Sensing of Harmful Algal Blooms (HABs) and a Potential Synthesized Framework. Sensors 2012, 12, 7778-7803.
