from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

def calc_results_row(y_pred, y_true, model):
    
    f1 = f1_score(y_true, y_pred, average='macro')
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='macro')
    recall = recall_score(y_true, y_pred, average='macro')
    
    row = {'model' : model,
           'f1': f1,
           'accuracy': acc, 
           'precision': prec,
           'recall': recall}
    return row