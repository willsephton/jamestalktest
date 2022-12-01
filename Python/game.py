import random

def mainMenu():
    choice = ""
    while choice != "C":
        print("-----Main Menu-----")
        print("A) Rock Paper Scissors \nB) Tic Tac Toe \nC) Exit")
        choice = input("Which option would you like to do: ").upper()
        if choice == "A":
            rockpaperscissors()
        elif choice == "B":
            tictactoe()
        elif choice == "C":
            print("Exiting....")
        else:
            print("Incorrect option")


def rockpaperscissors():
    print("-----Rock, Paper, Scissors-----")
    userChoice = input("Would you like to pick Rock, Paper, Or Scissors: ").upper()
    compChoice = random.randint(1,3)
    if compChoice == 1:
        compChoice = "ROCK"
    elif compChoice == 2:
        compChoice = "PAPER"
    elif compChoice == 3:
        compChoice = "SCISSORS"
    else:
        print("Something has gone wrong.")
    
    print("The computer chose",compChoice)
        
    if compChoice == userChoice:
        print("That game was a draw!")
    elif (compChoice == "ROCK" and userChoice == "PAPER") or (compChoice == "PAPER" and userChoice == "SCISSORS") or (compChoice == "SCISSORS" and userChoice == "ROCK"):
        print("You won. You did great!")
    elif (compChoice == "PAPER" and userChoice == "ROCK") or (compChoice == "SCISSORS" and userChoice == "PAPER") or (compChoice == "ROCK" and userChoice == "SCISSORS"):
        print("The computer won. Maybe next time!")
        
    choice2 = input("Would you like to play again (Yes Or No):").upper()
    if choice2 == "YES":
        rockpaperscissors()
    else:
        print("Returning to main menu.....")


def tictactoe():
    while True: #Taken if User Want to play game again
        filed=1 #Counter how many values are filled in board
        board=[" "]*10 #Setting all values to blank in board
        player="" #Will store which player is playing
        hasWon=False #For Checking if any player won or not

        def printTable():
                for i in range(1,10):
                        print(board[i],end=" ")
                        if(i%3==0 and i!=9):
                                print("\n","-"*8)
                        elif i!=9:
                                print("|",end=" ")
                                
        print("-----Tic Tac Toe-----\n")
        printTable()

        while True:
                XorO=input("\n\nEnter O or X ") #Taking 1st user value if its O or X
                if XorO.lower() == "o" or XorO == "0": #Check if it is O 
                        player = "O"  # set player to O
                        break
                elif XorO.lower() == "x": #Check if it is X
                        player = "X" # set player to X
                        break
                else: #When neither O nor X entered
                    print("You are not entering O or X, try again")

    #Function for win Situation Return True if player Win else False, Player is taken as parameter because by default blank is assigned to all
                    #on equating 2 blank it will return true even if that position are empty

        def test(player):
                if board[1]==board[2] and board[2]==board[3] and board[3]==player: #123 1st row
                        return True
                elif board[4]==board[5] and board[5]==board[6] and board[6]==player: #456 2nd row 
                        return True
                elif board[7]==board[8] and board[8]==board[9] and board[9]==player: #789 rd row
                        return True
                elif board[1]==board[5] and board[5]==board[9] and board[9]==player: #1st column
                        return True
                elif board[3]==board[5] and board[5]==board[7] and board[7]==player: #2nd column
                        return True
                elif board[1]==board[4] and board[4]==board[7] and board[7]==player: #3rd column
                        return True
                elif board[2]==board[5] and board[5]==board[8] and board[8]==player: #Diagonal 1
                        return True
                elif board[3]==board[6] and board[6]==board[9] and board[9]==player: #Diagonal 2
                        return True      
                else:
                        return False

        while filled != 10: #Will Run until whole board is filled  
                position = input("\nEnter position: ") #Taken Position
                while position not in ['1','2','3','4','5','6','7','8','9']: #if invalid position entered
                        print("You are not entering a correct position\n")
                        position = input('Enter position ') #taken position again
                if(board[int(position)] == " "): #check position is empty 
                        board[int(position)] = player  #fill board with O/X at entered position
                        filled = filled + 1 #Updating count of number of positions filled in board
                        printTable() #Print Table
                        if filled > 4: #Minimum 5 values is needed to be filled in order to Win (In Total of X and O )
                            if test(player): #If any player had won before filling the entire board it will break and Val becomes true, initially Declared false at top. 
                                hasWon=True
                                break
                        if player=="X": #Player will Swap after every turn
                                player="O"
                        else:
                                player="X"
                else:
                    print("Position is already occupied") #if position is already filled again position is asked , end of while loop
        if hasWon==True: 
                print("\n\n",player," Wins the game.")
        else:
                print("\nDraw")
        playAgain = input("\nDo you want to play again (Yes or No): \n") #Ask user if he want to play again
        if playAgain.lower() != "yes": #Check if is any other value than Y or y then break, program will be terminated, if Y is enteree control will go to 1st line while loop
            print("Exiting....")
            break
mainMenu()
