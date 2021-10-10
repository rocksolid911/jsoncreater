file1 = open(r"/home/rocksolid91/Documents/testjson.txt", "r+")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()
file1 = open(r"/home/rocksolid91/Documents/testjson.txt", "r")
print("Output of Read function is ")
print(file1.read())
print(file1.seek(0))

print("Output of Readline function is ")

print(file1.readline())

print(file1.seek(2))

print(file1.readline())

print("Output of Readline(9) function is ")
print(file1.readline(9))
