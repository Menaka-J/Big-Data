import sys
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

data = defaultdict(list)

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t')
        data[key].append(float(value))
    except:
        continue

df = pd.DataFrame(dict(data))

df.hist(figsize=(10, 6), bins=20, edgecolor='black')
plt.suptitle("Histograms of Iris Features", fontsize=14)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
df.boxplot(rot=45)
plt.title("Boxplot of Iris Features")
plt.tight_layout()
plt.show()
