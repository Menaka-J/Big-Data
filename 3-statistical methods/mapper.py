from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']      
feature_names = data['feature_names']  

for col_index, col_name in enumerate(feature_names):
    for row in features:
        value = float(row[col_index])
        key = col_name.replace(" ", "_")  
        print(f"{key}\t1\t{value}\t{value**2}\t{value}\t{value}")

