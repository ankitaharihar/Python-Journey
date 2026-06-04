# importing os module
import os

# path of the directory
path = "C:\\Users\\Aditya\\OneDrive\\Desktop"

# storing all files and folders in a variable
files = os.listdir(path)

# printing heading
print("Contents of directory are:")

# loop to print each file and folder name
for file in files:
    print(file)