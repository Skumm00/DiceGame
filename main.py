#imports random numbers
import random

def rolldice():
    b = random.randint(1, 6)
    #custom numbers
    if b == 1:
        print("[-----]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[\u00A0  0 ]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[-----]")
    elif b == 2:
        print("[-----]")
        print("[  0 ]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[\u00A0\u00A0  0 ]")
        print("[-----]")
    elif b == 3:
        print("[-----]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[0 0 0]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[-----]")
    elif b == 4:
        print("[-----]")
        print("[0 0]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[0 0]")
        print("[-----]")
    elif b == 5:
        print("[-----]")
        print("[0 0]")
        print("[\u00A0  0 ]")
        print("[0 0]")
        print("[-----]")
    else:
        print("[-----]")
        print("[0 0 0]")
        print("[\u00A0\u00A0\u00A0\u00A0 ]")
        print("[0 0 0]")
        print("[-----]")

#asks if user wants to roll again
def main():
    while True:
        rolldice()
        x = input("Press 'y' to roll again or 'n' to exit: ")
        if x.lower() != 'y':
            break
          
#calls the entire function using classes and functions
if __name__ == "__main__":
    main()
