from sys import exit
import random

kurallariOku = input("SOS oyununa hos geldiniz!\n------------------------- \nKurallari okumak icin r tusuna basiniz.")

if(kurallariOku == 'r'):

    print("**Oyun Kuralları: Sos**\n")
    print("1. **Oyun Alanı:**\n   - Oyun 3x3'lük bir kare alan üzerinde oynanır.\n")
    print("2. **Sıralama:**\n   - Oyuncular sırayla hamle yaparlar.\n")
    print("3. **Amac:**\n   - Amacınız, üç S ya da üç O'yu yatay, dikey veya çapraz bir çizgi oluşturarak oyun alanına yerleştirmektir.\n")
    print("4. **Hamle Yapma:**\n   - Oyuncular sırası geldiğinde, boş bir hücreye S (oyuncu) veya O (bilgisayar) koyarlar.\n")
    print("5. **Çizme:**\n   - Oyuncular, üç S veya üç O'yu bağlamayı başarırlarsa, o oyuncu oyunu kazanır.\n")
    print("6. **Beraberlik:**\n   - Eğer oyun alanı tamamen dolduğunda ve kimse üçlü bir dizilim yapamazsa, oyun berabere biter.\n")
    print("7. **Yeni Oyun:**\n   - Oyun sona erdiğinde, isterseniz yeni bir oyun başlatmak için tekrar başlayabilirsiniz.\n")
    print("8. **Kazanan:**\n   - Üçlü bir dizilimi ilk tamamlayan oyuncu kazanır.\n")


possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3],[4,5,6],[7,8,9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end = "")
        for y in range(cols):
            print("", gameBoard[x][y], end = " |")
    print("\n+---+---+---+")


def modifyArray(num, turn):
    num -= 1
    if(num == 0):
        gameBoard[0][0] = turn
    elif(num == 1):
        gameBoard[0][1] = turn
    elif(num == 2):
        gameBoard[0][2] =turn
    elif(num == 3):
        gameBoard[1][0] = turn
    elif(num == 4):
        gameBoard[1][1] = turn
    elif(num == 5):
        gameBoard[1][2] = turn
    elif(num == 6):
        gameBoard[2][0] = turn
    elif(num == 7):
        gameBoard[2][1] = turn
    elif(num == 8):
        gameBoard[2][2] = turn

def checkForWinner(gameBoard):
    ##X axis
    if(gameBoard[0][0] == 'S' and gameBoard[0][1] == 'S' and gameBoard[0][2] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[1][0] == 'S' and gameBoard[1][1] == 'S' and gameBoard[1][2] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[2][0] == 'S' and gameBoard[2][1] == 'S' and gameBoard[2][2] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"



    ##Y axis
    elif(gameBoard[0][0] == 'S' and gameBoard[1][0] == 'S' and gameBoard[2][0] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][1] == 'S' and gameBoard[1][1] == 'S' and gameBoard[2][1] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][2] == 'S' and gameBoard[1][2] == 'S' and gameBoard[2][2] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"


    ##Cross wins
    elif(gameBoard[0][0] == 'S' and gameBoard[1][1] == 'S' and gameBoard[2][2] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
        print("O has won!")
        return "O"
    elif(gameBoard[0][2] == 'S' and gameBoard[1][1] == 'S' and gameBoard[2][0] == 'S'):
        print("S has won!")
        return "S"
    elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
        print("O has won!")
        return "O"




leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
    ## It's the player's turn
    if(turnCounter % 2 == 1):
        printGameBoard()
        numberPicked = int(input("\nChoose a number 1 through 9: "))
        #checking if the input is valid
        if(numberPicked >= 0 or numberPicked <= 9):
           modifyArray(numberPicked, 'S')
           possibleNumbers.remove(numberPicked)
        else:
            print("invalid input. Please try again")
        turnCounter += 1
    ##It's the computer's turn
    else:
        while(True):
            cpuChoice = random.choice(possibleNumbers)
            print("\nCpu choice: ", cpuChoice)
            if(cpuChoice in possibleNumbers):
                modifyArray(cpuChoice, 'O')
                possibleNumbers.remove(cpuChoice)
                turnCounter += 1
                break


        
exit()
