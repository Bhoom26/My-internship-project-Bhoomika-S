#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time

def display_intro():
    print("You are a brave knight on a quest to rescue the princess from the clutches of a fearsome dragon.")
    print("You find yourself standing at a crossroads. Which path will you choose?")
    print("1. The Forest")
    print("2. The Mountains")
    print("3. The Desert")

def forest_choice():
    print("You enter the dense forest. The trees loom large overhead, and it's getting darker.")
    time.sleep(1)
    print("Suddenly, you hear a rustling sound in the bushes.")
    choice = input("What will you do? (1. Investigate, 2. Keep moving): ")
    if choice == "1":
        print("You investigate and find a hidden treasure. You become rich!")
    else:
        print("You keep moving through the forest. The path leads you deeper into the woods.")
        time.sleep(1)
        print("Unfortunately, you lose your way and get attacked by wild animals. Game over!")

def mountain_choice():
    print("You begin your ascent up the steep and treacherous mountains.")
    time.sleep(1)
    print("After a long and exhausting climb, you reach a cave.")
    choice = input("Will you enter the cave? (1. Yes, 2. No): ")
    if choice == "1":
        print("You enter the cave and find a magic sword that will aid you in your quest!")
    else:
        print("You decide not to enter the cave and continue your journey.")
    
def desert_choice():
    print("You enter the scorching desert. The sun is unbearably hot.")
    time.sleep(1)
    print("You come across an oasis with a mysterious figure offering a drink.")
    choice = input("Do you accept the drink? (1. Yes, 2. No): ")
    if choice == "1":
        print("The drink was poisoned, and you fall unconscious. Game over!")
    else:
        print("You decline the drink and continue through the desert.")
        time.sleep(1)
        print("You find the dragon's lair in the distance.")

def main():
    display_intro()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        forest_choice()
    elif choice == "2":
        mountain_choice()
    elif choice == "3":
        desert_choice()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        main()

    print("You approach the dragon's lair. It's time for the final battle!")
    time.sleep(2)
    print("Congratulations! You have successfully rescued the princess and defeated the dragon!")

if __name__ == "__main__":
    main()


# In[ ]:




