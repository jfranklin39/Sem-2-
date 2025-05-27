import random

# Set initial credits
credits = 50

while True:
    mylist = [3, 7, 100]
    slot1 = random.choice(mylist)
    slot2 = random.choice(mylist)
    slot3 = random.choice(mylist)

    print(f"Welcome to the Slot Machine! You have {credits} credits.")
    print("Please select an option: ")
    print("1. Spin \n2. Quit ")

    activity = int(input("Activity: "))

    if activity == 1:
        # Check if the player has enough credits to spin
        if credits > 0:
            # Deduct 1 credit for each spin
            credits -= 1
            print("Your Numbers are: ")
            x = (slot1, slot2, slot3)
            y = (7, 7, 7)
            print(x)

            # Check if the player wins
            if x == y:
                print("You have won! You receive 10 credits!")
                credits += 10  # Award 10 credits for a win
            else:
                print("You have not won.")
        else:
            print("You don't have enough credits to spin.")

    elif activity == 2:
        print(f"Thanks for playing! You ended with {credits} credits. Goodbye.")
        break
    else:
        print("Invalid choice. Please choose 1 to spin or 2 to quit.")

