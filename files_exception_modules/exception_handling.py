try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
finally:
    print("Execution complete.")
