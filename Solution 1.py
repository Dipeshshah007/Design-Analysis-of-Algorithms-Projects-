import time
import math
import numpy
import matplotlib.pyplot as plt

# Function representing the given code
def pseudoCode(n):
    j = 2
    Sum = 0
    a = list(range(n+1))
    b = list(range(n+1))
    while j < n:
        k = j
        while k < n:
            Sum += a[j] * b[k]  # actual operation
            k = k * k
        j = 2 * j
    return Sum

# Theoretical time complexity O(log n * log log n)
def theoretical_time(n):
    if n <= 2:
        return 1
    return math.log2(n) * math.log2(math.log2(n))

# Values of n to test
nRange = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
theoreticalTime = []
experimentalTime = []

# Measure theoretical and experimental times
for n in nRange:
    # Theoretical time complexity
    theoreticalTime.append(theoretical_time(n))

    # Measuring experimental time
    startTime = time.perf_counter_ns()
    pseudoCode(n)
    endTime = time.perf_counter_ns()
    experimentalTime.append(endTime - startTime)
    print(f"n={n}, Experimental={experimentalTime[-1]}, Theoretical={theoreticalTime[-1]}")

# Normalization of Theoretical Values using a scaling method
theoretical_avg, experimental_avg = numpy.average(theoreticalTime), numpy.average(experimentalTime)
scaling_constant = experimental_avg / theoretical_avg
print(f"Scaling constant: {scaling_constant}")

theoreticalTime = [theoreticalTime[i] * scaling_constant for i in range(len(theoreticalTime))]
print('thereotical values are: ', theoreticalTime)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting theoretical times
plt.plot(nRange, theoreticalTime, label="Theoretical Time (O(log n * log log n))", marker='o')

# Plotting experimental times
plt.plot(nRange, experimentalTime, label="Experimental Time", marker='x')

# Logarithmic scale for better comparison
plt.xscale('log')
plt.yscale('log')

plt.xlabel("n (log scale)")
plt.ylabel("Time (ns, log scale)")
plt.title("Comparison of Theoretical and Experimental Time Complexity")
plt.legend()

# Show the plot
plt.show()
