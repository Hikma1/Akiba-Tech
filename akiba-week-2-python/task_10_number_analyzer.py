largest = None
smallest = None
total = 0
even_count = 0
odd_count = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))

    # Initialize largest and smallest with first number
    if largest is None:
        largest = num
        smallest = num

    # Update largest and smallest
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    # Update sum
    total += num

    # Count even and odd
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 10

print("\n--- Analysis Result ---")
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)