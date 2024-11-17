#create a new file
new_file1 = open('new_file1.txt', 'x')
new_file1.close()

#check if a file exists
import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
    print("The file does not exist")
    
# creat a new if it does not
my_file = open('my_file.txt', 'w')
my_file.write("Hi! I am Penguin and I am 1yr old.")
my_file.close()

#delete file name coding
os.remove('coding2.txt')

#delete the folder
os.rmdir('folder')