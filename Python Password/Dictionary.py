import os


def Dictionary():

    path = "/home/adam/Documents/Gitshub2/New-Password-Cracker/paslist.txt"
    print(os.getcwd())
    password = "someday"
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
Dictionary()