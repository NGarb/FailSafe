## Objectives

For this project, I want to continue perfecting my pipeline as well as add some things I learned from the Amazon Access (11) nb

1. Have explanatory modeling as well as performance modeling
2. In the performance modeling, I would like to try staking models 
3. I want to create the polynomial featuresets, the engineered feature sets, the greedy feature selection


There is no set problem statement for this dataset, so we will predict price because we want to experiment with techniques more so that find an interesting problem in this specific dataset

## TODO
- put categorical encoding selection into Utils
- put simple modeling pipeline into Utils
- add pearson's correlation to reg errors and mae and mad: mean absolute deviation from the median
- automate scaling selection
- automate baseline 
- automate some parts of the pipeline eg compiling results_df

## learned
- If RMSE is high and mape is low (comparatively) then the predictions are being skewed by outliers
- really interesting. Hyperopt tuned in such a way as the mape was higher (most predictions were dispersed slightly further from truth but no outliers). Better generalization? 
- hp choice returns the index of the input list/array
- hp choice is much faster than choosing from a distribution
- always dismissed model choice as secondary to features and problem definition but seeing the results of xgb vs lgm vs ctb has changed my mind
- from Amazon Access solution: never ever would have thought about unrolling all features (sparsify dataset), training logistic regression models and populating the dataset with the coefficients



robust.scale.mad(state['Population'])
