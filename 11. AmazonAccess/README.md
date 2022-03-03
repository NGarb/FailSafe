This is my work-through of the winning solution of the Amazon Access prediction challenge. 
This can be found at: https://github.com/pyduan/amazonaccess
## NOTES
1. I think going forward, I would like to separate performance modeling from explanatory modeling. Getting into the habit of doing both is probably a good thing
2. brute forcing dozens of feature combinations helps model performance. Is it something good to do in a business/real world application setting? I suppose that would depend on the reason for running the model. 
3. Really need to test the gain in applying this method as opposed to XGBoost on raw
4. I found myself getting 'stuck' on this project for too long. This is something I am trying to avoid with the incremental learning approach where with every new project I aim to learn one new thing and move through projects fast. I will take what I have learned so far and apply it. Marking this project as one to possibly come back to. 

## LEARNING 
- feature creation 
    - really cool so far. generating features of all combinations of deg 2 and deg 3 and hashing 
    - for every single combination (of deg 2/3), the 2/3 features are tupled together and hashed resulting in one new column
    - after the tuple hash column is created, all columns are stacked together. These are one hot encoded : i.e. for each column a matrix is created which represents column value and frequency in a sparse binary representation
    - the trick of combining two numeric columns - a + 1000*b. 
    - the groupby trick: count/freq of each col (and logging the counts)
    - % of department that is the resource
    - number of resources a manager manages
    - common but haven't seen it used recently: remove zero variance features
    
## QUESTIONS
- Greedy feature selection loop: don't understand the cumulative feature adding and training, This means that for each new feature you are adding to the selection, you are evaluating how well it plus all its predecessors are doing. Then you are still selecting them as if they are independent. 
- why remove last added feature from list?
- how well does this type of thing generalize? All the feature engineering is so cool. I guess based on the fact that this is the winning solution, it performs really well on test. And I guess in a real world setting, you would have be recreating these features and retraining this model periodically. 
- why drop role code? redundant?
- how were the initial selected models selected? 
- why do we create features based off of the pivot table (cross-tab counts) and not off the features directly?

## FIGURED OUT
- pivot table: 
    - for each column: we have entries for all unique values of the column plus total (count of all values)
    - for each unique value: we have value counts of all other columns'unique values at that value. 

