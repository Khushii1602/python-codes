def sum_of_numbers(numbers):
    return sum(numbers)

# Ask the user to input a list of numbers
user_input = input("Enter a list of numbers, separated by spaces: ")

# Convert the user input string to a list of numbers
numbers_list = list(map(float, user_input.split()))

# Calculate the sum of the numbers
total_sum = sum_of_numbers(numbers_list)

# Print the sum
print(f"\nThe sum of the numbers is: {total_sum}")