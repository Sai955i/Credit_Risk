
file = open("open.txt", "r")    
text=file.read()   # read the file
file.close()  # close the file
print("File read successfully.")
print(text)