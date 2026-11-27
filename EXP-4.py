
import statistics as st

# Input dataset
data = input("Enter dataset elements separated by spaces: ").split()

# Convert input elements into integers
for i in range(len(data)):
    data[i] = int(data[i])

# Calculate Mean, Median and Mode
mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)

# Display results
print("Mean (Expectation) =", mean)
print("Median =", median)
print("Mode =", mode)
