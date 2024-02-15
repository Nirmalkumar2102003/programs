import os

print("List directory contents:")
print(os.listdir())

print("Current directory:")
print(os.getcwd())

a= input("Enter the name of the file to create: ")
print(os.mkdir(a))
print("File created")

# Check if a path exists
b= input("Enter a path to check if it exists: ")
print("Path exists:", os.path.exists(b))

# Check if a file exists
c= input("Enter a file to check if it exists: ")
print("File exists:", os.path.isfile(c))

# Remove a directory
d = input("Enter a directory to remove: ")
os.rmdir(d)
print("Directory removed")
