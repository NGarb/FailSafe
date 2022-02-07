# Learned
- Using MICE! Multiple Imputation Chained Equations
- this is found in the library *fancyimpute*
- https://www.indexmundi.com/aruba/ -- all sorts of indices for countries
- refreshed pipes and encoding. 
    - label encoding = mapping to increasing natural numbers len(num_categories)
    - one hot = 1s and 0s
- refresher on target scaling
- yay for yellowbrick!! residuals plot and prediction error plot
- NB! XGBOOST.TRAIN(DMATRIX) VASTLY DIFFERENT RESULTS TO XGBREGRESSOR.FIT(X_TRAIN)
    - error is so much larger for former? 
- v v simple but obv important: plot of y vs yhat unscaled. Our model does well :D and we achieve a very small error
- hyperopt implementation - much simpler than I've ever made it. Convergence feels slow and my results are better with manual tuning for now. would like to experiment. 
- in hyperopt, if you are using a classification metric such as AUC that you are trying to maximize then in the objective you will return {'loss': -accuracy, 'status': STATUS_OK }. for LOSS metrics such as RMSE, do NOT do this as it will maximize the score and do the opposite of what you are trying to achieve. 
- played around with taking sample space options from uniform to normal and this did absolutely nothing for convergence
- for this particular example, no tuning could beat the default params. Manual tuning was a bit worse but hyperopt was v bad. 
- tried out TPOT! so fast! and interesting results!
- don't drop/truncate/overwrite original X_test since it helps with seeing where the model didn't predict

# To investigate
- investigate library fancyimpute
- FastML
- ?? XGBOOST.TRAIN(DMATRIX) VASTLY DIFFERENT RESULTS TO XGBREGRESSOR.FIT(X_TRAIN)
- prediction_plot (yellowbrick plot of y vs yhat) -- would be cool to do on non-scaled version to see if systematic incorrect prediction
- how to design mu and sigma for hyperopt hp normal?


# Thus far core kit:
- sklearn 

# TODO
- compile my utils lib for stuff I find myself repetitively moving from one nb to another
- clean up pipelines
- start to split out data exploration and clean up modules from modeling modules
- so. the above X2. create separate modules for everything. data cleaning, data exploring, data training, evaluation, then explaining. all of these should be linked via outputs and inputs in order to make stuff easy to work with and neat. 
- good lord. fit categorical encodings on full dataset. scaling on train. 
- more exploration work with SHAP
- ALL RIGHT. LEFT "hyper_params_1.ipynb" for later as it is deviating from xgboost to optimization. But really do want to return

# Note:
- because we are using trees, I don't bother scaling anything - target or input. It shouldn't be necessary but is still good practice
- UGHHHHH this whole time I have been splitting test set into test and val and using val as test. OBVIOUSLY leakage. fix. 
- used FastML for this. 
- Our model actually does pretty well :D 
- my biggest question is how tuning the model was just hopeless because default params were the best and then regularization made things worse. 
- wondering if its best to actually just save indices of test, train, validation in order not to save full dataframes?