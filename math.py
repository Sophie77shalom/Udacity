import math

x1 = 120
x2 = 155
mean = 180
std_dev = 34

# Calculate the cumulative probability for x1
cdf_x1 = (1 / 2) * (1 + math.erf((x1 - mean) / (std_dev * math.sqrt(2))))

# Calculate the cumulative probability for x2
cdf_x2 = (1 / 2) * (1 + math.erf((x2 - mean) / (std_dev * math.sqrt(2))))

# Probability of weighing between 120 and 155 pounds
probability = cdf_x2 - cdf_x1

print(probability)
