number=int(input("Enter a number: "))
count=0

for i in range(1,number+1):
    if number%2==0:
        count+=1
    sum=number+1
print(f"The number of even numbers between 1 and {number} is {count}.")
print(f"The number of odd numbers between 1 and {number} is {number-count}.")
print(f"The sum of all numbers between 1 and {number} is {sum}.")