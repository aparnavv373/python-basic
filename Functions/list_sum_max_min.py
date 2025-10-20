numbers=(input("Enter numbers seperated by spaces:")).split()
numbers=[int(num) for num in numbers]
print("Sum",sum(numbers))
print("Minimum:",min(numbers))
print("Maximum:",max(numbers))
