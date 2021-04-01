#!/usr/bin/env python3

''' a guessing game '''

def getAns():
    f = open("mygame.data", "r")
    return f.readline()

def main():
    
    print("A VERY COOL GAME")
    
    ans = getAns().strip()

    #read a single char 
    x = input("Think of a single charater:")

    #check answer aginst game data file
    if x.strip().lower() == ans.lower():
        print("Congrats! You are the grand winnder!!!")
    else:
        print("You were close, try again !!!")

    
if __name__ == "__main__":
    main()
