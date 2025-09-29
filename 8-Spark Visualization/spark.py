from pyspark.sql import SparkSession
import seaborn as sns
import matplotlib.pyplot as plt

# Start Spark session
spark = SparkSession.builder.appName("IrisPlots").getOrCreate()

# Load Iris dataset via seaborn
iris_pdf = sns.load_dataset("iris")

# Convert to Spark DataFrame
df = spark.createDataFrame(iris_pdf)

# Convert Spark DF to pandas for plotting
pdf = df.toPandas()

# List of numeric features
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# --------- 1. Histograms separately using subplots ----------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # flatten for easy iteration

for i, feature in enumerate(features):
    axes[i].hist(pdf[feature], bins=15, color='skyblue', edgecolor='black')
    axes[i].set_title(f'Histogram of {feature}')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# --------- 2. Single Box Plot for all features ----------
plt.figure(figsize=(8,6))
plt.boxplot([pdf[feature] for feature in features], labels=features)
plt.title("Box Plot of Iris Features (All in One Plot)")
plt.ylabel("Value")
plt.show()

# --------- 3. Statistical Summary for Each Feature ----------
import numpy as np
from scipy import stats

print("\n--- Statistical Summary of Iris Features ---")
for feature in features:
    data = pdf[feature]
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_val = stats.mode(data, keepdims=True)[0][0]
    var_val = np.var(data, ddof=1)  # sample variance
    std_val = np.std(data, ddof=1)  # sample standard deviation

    print(f"\nFeature: {feature}")
    print(f"Mean       : {mean_val:.2f}")
    print(f"Median     : {median_val:.2f}")
    print(f"Mode       : {mode_val:.2f}")
    print(f"Variance   : {var_val:.2f}")
    print(f"Std Dev    : {std_val:.2f}")