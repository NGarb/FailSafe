# NOTES:
- really really happy with the script that compares different types of encoders. I think it really makes a lot of sense. For different columns and different problems, different types of encodings are going to work better. Then also, if it is a task more geared toward explainability, then using one hot encoding with lasso/random forest for level pruning will be a good idea. Interesting to see if it would drop accuracy by so much. Anyway. Another cool step in the whole process. Also I'm liking working without dimensionality reduction for simple tabular data. From past experience it never works well for this. And then with tabular data tasks, you kind of always want some sort of explainability kind of stuff etc. 


# TODO
1. put preprocessing into separate components after data explorations
2. specific notebook comparing the effects of using different category encoders 
3. re-read and work through the James Stein encoding https://kiwidamien.github.io/james-stein-encoder.html
4. run hyperopt for 5000 trials to see if this helps. Will run cross-validation in the objective function next.
5. leave out hyperopt in favour of optuna
6. check for any infinite or NaN values after encoding.
7. use_cat_names = True in one hot
8. change feature names for one hot to corresponding classes 
    - note: use preprocessor.transformers_[2][1].named_steps['encoder'].category_mapping
9. ExplainerDashboard is tuned with loss in r2. Probably better to choose rmse.

# LEARNED
- refreshed category_encoders lib 
    - https://practicaldatascience.co.uk/machine-learning/how-to-use-category-encoders-to-transform-categorical-variables
- used optuna for the first time. It seems to do better. Like I know they use the same methods under the hood and I must be going crazy but 0_0. 
- using Explainer Dashboard. What an amazing experience. 
    
# QUESTIONS
- I just don't seem to get very good results using hyperopt. I run for 1000 trials. Would increasing this help? Not sure. Granted, gridsearchcv is cross validated and is run on only train but test results speak for themselves. 
- OMG I keep getting so confused with under predicting and over predicting and negative and positive residuals. Are residuals always y - yhat or is it yhat - y 
- after looking at residuals and identifying any groups that under or overpredict. What to do with those rows?
- Explainer dashboard: using this with scaled features is really difficult?
