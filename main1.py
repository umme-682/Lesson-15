#write in file using with() function
with open('coding1.txt', 'w')as file:
    file.write("Hi! I am Penguin and I am 1yr old.")
file.close()

#split file into words
with open('coding1.txt', 'r')as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
      word = line.split()
      print(word)
file.close()