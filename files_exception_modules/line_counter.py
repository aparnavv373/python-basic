with open("sample.txt","r") as f:
   content= f.readlines()
   print(content)
print("Number of lines in the file:",len(content))