fileName = "myfile.txt"

f = None
try:
    # manually open the file
    f = open(fileName, "r")
    contents = f.read()
    print("The contents of the file:")
    print(contents)
except FileNotFoundError:
    print("The file", fileName, "does not exist")
finally:
    if f:
        f.close()
        print("File is closed")
