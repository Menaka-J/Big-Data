import sys
import pandas as pd
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


data = defaultdict(list)

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t')
        data[key].append(float(value))
    except:
        continue

df = pd.DataFrame(dict(data))

k = 3   
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(df)

for idx, cluster_id in enumerate(clusters):
    print(f"Sample_{idx}\tCluster_{cluster_id}")

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=clusters, cmap='viridis', s=50)
plt.title("KMeans Clusters of Wine Dataset (PCA-reduced)")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.colorbar(scatter, label='Cluster')
plt.tight_layout()
plt.show()