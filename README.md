# Yield Prediction and Variety Recommender

Improving the procedure for estimating the total amount of seed that needs to be produced can save a global seed company millions of dollars. 
By building a predictive model for the dry yield (how much useful product was harvested/extracted) of crops in Southern India, I was able to develop a procedure for forecasting the dried yield per acre of a farm. Recommending specific high yield varieties to locations within the region was another method that I used to improve the efficiency of the farms. 
The ideas behind this project can be applied to other crops and can be scaled to bigger regions.

## Business Understanding

By building a predictive model for the dry yield (how much useful product was harvested/extracted) of crops, the partial dependencies of the crop varieties can be used to recommend the variety that would increase the dry yield the most. This will also provide some more insight into the features that are contributing to the change in yield. 
More features and weather interactions could also be taken into consideration. 

The varieties and locations could be split into groups. Analysis on the locations / villages that produce vast amounts of yield as opposed to smaller villages. Improving efficiency in the larger locations may prove to be more worthwhile than the smaller ones. In order to focus on specific locations and varieties, the overall efficiency and “value” of the particular “field” could be inferred. This could drive decision making where certain customers or areas are targeted for growth. Locations where focusing on growth would minimize losses or maximize profits and locations could be grouped by high yield or low yield. 

The company also does produce a large amount of seed based on the yield expected for specific locations. They would like to develop some methods to better predict the amount of seed that will be needed and to minimize shortages and surpluses. 
Could possibly account for the specific shift in patterns (weather or otherwise) to prepare and produce more or less seed for specific varieties based on yield. 

## Data Understanding

Monsanto. I have already received a data set and it contains the yield for different varieties at different locations during different seasons. The location data included in the dataset is not anonymized and can be used to “scrape” or obtain weather data based on the date when the variety was sowed (Indian Meteorological Department, data.gov.in). Using the same locations and date, if doable, soil data can also be obtained. (data.gov.in)

## Data Preparation

The data is already quite clean. The date-time variables will have to be changed to something more quantifiable. Possibly, days since the reference date Epoch (January 1, 1970 midnight UTC/GMT). The categorical variables need to be converted to dummy variables. Leaky features (e.g. gross yield) will need to be removed. The soil and weather data will have to be obtained, cleaned and transformed. For regression the data may also need to be transformed to the spline basis (polynomial basis?). 

## Modeling

Regression for a better understanding of the coefficients. Since there will be quite a lot of features, regularization could come in handy. Will attempt and try both Ridge and Lasso.
Clustering could also be an interesting idea and could lead to some unexpected patterns. 
Possibly building a graph of varieties 
If the model is just based on prediction than Random Forest or Gradient Boosted models could also work.

## Evaluation
if information can be obtained. The model could be validated with historical results in those areas too. 
 
## Deployment

A website could be used here to present the findings. If location data is provided, then the regions could be visualized on a map and each area would contain information on the recommended crop varieties for that region. 

