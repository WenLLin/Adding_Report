
items = []

def adding_report(word):
    total = 0
    while True:
        if word.isdigit():
            total += int(word)
            items.append(word)
        elif word == "Quit" or word == "q" or word == "Q"or word == "quit":
            break
        else:
            print(word,"is invalid input")
        word = input("Enter an integer or \"Q\": ") 
        
    if word == "q" or word == "Q":
        print("")
        print(*items, sep = "\n")
        return print("\nTotal\n"+ str(total))
    elif word != "Quit" or word != "quit":
        return print("\nTotal\n"+ str(total))
        
print("Input an integer to add to the total or \"Q\" to quit")
word = input("Enter an integer or \"Q\": ")   
adding_report(word)