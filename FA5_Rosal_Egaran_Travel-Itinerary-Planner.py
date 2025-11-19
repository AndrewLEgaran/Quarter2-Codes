def choicemaker():
    if destchange == 1:
        newdest1 = input("Please enter the new destination for Destination 1: ")
        Destinations[0] = newdest1.capitalize()
    elif destchange == 2:
        newdest2 = input("Please enter the new destination for Destination 2: ")
        Destinations[1] = newdest2.capitalize()
    elif destchange == 3:
        newdest3 = input("Please enter the new destination for Destination 3: ")
        Destinations[2] = newdest3.capitalize()
    elif destchange == 4:
        newdest4 = input("Please enter the new destination for Destination 4: ")
        Destinations[3] = newdest4.capitalize()
    elif destchange == 5:
        newdest5 = input("Please enter the new destination for Destination 5: ")
        Destinations[4] = newdest5.capitalize()
    else:
        print("You have Entered a variable outside of the question's range: TypeError")
        print("Please try again.")

def destinechanger():
    if choice2 == "Y":
        choicemaker()
    elif choice2 == "N":
        print("Final Itinerary Plan: ")
        print("1. ", Destinations[0].capitalize())
        print("2. ", Destinations[1].capitalize())
        print("3. ", Destinations[2].capitalize())
        print("4. ", Destinations[3].capitalize())
        print("5. ", Destinations[4].capitalize())
    else:
        print("You have Entered a variable outside of the question's range: TypeError")
        print("Please try again.")

Destinations = []
print("Please enter the 5 destinations you are planning to visit:")
Dest1 = input("Destination 1: ")
Destinations.append(Dest1)
Dest2 = input("Destination 2: ")  
Destinations.append(Dest2)
Dest3 = input("Destination 3: ")
Destinations.append(Dest3)
Dest4 = input("Destination 4: ")
Destinations.append(Dest4)
Dest5 = input("Destination 5: ")
Destinations.append(Dest5)

print("Original Travel Itinerary: ")
print("1. ", Destinations[0].capitalize())
print("2. ", Destinations[1].capitalize())
print("3. ", Destinations[2].capitalize())
print("4. ", Destinations[3].capitalize())
print("5. ", Destinations[4].capitalize())

print("Would you like to change any of the destination?")
choice = input("Y/N: ")
if choice == "Y":
    print("Please input the number of the destination you would like to change: ")
    destchange = int(input("Destination Number (1-5): "))
    choicemaker()
elif choice == "N":
    print("Final Itinerary Plan: ")
    print("1. ", Destinations[0].capitalize())
    print("2. ", Destinations[1].capitalize())
    print("3. ", Destinations[2].capitalize())
    print("4. ", Destinations[3].capitalize())
    print("5. ", Destinations[4].capitalize())
else:
    print("You have Entered a variable outside of the question's range: TypeError")
    print("Please try again.")


print("Would you like to change another destination?: ")
choice2 = input("Y/N: ")

destinechanger()
