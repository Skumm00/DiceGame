#imports the random numbers
import random

def rolldice(num_dice):
    """
    Rolls for how many rolls you want
    And Also selecting how many dice you want to role per base!
    """
    for _ in range(num_dice):
        b = random.randint(1, 6)
        if b == 1:
            print("[-----]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[\u00a0  0 ]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[-----]", end=" ")
        elif b == 2:
            print("[-----]")
            print("[  0 ]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[\u00a0\u00a0  0 ]")
            print("[-----]", end=" ")
        elif b == 3:
            print("[-----]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[0 0 0]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[-----]", end=" ")
        elif b == 4:
            print("[-----]")
            print("[0 0]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[0 0]")
            print("[-----]", end=" ")
        elif b == 5:
            print("[-----]")
            print("[0 0]")
            print("[\u00a0  0 ]")
            print("[0 0]")
            print("[-----]", end=" ")
        else:
            print("[-----]")
            print("[0 0 0]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[0 0 0]")
            print("[-----]", end=" ")

    total_sum = 0  # Total Sum is 0 per default
    for _ in range(num_dice):
            b = random.randint(1, 6)
            total_sum += b  

    print(f"Complete sum of {num_dice} dice rolls is {total_sum}!")
def main():

    while True:
        try:
            num_dice = int(input("Enter how many dice you want to roll (0 to exit): "))
            if num_dice == 0:
                break
            rolldice(num_dice)
            print()  # After Displaying Results
        except ValueError:
            print("NOT VALID! ENTER A POSTIVE NUMBER OR CLICK 0 TO LEAVE!")

if __name__ == "__main__":
    main()
