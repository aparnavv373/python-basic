# write  some text into a file
with open("sample.txt","w") as f:
    f.write("Python is a high-level, general-purpose programming language\n")
    f.write(" Its design philosophy emphasizes code readability with the use of significant indentation\n")
    f.write(" Python is dynamically type-checked and garbage-collected.")
# read the file
with open("sample.txt","r") as f:
    content=f.read()
    print(content)