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
The location data included in the dataset is not anonymized and can be used to “scrape” or obtain weather data based on the date when the variety was sowed (Indian Meteorological Department, data.gov.in). Using the same locations and date

## Data Preparation

The gross yield was removed 
The Sown and Harvest dates were combined to create the Days Till Harvest. 

The categorical variables need to be converted to dummy variables. The weather and location (latitude, longitude) data was cleaned and transformed. For regression the data may also need to be transformed to the spline basis (polynomial basis?). 

## Modeling

Regression for a better understanding of the coefficients. Since there will be quite a lot of features, regularization could come in handy. Will attempt and try both Ridge and Lasso.
Clustering could also be an interesting idea and could lead to some unexpected patterns. 
Possibly building a graph of varieties 
If the model is just based on prediction than Random Forest or Gradient Boosted models could also work.

## Evaluation
if information can be obtained. The model could be validated with historical results in those areas too. 
 
## Deployment

A website could be used here to present the findings. If location data is provided, then the regions could be visualized on a map and each area would contain information on the recommended crop varieties for that region. 

## References
