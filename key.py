def check_key(dictionary, key):
    if key in dictionary:
        print(f"The key {key} exists in the dictionary.")
    else:
        print(f"The key {key} does not exist in the dictionary.")

# Example dictionary
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Prompting the user for a key
user_key = int(input("Enter a key to check: "))

# Calling the function to check the key
check_key(dict, user_key)
