#Bcrypt
import bcrypt
import os 
passwordHash = (input("Enter the hash you want to convert ")).encode('utf-8')
paths = "/home/adam/Documents/Gitshub2/New-Password-Cracker/paslist.txt"
print(os.getcwd())
count = 0
with open(paths, "r") as pList:
    
    while count < 1000000:
        count += 1
 
        # Get next line from file
        line = pList.readline()
        lineR = line.rstrip()
        bytes = lineR.encode('utf-8') 
  
        # generating the salt 
        #salt = bcrypt.gensalt() 
  
        # Hashing the password 
        #hashedLine = bcrypt.hashpw(bytes, salt) 
        
        # if line is empty
        # end of file is reached
        print("Trying: " + str(lineR))
        if bcrypt.checkpw(bytes, passwordHash ):
            print("Sucess the hash " + str(passwordHash) + " equals " + lineR)
            break
        if count == 10001:
            print("we could not decode that hash")
            break
        #print("Line{}: {}".format(count, line.strip()))
#test
