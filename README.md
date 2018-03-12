# Yield Prediction and Variety Recommender

Improving the procedure for estimating the total amount of seed that needs to be produced can save a global seed company millions of dollars. 
By building a predictive model for the dry yield (how much useful product was harvested/extracted) of crops in Southern India, I was able to develop a procedure for forecasting the dried yield per acre of a farm. Recommending specific high yield varieties to locations within the region was another method that I used to improve the efficiency of the farms. 
The ideas behind this project can be applied to other crops and can be scaled to bigger regions.

## Business Understanding

The value of the total seed produced in this region is about $60 million. So a variability of 1.5% in the projected production can result in a loss of about $1 million for a surplus, and $2.5 million for a deficit. Minimizing this uncertainty can be vital especially when scaling up to bigger regions. 

The problem is to estimate the amount of seed that will be required for regions in Southern India and by building a predictive model for the dry yield per acre, the total seed production can be better estimated. Recommending specific high yield varieties for the different locations and also providing recommendations for each variety are also other ideas that can be incorporated into the solution. 

## Data Understanding

### Crop Data
I received anonymized crop data from a major global seed company, which contains the yield for different varieties at different locations. 

### Weather and Location Data
The location data included in the dataset is not anonymized and was used to “scrape” or obtain weather data based on the date when the variety was sowed (Indian Meteorological Department, data.gov.in). I also gathered latitude, longitude and elevation for the different locations and tested these features.  

## Data Preparation

The Gross Yield was removed and the response was converted to Dried Yield Per Acre (Dried Yield / Standing Area).

The Sown and Harvest dates were combined to create the Days Till Harvest. 

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/days_till_harvest_scatter.png)

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/days_till_harvest_boxplot.png)

The Sowing Month and Sowing Week were combined to create the Sowing Week of Year.

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/sowing_week_year_hist.png)

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/sowing_week_year_boxplot.png)

The weather data was aggregated based on the first 3 months after the plant was sown.
For regression the data was also transformed to degree 2 and 3 polynomials and those models were also compared. 

Finally, the varieties were converted to dummy variables.

## Modeling

Inference and Recommendations:
* Regression for a better understanding of the coefficients and to recommend the varieties.
* Matrix Factorization - Singular Value Decomposition (SVD): Matrix factorization was attempted to try to recommend varieties to particular locations for which data was not available. Using the dry yield as a "rating", varieties were recommended and compared to the regression recommendations. This was not entirely successful as domain knowledge along with other factors would be very influential in this area. There are biological and agricultural reasons for variety recommendations and this matrix factorization technique would struggle to incorporate that. 

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/regression_coefs_capstone.png)

Prediction models:

* Random Forest Regressor 
* Gradient Boosted Regressor

## Evaluation

10-fold cross validation, polynomial models did not perform very well. 

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/capstone_test_errors.png)

If information can be obtained. The model could be validated with historical results in those areas too. 
 
## Deployment

Interface with map of India and the relevant states highlighted. The bubbles present on the states would display, when hovered over, the locations and the varieties that are recommended along with recommendations for the varieties. 

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/Screen%20Shot%202018-02-06%20at%2012.12.04%20AM.png)

![alt text](https://github.com/anubhavrana/Capstone-Yield-prediction-and-Variety-recommender/blob/master/img/Screen%20Shot%202018-02-07%20at%201.13.22%20AM.png)

## Further Work

* Quantify Recommendations for Varieties: 
* Incorporate More Weather Variables: Temperature, Humidity, Hours of Sunlight
* Incorporate Soil Data
* Gather Location-Based Variety Data for Recommendations
* Attempt to use mixed models (treating Year as Random Variable)

## References

Indian Meteorological Department, http://hydro.imd.gov.in/hydrometweb/(S(caavbb45wqmmz4q1zopq1c45))/DistrictRaifall.aspx
https://www.whatismyelevation.com

