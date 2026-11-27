
import statistics

# Input dataset
data = input("Enter dataset elements separated by spaces: ").split()

# Convert elements into integers
for i in range(len(data)):
    data[i] = int(data[i])

# Calculate mean
mean = statistics.mean(data)

# Calculate variance and standard deviation
variance = statistics.variance(data)
std_dev = statistics.stdev(data)

# Display results
print("\nMean =", mean)
print("Variance =", variance)
print("Standard Deviation =", std_dev)

