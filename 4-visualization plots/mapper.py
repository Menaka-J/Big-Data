from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data
feature_names = iris.feature_names

for i, feature in enumerate(feature_names):
    for row in features:
        print(f"{feature}\t{row[i]}")
