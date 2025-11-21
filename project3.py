import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

# --------------------------------------------------------
# Pseudo-Polynomial Subset Partition DP
# --------------------------------------------------------
def can_partition(arr):
    S = sum(arr)
    if S % 2 != 0:
        return False

    target = S // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    return dp[target]


# --------------------------------------------------------
# Measure runtime in nanoseconds
# --------------------------------------------------------
def measure_runtime_ns(arr):
    start = time.time_ns()
    can_partition(arr)
    end = time.time_ns()
    return end - start


# --------------------------------------------------------
# EXPERIMENTAL ANALYSIS
# --------------------------------------------------------
n_values = [50, 100, 200, 400, 600, 800, 1000, 1500, 2000]

results = []

for n in n_values:
    times = []
    sums = []

    # generate smooth pseudo-polynomial behaviour: S ≈ 10n
    for _ in range(5):
        arr = [random.randint(1, 20) for _ in range(n)]
        sums.append(sum(arr))
        times.append(measure_runtime_ns(arr))

    avg_runtime = mean(times)
    avg_sum = mean(sums)

    print(f"n = {n}, sum ≈ {avg_sum:.0f}, avg_runtime = {avg_runtime} ns")

    results.append({
        "n": n,
        "sum": avg_sum,
        "runtime_ns": avg_runtime,
        "complexity_metric": n * avg_sum   # O(n·S)
    })


df = pd.DataFrame(results)

# --------------------------------------------------------
# THEORETICAL SCALING — YOUR REQUESTED METHOD
# scaling_factor = avg(experimental_times) / avg(theoretical_values)
# --------------------------------------------------------

avg_exp = df["runtime_ns"].mean()
avg_theo = df["complexity_metric"].mean()

scaling_factor = avg_exp / avg_theo

print("\n=== Scaling Factor Computation ===")
print(f"Average Experimental Runtime (ns): {avg_exp:.4f}")
print(f"Average Theoretical Value (n × S): {avg_theo:.4f}")
print(f"Scaling Factor = avg_exp / avg_theo = {scaling_factor:.10f}\n")

df["scaled_theoretical_ns"] = df["complexity_metric"] * scaling_factor

# --------------------------------------------------------
# PRINT SUMMARY TABLE
# --------------------------------------------------------
print("=== Detailed Table ===")
print(df.to_string(index=False))


# --------------------------------------------------------
# PLOT COMPARISON GRAPH
# --------------------------------------------------------
plt.figure(figsize=(10, 6))

plt.plot(df["n"], df["runtime_ns"], marker='o', label="Experimental Runtime (ns)")
plt.plot(df["n"], df["scaled_theoretical_ns"], marker='s', linestyle="--",
         label="Scaled Theoretical O(n·S) (ns)")

plt.xlabel("n")
plt.ylabel("Runtime (nanoseconds)")
plt.title("Experimental vs Theoretical Runtime (Pseudo-Polynomial O(n·S))")
plt.grid(True)
plt.legend()

plt.show()
