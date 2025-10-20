my_string=input("Enter a string:").strip()

#Dictionary to store character counts
count={}

for char in my_string:
    if char  not in count:
        count[char]=1
    else:
        count[char]+=1
print("charcter counts:",count)