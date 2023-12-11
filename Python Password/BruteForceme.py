import itertools
def BruteForce():

    password = "123456123"
    characs = input("Enter the Chracters / numbers used in the password ")
    length = int(input("Enter the password Length in integer form "))
    chracsList = list(itertools.chain.from_iterable(characs))
    #print(characs)
    #print(length)
    print(chracsList)

    changedList = list(itertools.product(chracsList,repeat=length))
#1234
    print(changedList)


    for x in changedList:
        word = ""
        for i in range (length):
            word = word + x[i]
        print("Trying this password " + word)
        if word == password:
            print("Success the password is "+ word)
            break
BruteForce()




