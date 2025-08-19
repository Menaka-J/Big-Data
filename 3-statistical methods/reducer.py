import sys
import math
from collections import defaultdict

stats = defaultdict(lambda: {
    "count": 0,
    "sum": 0.0,
    "sum_sq": 0.0,
    "min": float('inf'),
    "max": float('-inf')
})

for line in sys.stdin:
    try:
        key, count, sum_val, sum_sq, min_v, max_v = line.strip().split('\t')
        count = int(count)
        sum_val = float(sum_val)
        sum_sq = float(sum_sq)
        min_v = float(min_v)
        max_v = float(max_v)

        stats[key]["count"] += count
        stats[key]["sum"] += sum_val
        stats[key]["sum_sq"] += sum_sq
        stats[key]["min"] = min(stats[key]["min"], min_v)
        stats[key]["max"] = max(stats[key]["max"], max_v)
    except:
        continue

for key, stat in stats.items():
    count = stat["count"]
    total_sum = stat["sum"]
    sum_sq = stat["sum_sq"]
    min_val = stat["min"]
    max_val = stat["max"]

    mean = total_sum / count
    variance = (sum_sq / count) - (mean ** 2)
    std_dev = math.sqrt(variance)
    range_val = max_val - min_val

    print(f"\n--- {key.replace('_', ' ').title()} ---")
    print(f"Count:\t{count}")
    print(f"Sum:\t{total_sum:.2f}")
    print(f"Mean:\t{mean:.2f}")
    print(f"Min:\t{min_val:.2f}")
    print(f"Max:\t{max_val:.2f}")
    print(f"Range:\t{range_val:.2f}")
    print(f"Variance:\t{variance:.2f}")
    print(f"Standard Deviation:\t{std_dev:.2f}")
