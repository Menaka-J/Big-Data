from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
features = data.data
labels = data.target
n_samples, n_features = features.shape

for i in range(n_samples):
    feature_str = ','.join(map(str, features[i]))
    label = labels[i]
    print(f"Sample_{i}\t{feature_str},{label}")
