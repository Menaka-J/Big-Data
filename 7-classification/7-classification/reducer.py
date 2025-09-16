import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

sample_ids = []
X = []
y = []

for line in sys.stdin:
    try:
        sample_id, values = line.strip().split('\t')
        *features_str, label_str = values.split(',')
        features = list(map(float, features_str))
        label = int(label_str)

        sample_ids.append(sample_id)
        X.append(features)
        y.append(label)
    except Exception:
        continue

X_df = pd.DataFrame(X)
y_series = pd.Series(y)

# Train-test split for evaluation
X_train, X_test, y_train, y_test, ids_train, ids_test = train_test_split(
    X_df, y_series, sample_ids, test_size=0.3, random_state=42
)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Output predictions for test samples to stdout
for sample_id, pred_label in zip(ids_test, y_pred):
    print(f"{sample_id}\tClass_{pred_label}")

# Print evaluation metrics to stderr
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}", file=sys.stderr)
print("Classification Report:", file=sys.stderr)
print(classification_report(y_test, y_pred), file=sys.stderr)
