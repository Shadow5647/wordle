from colorama import init, Fore, Back, Style
import random
from word import WordList5,WordList4,WordList3

def tutorial() :
    print("---------------------------------------------------------------") 
    print("|        Just try to guess the word. After each guess,        |") 
    print("|          Press enter to check it. the color of the          |")
    print("|        word will change to show how close your guess        |")
    print("|                      was to the word.                       |")
    print("|   Red for the letter in the word and in the correct spot.   |")
    print("|   Yellow for the letter in the word but wrong spot.         |")
    print("|   black for the letter that not in the word in any spot     |")
    print("|                          Good Luck                          |")
    print("---------------------------------------------------------------")

print("\n-----------------------------------------------")
print("-------------  Welcome to Wordle  -------------")
print("-----------------------------------------------")

while True :
    
    #Menu
    print("\n ----- Please select ----- \n")
    print("1.play the game")
    print("2.tutorial for game")
    print("3.exit the game")
    
    #SelectMenu
    PorE = input("\nPlease type 1 2 or 3 : ")
    print(" ")
    if int(PorE) == 1 :
        print("\n------- Select the number of characters -------")
        Num_Word = input("\nPlease type 3 4 or 5 : ")
        
        if int(Num_Word) == 4 :
            #Start Play
            inner_loop = 0
            #Diffculty
            print("\n-------------- Select difficulty --------------")
            print("[1 is easy]")
            print("[2 is normal]")
            print("[3 is hard]")
            print("[4 is impossible]")
            diff = 7-int(input("\nPlease type 1-4 : "))
            print(" ")
            #Random Word
            word = random.choice(WordList4)
            while inner_loop < diff:

                attempt = input("Enter 4 letter word : ")

                output = ""
                for i in range(word.__len__()):
                    if attempt[i] == word[i]:
                        output = output + Back.RED + attempt[i] + Back.RESET
                    elif attempt[i] in word:
                        output = output + Back.YELLOW + attempt[i] + Back.RESET
                    else:
                        output = output + attempt[i] + Back.RESET
                print("-------------------- "+ output +" ---------------------")
                if word == attempt:
                
                    print("-----------------------------------------------")
                    print("------------------  You Win  ------------------")
                    print("-----------------------------------------------")
                    # Reset game
                    inner_loop = inner_loop + diff 
            
                inner_loop = inner_loop + 1
            print("\n-------------- Correct Answer Is --------------")
            print("                      "+str(word)+"            ")
            print("-----------------------------------------------")
        elif int(Num_Word) == 5 :
            #Start Play
            inner_loop = 0
            #Diffculty
            print("\n-------------- Select difficulty --------------")
            print("[1 is easy]")
            print("[2 is normal]")
            print("[3 is hard]")
            print("[4 is impossible]")
            diff = 8-int(input("\nPlease type 1-4 : "))
            print(" ")
            #Random Word
            word = random.choice(WordList5)
            while inner_loop < diff:

                attempt = input("Enter 5 letter word : ")

                output = ""
                for i in range(word.__len__()):
                    if attempt[i] == word[i]:
                        output = output + Back.RED + attempt[i] + Back.RESET
                    elif attempt[i] in word:
                        output = output + Back.YELLOW + attempt[i] + Back.RESET
                    else:
                        output = output + attempt[i] + Back.RESET
                print("------------------- "+ output +" ---------------------")
                if word == attempt:
                
                    print("-----------------------------------------------")
                    print("------------------  You Win  ------------------")
                    print("-----------------------------------------------")
                    # Reset game
                    inner_loop = inner_loop + diff 
            
                inner_loop = inner_loop + 1
            print("                     "+str(word)+"            ")
            print("-----------------------------------------------")
        elif int(Num_Word) == 3 :
            #Start Play
            inner_loop = 0
            #Diffculty
            print("\n-------------- Select difficulty --------------")
            print("[1 is easy]")
            print("[2 is normal]")
            print("[3 is hard]")
            print("[4 is impossible]")
            diff = 8-int(input("\nPlease type 1-4 : "))
            print(" ")
            #Random Word
            word = random.choice(WordList3)
            while inner_loop < diff:

                attempt = input("Enter 3 letter word : ")

                output = ""
                for i in range(word.__len__()):
                    if attempt[i] == word[i]:
                        output = output + Back.RED + attempt[i] + Back.RESET
                    elif attempt[i] in word:
                        output = output + Back.YELLOW + attempt[i] + Back.RESET
                    else:
                        output = output + attempt[i] + Back.RESET
                print("--------------------- "+ output +" ---------------------")
                if word == attempt:
                
                    print("-----------------------------------------------")
                    print("------------------  You Win  ------------------")
                    print("-----------------------------------------------")
                    # Reset game
                    inner_loop = inner_loop + diff 
            
                inner_loop = inner_loop + 1
            print("\n-------------- Correct Answer Is --------------")
            print("                      "+str(word)+"                ")
            print("-----------------------------------------------")   
    elif int(PorE) == 2 :
        tutorial()
    elif int(PorE) == 3 :
        break
    else :
        print("  ")
        print(">>>> Just 1 or 2 Please type again <<<<")
        print("  ")

print(" ")
print("-----------------  THANK YOU  -----------------")
print(" ")
