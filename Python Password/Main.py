#main
import hashlib, os , bcrypt, itertools, sys
mode=""
type=""


typearg = sys.argv[2:]

for arg in typearg:
    if arg == "-b":
        mode = "bruteforce"
    elif arg == "-d":
        mode = "dictionary"
    elif arg == "-p":
        type = "plaintext"
    elif arg == "-m":
        type = "md5"
    elif arg == "-s":
        type = "Sha256"
    elif arg == "-bC":
        type = "bcrypt"
    
        



if type == "":
    type = "plaintext"
if mode == "":
    mode = "dictionary"
if (mode == "bruteforce") and (type== "Sha256" or type == "md5" or type == "bcrypt"):
    print("hashes cant be bruteforced only plaintext")
    type = "plaintext"




def Bcrypt():
    passwordHash = (sys.argv[1]).encode('utf-8')
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

def Sha256():

    passwordHash = sys.argv[1]
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

def BruteForce():

    password = sys.argv[1]
    characs = input("Enter the Chracters / numbers used in the password ")
    length = int(input("Enter the password Length in integer form "))
    chracsList = list(itertools.chain.from_iterable(characs))
    #print(characs)
    #print(length)
    #print(chracsList)

    changedList = list(itertools.product(chracsList,repeat=length))
#1234
    #print(changedList)


    for x in changedList:
        word = ""
        for i in range (length):
            word = word + x[i]
        print("Trying this password " + word)
        if word == password:
            print("Success the password is "+ word)
            break

def Md5():

    passwordHash = sys.argv[1]
    paths = "/home/adam/Documents/Gitshub2/New-Password-Cracker/paslist.txt"
    print(os.getcwd())
    count = 0
    with open(paths, "r") as pList:
    
        while count < 1000000:
            count += 1
 
            # Get next line from file
            line = pList.readline()
            lineR = line.rstrip()
            hashedLine = hashlib.md5(lineR.encode('utf-8')).hexdigest()
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

def Dictionary():

    path = "/home/adam/Documents/Gitshub2/New-Password-Cracker/paslist.txt"
    print(os.getcwd())
    password = sys.argv[1]
    #test = open(path,'r')
    #print(test.readline(2))
    #test.close()
    count = 0
    with open(path, "r") as pList:
    
        while count < 1000000:
            count += 1
 
            # Get next line from file
            line = pList.readline()
            lineR = line.rstrip()
            # if line is empty
            # end of file is reached
            print("Trying: " + lineR)
            if lineR == password:
                print("Sucess the password is " + lineR)
                break
            if count == 10001:
                break
        #print("Line{}: {}".format(count, line.strip()))
#test


if mode == "bruteforce":
    BruteForce()

if mode == "dictionary":
    if type =="plaintext":
        Dictionary()
    if type =="md5":
        Md5()
    if type == "Sha256":
        Sha256()
    if type == "bcrypt":
        Bcrypt()
