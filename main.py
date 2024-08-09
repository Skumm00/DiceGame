#imports the random numbers
import random

#superdice function
def superdice(num_dice):
    """
    More Advanced features for the dice!
    """
    rolls = []
    for _ in range(num_dice):
        d = random.randint(1, 8)
        rolls.append(d)
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

    total = sum(rolls)
    print(f"Complete sum of {num_dice} dice rolls is {total}!")

    # Gets the avg value of each roll
    average = total / num_dice
    print(f"Average value per roll: {average:.2f}")

    # = Show the highest/lowest roll
    highest_roll = max(rolls)
    lowest_roll = min(rolls)
    print(f"Highest roll: {highest_roll}")
    print(f"Lowest roll: {lowest_roll}")

    #Puts a cool message
    if total == num_dice:
        print("Wow, you rolled all ones! Lucky!")
    elif total == 7 * num_dice:
        print("Lucky number 7!")


def rolldice(num_dice):
    """
    Rolls for how many rolls you want
    And Also selecting how many dice you want to role per base!
    """
    rolls = []
    for _ in range(num_dice):
        b = random.randint(1, 6)
        rolls.append(b)
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

    total_sum = sum(rolls)
    print(f"Complete sum of {num_dice} dice rolls is {total_sum}!")
    
    # Gets the avg value of each roll
    average = total_sum / num_dice
    print(f"Average value per roll: {average:.2f}")

    # = Show the highest/lowest roll
    highest_roll = max(rolls)
    lowest_roll = min(rolls)
    print(f"Highest roll: {highest_roll}")
    print(f"Lowest roll: {lowest_roll}")

    #Puts a cool message
    if total_sum == num_dice:
        print("Wow, you rolled all ones! Lucky!")
    elif total_sum == 7 * num_dice:
        print("Lucky number 7!")
def main():
    #while true display
    while True:
        try:
            
            #add more to the selector
            selecter = input("Do You want the Normal or Super dice to play with? n/s")
            #add the selecter for the normal dice game
            if selecter == "n":
                #The Logic
                num_dice = int(input("Enter how many dice you want to roll (0 to exit): "))
                #break if num_dice = 0
                if num_dice == 0:
                    break
                #displaying the results
                rolldice(num_dice)
                print()  
            #if user chooses superdice in the selector
            elif selecter == "s":
                #logic for the superdice game
                super_dice = int(input("Enter how many dice you need: "))
                #add if super_dice is 0 then break
                if super_dice == 0:
                    break
                #displays the output
                superdice(super_dice)
                print()#prints everything

        #the value error if user doesnt put a correct thing       
        except ValueError:
            print("NOT VALID! ENTER A POSTIVE NUMBER OR CLICK 0 TO LEAVE!")

if __name__ == "__main__":
    main()
