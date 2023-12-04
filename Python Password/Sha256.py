#hash attack
import os 
import hashlib
passwordHash = input("Enter the hash you want to convert ")
paths = "/home/adam/Documents/Gitshub2/New-Password-Cracker/paslist.txt"
print(os.getcwd())
count = 0
with open(paths, "r") as pList:
    
    while count < 1000000:
        count += 1
 
        # Get next line from file
        line = pList.readline()
        lineR = line.rstrip()
        hashedLine = hashlib.sha256(lineR.encode('utf-8')).hexdigest()
        # if line is empty
        # end of file is reached
        print("Trying: " + hashedLine)
        if hashedLine == passwordHash:
            print("Sucess the hash " + passwordHash + " equals " + lineR)
            break
        if count == 10001:
            print("we could not decode that hash")
            break
        #print("Line{}: {}".format(count, line.strip()))
#test
