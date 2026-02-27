# Take input from the user
number = int(input("Enter your number: "))

# Store the original number for comparison later
reversed_number = 0

temp = number
# Reverse the number
while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

# Check if the original number and the reversed number are the same
if number == reversed_number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")