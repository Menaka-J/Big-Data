from sklearn.datasets import load_wine

wine = load_wine()
features = wine.data
feature_names = wine.feature_names

for i, feature in enumerate(feature_names):
    for row in features:
        print(f"{feature}\t{row[i]}")
