import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Function: partition
# Partitions the array around a chosen pivot element

def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

# Function: median_of_medians
# Selects a good pivot deterministically using median of medians

def median_of_medians(arr, low, high):
    n = high - low + 1
    if n < 5:
        arr[low:high + 1] = sorted(arr[low:high + 1])
        return low + n // 2

    medians = []
    for i in range(low, high + 1, 5):
        group = arr[i:min(i + 5, high + 1)]
        group.sort()
        medians.append(group[len(group) // 2])

    med_index = median_of_medians(medians, 0, len(medians) - 1) if len(medians) > 1 else 0
    pivot_value = medians[med_index]
    pivot_index = arr.index(pivot_value, low, high + 1)
    return pivot_index

# Function: deterministic_quickselect
# Main recursive function for selecting kth smallest element

def deterministic_quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = median_of_medians(arr, low, high)
    pivot_index = partition(arr, low, high, pivot_index)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return deterministic_quickselect(arr, low, pivot_index - 1, k)
    else:
        return deterministic_quickselect(arr, pivot_index + 1, high, k)

# Experimental Evaluation

sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
experimental_times = []

for n in sizes:
    arr = [random.randint(1, n * 10) for _ in range(n)]
    k = n // 2
    start = time.time_ns()
    deterministic_quickselect(arr.copy(), 0, len(arr) - 1, k)
    end = time.time_ns()
    experimental_times.append(end - start)
    
# Theoretical O(n) Computation and Normalization

theoretical = [n for n in sizes]
avg_exp = np.mean(experimental_times)
avg_theo = np.mean(theoretical)
scaling_constant = avg_exp / avg_theo
adjusted_theoretical = [val * scaling_constant for val in theoretical]

# Display Numerical Data

print("3.3 Output Numerical Data")
print("n | Experimental Result (in ns) | Theoretical Result")
for i in range(len(sizes)):
    print(f"{sizes[i]} | {experimental_times[i]} | {theoretical[i]:.9f}")
    
# Plot Graph - Runtime Comparison

plt.figure(figsize=(9,5))
plt.plot(sizes, adjusted_theoretical, marker='o', color='orange', label="Theoretical Time (O(n))")
plt.plot(sizes, experimental_times, marker='x', color='blue', label="Experimental Time")
plt.title("Deterministic Quickselect (Median of Medians) Runtime Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Complexity (in ns)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Scaling Constant Display

print(f"\nScaling Constant Used for Normalization: {scaling_constant:.6f}")

