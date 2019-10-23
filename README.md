## To Bloom or Not to Bloom, a NASA International Space App Challenge
Space Apps Project Page:
https://2019.spaceappschallenge.org/challenges/living-our-world/bloom-or-not-bloom/teams/bloomer-early-warning-system/project

# Bloomer: Early Warning System
  1. [Meet the Team](#meet-the-team)
  2. [What Are Algae Blooms](#what-are-algae-blooms)
  3. [Impact of Algae Blooms](#impact-of-algae-blooms)
  4. [Technical Background](#technical-background)\
    4.1 [Cause of Algae Blooms](#cause-of-algae-blooms)\
    4.2 [Existing Models](#existing-models)\
    4.3 [Existing Datasets](#existing-datasets)
  5. [Vision](#Vision)
  6. [Back End](#back-end)\
    6.1 [Database](#database)\
    6.2 [Classification](#classification)
  7. [Front End](#front-end)
  8. [Next Steps](#next-steps)\
    8.1 [Prediction Model](#prediction-model)\
    8.2 [User Segment](#user-segment)\
    8.3 [Space Segment](#space-segment)
  9. [References](#references)

## Meet the Team
![photo of Bloomer team](https://github.com/aerjay/algal-blooms/blob/master/media_photos/74575087_2493828480873329_4569868799494324224_n.jpg "Team Photo")
From Left to Right:
#### Chi Nguyen, B.
>Chi is a junior developer with Aucerna
#### Aer Jay, B.
> RJ is a junior developer with Aucerna
#### Benjamin Lee, B.
> Ben is a junior developer with Aucerna
#### James Xie, B. ASc. Engineering Chemistry
    James is an operations consultant at Stroud International, with experience in project management and process engineering design. James has designed remote sensing and astrobiology payloads as part of the University Rover Challenge and Canadian Satellite Design Challenge, and is currently the assistant project manager for the 2019-2020 SEDS Canada CAN-SBX Challenge.
#### Kal Radikov, B. ASc. Computer Engineering
> Kal is a senior developer with 

## What Are Algae Blooms
Algae blooms

**Harmful algae blooms (HABs)** contain algae species which additionally release toxins which can contaminate waterways, further causing 

## Impact of Algae Blooms
Overall, algae blooms represent a multi-billion dollar issue worldwide annually, and affect nearly all coastal/interior bodies of water worldwide.

**1. Agriculture & Fishing**

**2. Medical**
Direct medical costs are incurred through treatment of 

**3. Tourism & Recreation**

**4. Environmental**

## Technical Background
#### Cause of Algae Blooms
![variable analysis]("Variable analysis of algae blooms")
[2-8]

Many key variables in algae growth can be either directly measured from remote sensing satellites (blue) or estimated from spectral image data (orange). However, some must still be measured directly (brown) and are critical for calibrating a model for a particular water body.

#### Existing Models
Many models exist which predict the size of algae populations given a set of parameters, however they do not predict when the explosive growth of an algal bloom will occur in a water body. additionally, most studies are concentrated in a particular region and while some models can be extended to multiple regions with similar environments, there is no globally applicable model yet.

[3] Beaulieu et al. (2013) has shown that broad models across multiple water bodies are unable to explain much of the variation in cyanobacteria biomass, and multiple measurements throughout a growth season are needed to form adequate models within a region. As such, algal bloom prediction will likely need to be on the mesoscale/regional level

[2] Linear models, nutrition (P & N), temperature, water column stability, and forms of inorganic nitrogen. North American models are suitable for estimating total cyanobacterial biomass from temperate region in Canada.

However, significantly different regions (e.g. temperate Canada vs. southeast Asia) are not comparable

[4] Different cyanobacteria additionally have different responses to each variable, further limiting the applicability of a global model
[5] forecasting models can be developed but will require lake-specific calibration to be effective risk-management tools

[7] regional models exist but global ones do not. Models such as VEMALA [9] already exist for key predictors of algal populations

#### Existing Datasets
Remote sensing multispectral images of the earth are readily available through NASA's Moderate-Resolution Imaging Spectroradiometer (MODIS) which is capable of imaging in the VIS-NIR (459 - 2155 nm) bands at a spatial resolution of 250-500 m and spectral resolution of 20-50 nm.

MODIS has been successfully applied in monitoring blooms [1], however the spatial/temporal resolution and capability is insufficient for prediction alone and must be augmented with ground-based measurements [7]:

![map of ground data](https://github.com/aerjay/algal-blooms/blob/master/media_photos/Ground%20Measurement%20Datasets.png "Global map of ground measurements")

## Vision

A subscription model was selected for government and research/private users seeking predictive functionality since a new model must be 

## Back End
The model used in the proof of concept will consist of only the MODIS-Terra database (see Next Steps: Prediction Model).

#### Classification

## Front End

## Next Steps
#### Prediction Model
- [ ] Access to the MODIS-Aqua product to use spectral images of water bodies in the prediction model
  - the Bloomer team currently only has access to the MODIS-Terra database which does not include large bodies of water and the spectral data has been normalized for land-based uses, resulting in limited image quality over water bodies of interest
- [ ] Training a boosted regression tree (BRT) model for correlating hyperspectral images to key growth variables [6]
  - MacDougall et al. (2018) has shown that LAI, EVI, GEMI, and GVI indices may be correlated to nitrogen content with R<sup>2</sup> = 0.7
  - ARIMA models may be used to project measured variables forward in time as inputs to the BRT
  - Due to the inherent uncertainty in model inputs (estimated from satellite spectral measurements) and the model uncertainty due to the data resolution, an ensemble approach should be applied to the forecast by applying perturbations to model inputs as well as the model weights. The resultant Monte Carlo output may then be used as a probabalistic forecast.

#### User Segment

#### Space Segment

## References
The Bloomer team would like to thank Anthony Tan, Allegra Pearce, and Paul MacKeigan for helping research the topic.

- [1] Mati Kahru and B. Greg Mitchell. MODIS Detects a Devastating Algal Bloom in Paracas Bay, Peru. Eos, Vol. 85, No. 45, 9 November 2004
- [2] Marieke Beaulieu, Frances Pick, Michelle Palmer, Sue Watson, Jenny Winter, Ron Zurawell, and Irene Gregory-Eaves. Comparing predictive cyanobacterial models from temperate regions. Can. J. Fish. Aquat. Sci. 71: 1830–1839 (2014)
- [3] Marieke Beaulieu, Frances Pick, and Irene Gregory-Eaves. Nutrients and water temperature are significant predictors of cyanobacterial biomass in a 1147 lakes data set. Limnol. Oceanogr., 58(5), 2013, 1736–1746
- [4] Dolman AM, Rucker J, Pick FR, Fastner J, Rohrlack T, et al. (2012) Cyanobacteria and Cyanotoxins: The Influence of Nitrogen versus Phosphorus. PLoS ONE 7(6): e38757.
- [5] Anurani D. Persaud, Andrew M. Paterson, Peter J. Dillon, Jennifer G. Winter, Michelle Palmer, Keith M. Somers. Forecasting cyanobacteria dominance in Canadian temperate lakes. Journal of Environmental Management 151 (2015) 343e352
- [6] J.-P. Descy, F. Leprieur, S. Pirlot, B. Leporcq, J. Van Wichelen, A. Peretyatko, S. Teissier, G.A. Codd, L. Triest, W. Vyverman, A. Wilmotte. Identifying the factors determining blooms of cyanobacteria in a set of shallow lakes. Ecological Informatics 34 (2016) 129–138
- [7] Annette BG Janssen, Jan H Janse, Arthur HW Beusen, Manqi Chang, John A Harrison, Inese Huttunen, Xiangzhen Kong, Jasmijn Rost, Sven Teurlincx, Tineke A Troost, Dianneke van Wijk, and Wolf M Mooij. How to model algal blooms in any lake on earth. Current Opinion in Environmental Sustainability 2019, 36:1–10
- [8] GERALD K. MOORE (1980) Satellite remote sensing of water turbidity / Sonde de télémesure par satellite de la turbidité de l'eau, Hydrological Sciences Bulletin, 25:4, 407-421, DOI: 10.1080/02626668009491950
- [9] Huttunen, I., Huttunen, M., Piirainen, V. et al. Environ Model Assess (2016) 21: 83. https://doi.org/10.1007/s10666-015-9470-6
- [10]
- [11]
- [12]
