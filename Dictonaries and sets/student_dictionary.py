# Create Student Dictionary
student={
    "name":"Aparna",
    "age":22,
    "grade":"A"
}
#Add email key
student["email"]="aparnaxy@gmail.com"

#Update grade
student["grade"]="A+"

#print all keys and values
for key,value in student.items():
    print(f"{key}:{value}")

