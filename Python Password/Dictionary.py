import os



path = "/home/adam/Documents/Github/Password-Cracker-real/password/paslist.txt"
print(os.getcwd())
password = "someday"
#test = open(path,'r')
#print(test.readline(2))
#test.close()
count = 0
with open(path, "r") as pList:
    
    while count < 5:
        count += 1
 
        # Get next line from file
        line = pList.readline()
 
        # if line is empty
        # end of file is reached
        if str(line) == "123456":
            break
        print("Line{}: {}".format(count, line.strip()))
#test