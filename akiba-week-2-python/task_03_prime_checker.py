n=int(input("Enter a number: "))
if n<2:
    isPrime=False
else:
    for i in range(2,n):
        if n%i==0:
            isPrime=False
            break
        else:
            isPrime=True

print(f"Is the number prime? {isPrime}")