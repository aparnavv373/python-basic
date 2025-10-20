secret_number=5
number=int(input("Enter a number:"))
if number==secret_number:
    print("correct!")
elif number>secret_number:
    print("Too high")
elif number<secret_number:
    print("Too Low")
