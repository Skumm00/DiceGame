#imports the random numbers
import random

#superdice function
def superdice(num_dice):
    """
    More Advanced features for the dice!
    """
    for _ in range(num_dice):
        d = random.randint(1, 8)
        if d == 1:
            print("[-----]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[\u00a0  0 ]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[-----]", end=" ")
        elif d == 2:
            print("[-----]")
            print("[  0 ]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[\u00a0\u00a0  0 ]")
            print("[-----]", end=" ")
        elif d == 3:
            print("[-----]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[0 0 0]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[-----]", end=" ")
        elif d == 4:
            print("[-----]")
            print("[0 0]")
            print("[\u00a0\u00a0\u00a0\u00a0 ]")
            print("[0 0]")
            print("[-----]", end=" ")
        elif d == 5:
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

    total = 1  # Total should be 1!
    for _ in range(num_dice):
        b = random.randint(1, 6)
        total += b

    print(f"Complete sum of {num_dice} dice rolls is {total}!")


    # Gets the avg value of each roll
    average = total / num_dice
    print(f"Average value per roll: {average:.2f}")

    # = Show the highest/lowest roll
    highest_roll = max(b for _ in range(num_dice))
    lowest_roll = min(b for _ in range(num_dice))
    print(f"Highest roll: {highest_roll}")
    print(f"Lowest roll: {lowest_roll}")

    #Puts a cool message
    if total == num_dice:
        print("Wow, you rolled all ones! Lucky!")
    elif total == 7 * num_dice:
        print("Lucky number 7!")

#rolldice function
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
    #while true display
    while True:
        try:
            selecter = input("Do You want the Normal or Super dice to play with? n/s")
            if selecter == "n":
                num_dice = int(input("Enter how many dice you want to roll (0 to exit): "))
                if num_dice == 0:
                    break
                rolldice(num_dice)
                print()  # After Displaying Results
            elif selecter == "s":
                super_dice = int(input("Enter how many dice you need: "))
                if super_dice == 0:
                    break
                superdice(super_dice)
                print()#prints everything
        except ValueError:
            print("NOT VALID! ENTER A POSTIVE NUMBER OR CLICK 0 TO LEAVE!")

if __name__ == "__main__":
    main()
