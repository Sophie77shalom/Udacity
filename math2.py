import math

p = 0.15
n = 60
k = 7

# Calculate the binomial coefficient (n choose k)
binomial_coefficient = math.comb(n, k)

# Calculate the probability mass function (PMF)
pmf = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))

print(pmf)
