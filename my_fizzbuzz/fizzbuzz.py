#!/usr/bin/env python
# coding: utf-8

# Build lists of multiples of 3 & 5.
def multiples():
    b = 3
    c = 5
    x = []
    y = []
    for i in range(34):
        x.append(b*i)
    for i in range(21):
        y.append(c*i)
    return x, y


# Print 'Fizz', 'Buzz', 'Fizzbuzz', or number from value in list.
def fizzbuzz(num):
    # Print 'fizz' if multiple of 3 and not 5
    if (num in x) & (num not in y):
        print('fizz')
        return
    # Print 'buzz' if multiple of 5 and not 3
    if (num in y) & (num not in x):
        print('buzz')
        return
    # Print 'fizzbuzz' if multiple of both 3 and 5
    if (num in x) & (num in y):
        print('fizzbuzz')
        return
    # Print value if none of the above apply
    else:
        print(num)
        return

# Create a list of 1 - 100.
def create_list():
    list_to_use = []
    # Create a list from 0 - 100
    for i in range(101):
        # Build list.
        list_to_use.append(i)
    # Remove first value, a '0'
    list_to_use.pop(0)
    # Return list of 1 - 100
    return list_to_use

# Program.
def main():
    # Get list of numbers ranging from 1 - 100.
    numbers = create_list()
    # Iterate through list for to FizzBuzz
    for n in numbers:
        fizzbuzz(n)
    return

# Run Program.
if __name__ == '__main__':
    main()
