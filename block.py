blocks = int(input("Enter the number of blocks: "))

height = 0
total_blocks = 0

while total_blocks < blocks:
    height += 1
    total_blocks += height

if total_blocks > blocks:
    height -= 1

print("The height of the pyramid that can be built is:", height)

for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))
