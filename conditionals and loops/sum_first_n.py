# print sum of first N numbers
N=int(input("Enter a number:"))
total=0
i=1
while i<=N:
    total+=i
    i+=1
print(f"Sum of first {N} numbers:",total)