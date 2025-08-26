import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from collections import defaultdict

data = defaultdict(list)

for line in sys.stdin:
   try:
      key, value = line.strip().split('\t')
      data [key].append(float(value))
   except:
      continue

df = pd.DataFrame(dict(data))

corr_df = df.corr()

plt.figure(figsize=(8,6))
sb.heatmap(corr_df, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()
