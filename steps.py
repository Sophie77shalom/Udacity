def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Example usage:
c0 = int(input("Enter a non-negative, non-zero integer: "))
num_steps = collatz_steps(c0)
print("Number of steps:", num_steps)
