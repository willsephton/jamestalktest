var1 = 1
var2 = 2


def ifstatementTest():
    if var1 == var2:
        print("Var1 equals Var2")
    elif var1 != var2:
        print("Var1 does not equal Var2")
    else:
        print("Something has gone wrong")


    
def forLoopTest():
    for x in range(0,4):
        print("This should print 4 times.")
        


def whileLoopTest():
    counter = 1
    while counter != 7:
        print("This should print 6 times")
        counter = counter+1
        



def mainMenu():
    print("-----Main Menu-----")
    print("A) ifStatementTest() \nB) forLoopTest() \nC) whileLoopTest()")
    choice = input("Which option would you like to do: ").upper()
    if choice == "A":
        ifstatementTest()
    elif choice == "B":
        forLoopTest()
    elif choice == "C":
        whileLoopTest()
    else:
        print("Incorrect option")
    
mainMenu()