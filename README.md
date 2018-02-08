# Yield Prediction and Variety Recommender

Improving the procedure for estimating the total amount of seed that needs to be produced can save a global seed company millions of dollars. 
By building a predictive model for the dry yield (how much useful product was harvested/extracted) of crops in Southern India, I was able to develop a procedure for forecasting the dried yield per acre of a farm. Recommending specific high yield varieties to locations within the region was another method that I used to improve the efficiency of the farms. 
The ideas behind this project can be applied to other crops and can be scaled to bigger regions.

## Business Understanding

The value of the total seed produced in this region is about $60 million. So a variability of 1.5% in the projected production can result in a loss of about $1 million for a surplus, and $2.5 million for a deficit. Minimizing this uncertainty can be vital especially when scaling up to bigger regions. 

The problem is to estimate the amount of seed that will be required for regions in Southern India and by building a predictive model for the dry yield per acre, the total seed production can be better estimated. Recommendeing specific high yield varieties for the different locations and also providing recommendations for each variety are also other ideas that can be incorporated into the solution. 

## Data Understanding

### Crop Data
I received anonymized crop data from a major global seed company, which contains the yield for different varieties at different locations. 

### Weather and Location Data
The location data (latitude, longitude, elevation) included in the dataset is not anonymized and can be used to “scrape” or obtain weather data based on the date when the variety was sowed (Indian Meteorological Department, data.gov.in). Using the same locations and date

## Data Preparation

The Gross Yield was removed and the response was converted to Dried Yield Per Acre (Dried Yield / Standing Area).

The Sown and Harvest dates were combined to create the Days Till Harvest. 

The Sowing Month and Sowing Week were combined to create the Sowing Week of Year.

The weather and location data (latitude, longitude, elevation) was aggregated. 
For regression the data may also need to be transformed to the spline basis (polynomial basis?). 

The varieties were converted to dummy variables.

## Modeling

Inference and Recommendations:
Regression for a better understanding of the coefficients and to recommend the varieties.
Matrix Factorization - Singular Value Decomposition (SVD)

Prediction models:
Random Forest Regressor 
Gradient Boosted Regressor

## Evaluation

10-fold cross validation 

If information can be obtained. The model could be validated with historical results in those areas too. 
 
## Deployment

Interface with map of India and the relevant states highlighted. The bubbles present on the states would display, when hovered over, the locations and the varieties that are recommended along with recommendations for the varieties. 

## References

Indian Meteorological Department, http://hydro.imd.gov.in/hydrometweb/(S(caavbb45wqmmz4q1zopq1c45))/DistrictRaifall.aspx
https://www.whatismyelevation.com
