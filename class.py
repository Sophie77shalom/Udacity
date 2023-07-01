import math

x = 185
mean = 180
std_dev = 34

# Calculate the probability density function (PDF)
pdf = (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))

# Probability of weighing exactly 185 pounds
probability = pdf

print(probability)
