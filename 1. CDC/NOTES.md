# Learnings:

## XGBoost 
- enable gpu:
    - set tree_method = 'gpu_hist', single_precision_histogram=True, gpu_id=0
    - histogram tree method : 
        - allows distribution
        - continuous feautures bucketed (using hist)
        - fastest method 
    - a lot faster!!
- fastest way to tune :D  (enable gpu and follow steps below)
    1. learning curve for early_stopping and an idea of iterations (as well as maybe the real crapness of some features and comparison with untuned model and baseline)
    2. gridsearchcv on three basic and most important params: learning_rate, n_trees, tree_depth (these are also the longest ones to run)
    3. test vs train to see fit (along w learning curves). If overfitting then regularization tuning.
## Modeling
- AGE model: model results worse than baseline of regression (average across target). from learning curves we see test error coming rapidly UP. Upon removing most of the features besides for age and year, we see the learning curves stick together EXACTLY. This is all the information the model can learn. Need better features. Might be suggestive of the fact that age is not really factoring in obesity. Of course if we do a simple scatter plot we can already see this. 
        
# Questions:
## XGBoost
- Difference between Objective functions and Metric functions?

## Modeling


# TODO:
- effect of adding those magic groupby features? 
- for this investigation, I would join on location and year to get a wide data set with ages, incomes etc to look at all those vars
- compare to and work through original code : https://www.kaggle.com/spittman1248/cdc-data-nutrition-physical-activity-obesity?ref=hackernoon.com&select=Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv