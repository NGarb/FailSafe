## Results are contained in Data folder under test_results.csv

Note: 
- no data is deleted in case there is need for comparison/reproducibility/general ease of use.
- please edit paths as needed

## Summary
In this exercise, we explore the data and its various features, find out how best to fill the missing data as well as experiment with some feature engineering before investigating various modeling approaches and derive model insights. 

For best model results, see script "4: model_lag_deltas". 

## Best Results

Summary of best performing model:
- GridSearch XGBoost with no regularization trained on delta features

- AUC: 0.898409, 
- F1 macro: 0.706612, 
- F1 weighted: 0.747307, 
- Accuracy: 0.750570

Looking at our best performing model and extracting tree-based feature importance (weight i.e. number of times a feature is used to split the data across all trees) we have the following features in order: 
1. equity_ratio
2. cash_ratio
3. profit_after_net_financial_items
4. equity
5. profit_margin

## Improvements
Given more time and should there be a need:
1. Test more models tuned by human (not AutoML)
2. Play with feature creation - golden features, seeing if there are any easily available features for these companies such as work-force, industry etc
3. Dive into error analysis
4. Run an explanatory dashboard with model insights on a feature level, observation level and general level

## Data observations
From exploratory analysis, the shape of the missing data is systematic. This is completely explained upon investigation of what the features mean. If a company is new or has not submitted its financials data, we will of course have missing data for all columns related to the missing year lags for that row. We derive features on the consistency of data submission based on dates as well as how many years there are submitted. We do not see this coming into the top most important features - this might not affect the credit rating that is assigned to companies. We do however observe that zero-filling these is not only logically correct but also performs better in modeling. 

Payment date and amount may be important features; however, they are present for about ten percent of rows and as such are initially discarded. For future improvements of the work in order to gain some marginal model performance improvement, we may decide to bring this feature back as a binary columns signifying whether or not it is present. 

Taking a closer look at the target feature, we see that there is a class imbalance but it is not so severe that we have to get creative with techniques. Looking at AutoML performance confusion matrix, we can see that without any optimizations, Rating class C is the least accurate. Interestingly, this is improvement by some feature engineering. Instead of using the actual values for the lagged years, we calculate the delta. This helps with pattern recognition for classes. If we examine the AutoML explain folder, the top performing model is the Ensemble and here we can see in the README that the class with the lowest F1 score is 0.618182 for class C (this is definitely not bad to start). Very interestingly, the top performing model for AutoML performance mode is XGBoost. This is why we just pick this for custom work and proceed with the 'manual' observation using the XGBoost model. Given more time we would have included other models; however, for this use-case this is overkill. We examine the Catboost model in the AutoML folder (default since it performs better). Catboost is more robust than xgboost due to the feature permutation built into the structure of the model which makes it more stable. Typically we don't trust permuation feature importance for tree-based models; however, for Catboost this can be indicative. The permutation importance reveals that equity_ratio, profit_after_net_financial_items, and cash ratio are the top 3 most important features. The SHAP feature importance from the AutoML XGBoost folder has the exact same three features in the same order. 

