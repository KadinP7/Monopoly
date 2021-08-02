import random
import time
money = [0, 1500, 1500, 1500]
#Starting money for each player (1-4), the random import is to simulate probability and the time import is to simulate passing of time when round ends

deeds1 = []
deeds2 = []
deeds3 = []
deeds4 = []
#Deeds that each player would start with


mortgage1 = []
mortgage2 = []
mortgage3 = []
mortgage4 = []
space = [0,1,1,1,1]
#Mortgages and spaces on board

rail1 = set()
rail2 = set()
rail3 = set()
rail4 = set()
#Railways
util1 = set()
util2 = set()
util3 = set()
util4 = set()
#Utilities
j = [0,0,0,0,0]
jailfree = [0,0,0,0,0]
check = [0,0,0,0,0,0,0,0,0]
#Used in function to check whether or not player is in jail and therefore restricted
def roll(x):
    y = 0
    for i in range(x):
        z = random.radiant(1,6)
        y == z
    return y
#Simulate dice roll 1-6
def isnumeric(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
#Checks if input is number
def price(x):
    y = x + 30
    z = y/2
    return int(z)
#Used to calculate prices


#Defines objects for each of the properties, prices,
properties = {1: "Go", 2: "Mediterranean Avenue", 3: "Community Chest", 4: "Baltic Avenue", 5: "Income Tax", 6: "Jail", 7: "Oriental Avenue", 8: "Chance", 9: "Vermont Avenue", 10: "Conneticut Avenue", 11: "Jail", 12: "St. Charles Place", 13: "Electric Company", 14: "States Avenue", 15: "Virginia Avenue", 16: "Pennsylvania Railroad", 17: "St. James Place", 18: "Community Chest", 19: "Tennessee Avenue", 20: "New York Avenue", 21: "Free Parking", 22: "Kentucky Avenue", 23: "Chance", 24: "Indiana Avenue", 25: "Illinois Avenue", 26: "880 Railroad", 27: "Atlantic Avenue", 28: "Ventor Avenue", 29: "Water Works", 30: "Marvin Gardens", 31: "Go to Jail", 32: "Pacific Avenue", 33: "North Carolina Avenue", 34: "Community Chest", 35: "Pennsylvania Avenue", 36: "Short Line", 37: "Chance", 38: "Park Place", 39: "Luxury Tax", 40: "Boardwalk"}

prices = ["A", 60, "B", 60, "C", "D", 100, "E", 120, "F", 140, "G", 140, 160, "H", 180, "I", 180, 200, 0, 220, "J", 220, 240, "K", 260, 260, "L", 280, "M", 300, 300, "N", 320, "O", "P", 350, "Q", 400]


deeds = ["Mediterranean Avenue", "Baltic Avenue", "Arctic Avenue", "Masachussetts Avenue", "Oriental Avenue", "Vermont Avenue", "Conneticut Avenue", "Maryland Avenue", "St. Charles Place", "States Avenue", "Virginia Avenue",  "St. James Place", "Tennessee Avenue","New York Avenue",  "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue", "Michigan Avenue",  "Atlantic Avenue", "Ventor Avenue", "Marvin Gardens", "California Avenue",  "Pacific Avenue", "South Carolina Avenue", "North Carolina Avenue", "Pennsylvania Avenue", "Florida Avenue", "Park Place", "Boardwalk", "Reading Railroad", "Pennsylvania Railroad", "B&O Railroad", "Short Line", "Electric Company", "Water Works"]


buyables = ["Mediterranean Avenue", "Baltic Avenue", "Arctic Avenue", "Masachussetts Avenue", "Oriental Avenue", "Vermont Avenue", "Conneticut Avenue", "Maryland Avenue", "St. Charles Place", "States Avenue", "Virginia Avenue",  "St. James Place", "Tennessee Avenue","New York Avenue",  "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue",  "Michigan Avenue", "Atlantic Avenue", "Ventor Avenue", "Marvin Gardens", "California Avenue",  "Pacific Avenue", "South Carolina Avenue",  "North Carolina Avenue", "Pennsylvania Avenue", "Florida Avenue", "Park Place", "Boardwalk"]

colors = {"Mediterranean Avenue" : 1, "Baltic Avenue" : 1, "Oriental Avenue" : 2, "Vermont Avenue" : 2, "Conneticut Avenue" : 2, "St. Charles Place": 3, "States Avenue": 3, "Virginia Avenue": 3, "St. James Place" : 4, "Maryland Avenue" : 5, "St. Charles Place": 6 ,"States Avenue": 6, "Virginia Avenue": 6 ,  "St. James Place": 4, "Tennessee Avenue": 4 ,"New York Avenue": 4,  "Kentucky Avenue": 5 , "Indiana Avenue": 5, "Illinois Avenue": 5,  "Michigan Avenue": 5 , "Atlantic Avenue": 5, "Ventor Avenue": 5, "Marvin Gardens": 5, "California Avenue": 5,  "Pacific Avenue": 6, "South Carolina Avenue": 6,  "North Carolina Avenue": 6, "Pennsylvania Avenue": 6, "Florida Avenue": 7, "Park Place": 8, "Boardwalk": 8 }

chance = {1: "Advance to Go. (Collect $200))", 2: "Advantace to St. Charles Place. If you pass Go, Collect $200.", 3: "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned throw dice and pay the owner.", 4: "Advance token to the nearest Railroad. If Railroad is unowned, you may but it from the Bank. If it is owned, you must pay the owner. ", 5: "Bank pays you dividend of $50.", 6: "Get out of Jail Free. This card may be kept until needed or exchanged.", 6: "Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.", 7 : "Grand Opera Night Collect $50 from every player for opening night seats. ", 8: "Holiday Fund matures. Collect $100.", 9: "Income tax refund. Collect $20. ", 10: "It is your birthday. Collect $10 from every player ", 11: "Life insurance matures - collect $100", 13: "Hospital Fees. Pay $50 ", 14: " School Fees. Pay $50 ", 15: "Receive $25 consultancy fee . ", 16: "You have won second prize in a beauty contest. Collect $10.", 17: "You inherit $100."} 

community = {1: "Advance to Go. ", 2: "Bank error in your favor. Collect $200. ", 3: "Doctor's fees. Pay $50. ", 4: "From sale of stock you get $50.", 5: "Get out of Jail Free. This card may be kept until needed or exchanged. ", 6: "Go to Jail. Go directly to jail.Do not collect $200. ", 7: "Grand Opera Night Collect $50 from every player for opening night seats.", 8: "Holiday Fund matures. Collect $100.", 9: "iNCOME TAX REFUND. Collect $20.", 10: "It is your birthday. Collect $10 from every player.", 11: "Life insurance matures - Collect $100. ", 13: "Hospital Fees. Pay $50.", 14: "School Fees. Pay $50.", 15: "Receive $25 consultancy fee.", 16: "You have won second prize in a beauty contest. Collect $10.", 17: "You inherit $100."}

introText = input("Welcome toMonopoly! \n\n In this game you, will be playing the text-adventure version of the board game Monopoly.")

inputPlayers = int(input("How many players are there (2-4: "))

if inputPlayers > 4:
    inputPlayers = 4
elif inputPlayers < 2:
    inputPlayers = 2
#Caps players at 4 and minimizes players at 2

while True:
    check1 = [0,1,0,0,0,0,0,0,1]
    check2 = [0,1,0,0,0,0,0,0,1]
    check3 = [0,1,0,0,0,0,0,0,1]
    check4 = [0,1,0,0,0,0,0,0,1]
    for i in range(1,inputPlayers+1):
        prop = 1
        nobuy = 0
        print("\nPlayer " + str(i) + ": ")

        if i == 1:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]) + ", you have " + str(len(deeds1)) + " deeds, and you are on " + printer + ". ")
        elif i == 2:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]) + ", you have " + str(len(deeds2)) + " deeds, and you are on " + printer + ". ")
        elif i == 3:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]) + ", you have " + str(len(deeds3)) + " deeds, and you are on " + printer + ". ")
        elif i == 4:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]) + ", you have " + str(len(deeds4)) + " deeds, and you are on " + printer + ". ")

#Tells players #1-4 their money amount, deed amount, and spatial positions
        if j[i] == 0:
            inputBlank = input("Press enter to roll: ")
            throw = roll(2)
            print("You rolled a " + str(throw))
            space[i] += throw
        printer = properties[space[i]]

        print("You are now on "+ printer)
#Simulates change in spatial position after dice roll


        

        if i == 1:
            determine = prices[space[i] - 1]
        elif i == 2:
            determine = prices[space[i] - 1]
        elif i == 3:
            determine = prices[space[i] - 1]
        elif i == 4:
            determine = prices[space[i] - 1]
#Determines price of property landed on



#The following functions dictate the effect of each of the chance cards:
        if determine == "A":
            number = random.radiant(1,15)
            card = chance[number]
            time.sleep(1)
            print("You have drawn a card that says: ")
            time.sleep(1)
            print(card)
            if number == 1:
                space[i] == 41
            elif number == 2:
             if space[i] > 40:
                space[i] -= 40
                print("You passed Go and collect $200")
                money[i] += 200
                space[i] += 1
                print("You are now on " + properties[space[i]])
                printer = properties[space[i]]
                determine = prices[space[i] - 1]
        elif number == 4:
                while prices[space[i]] != "R":
                    space[i] += 1
                    if space[i] > 40:
                        space[i] -= 40
                        print("You passed Go and collect $200")
                        money[i] += 200
                        space[i] += 1
                        print("Tiy are now on " + properties[space[i]])
                        printer = properties[space[i]]
                        determine = prices[space[i]-1]
        elif number == 5:
                money[i] += 50
        elif number == 6:
                jailfree[i] == 7
        elif number == 8:
            money[i] -= 15
        elif number == 9:
                while properties[space[i]]!= "Reading Railroad":
                    if space > 40:
                        space[i] -= 40
                        print("You passed Go and collect $200")
                        money[i] += 200

        elif number == 10:
                while properties[space[i]] != "Boardwalk":
                    space[i] =+ 1
                    print("You are now on Boardwalk")
                    printer = properties[space[i]]
                    determine = prices[space[i]-1]
        elif number == 11:
                money -= 50 * (inputPlayers - 1)
                num = []
                for i in range(1,inputPlayers+1):
                    num.append(i)
                for numb in num:
                    if i != num:
                        money[numb] += 50
        elif number == 12:
                money[i] =+ 150
        elif number == 13:
                money[i] =+ 100
        elif number == 14:
             space[i] -= 3
             printer = properties[space[i]]
             determine = prices[space[i] - 1]
        elif number == 15:
                while properties[space[i]] != "Illinois Avenue":
                    space[i] += 1
                    if space[i] > 40:
                        space[i] -= 40
                    print("You passed Go and collected 200 dollars")
                    money[i] += 200
                print("You are now on Illinois Avenue")
                printer = properties[space[i]]
                determine = prices[space[i] - 1]


        if determine == 'C':
            number = random.radiant(1,17)
            card = chance[number]
            time.sleep(1)
            print("You draw a Community Chest card that says: ")
            time.sleep(1)
            print(card)
            if number ==1:
                if number ==1:
                    space[i] ==41
                elif number ==2:
                    money[i] += 200
                elif number ==3:
                    money[i] -= 50
                elif number == 4:
                    money[i] +=50
                elif number == 5:
                    jailfree[i] += 1
                elif number == 6:
                    determine = "J"
                elif number == 11:
                    money = 50 * (inputPlayers - 1)
                    num = []
                    for i in range(1,InputPlayers+1):
                        num.append(i)
                    for numb in num:
                        if i != numb:
                            money[numb] -= 50
                elif number == 8:
                        money[i] += 100
                elif number == 11:
                        money[i] += 100
                elif number == 12:
                        money[i] += 50
                elif number == 13:
                        money[i] += 50
                elif number == 14:
                        money[i] -= 50
                elif number == 15:
                        money[i] += 25
                elif number ==16:
                        money[i] += 10
                elif number ==17: 
                        money[i] += 100



#Gives players $200 after passing Go. Since there are 40 spaces on the board, when space > 40, the player should collect $200.
            if space[i] > 40 and space[i] != 41:
                space[i] -= 40
                print("You passed Go and collected $200")
                money[i] += 200
            elif space[i] ==41:
                print("You are on Go. Collect $200")
                space[i] -= 40
                money[i] += 200


            elif isnumeric(determine) == True and printer in deeds:
                    inputBuy = input("Type 'yes' to buy " + printer + "for $" + str(determine) + ":")
                    prop += 1
                    if inPutBuy.lower() == "yes":

    if  i  == 1:
    money[i] -= determine
    deeds.remove(printer)
    deeds1.append(printer)

    
elif i ==2:
    money[i] -= determine
elif i == 3:
    money[i] -=determine
    deeds.remove(printer)
                     deeds2.append(printer)
          elif i ==4:
                        money[i] -= determine
                        deeds.remove(printer)
                        deeds4.append(printer)
          else:
                    nobuy = 1

          elif i ==1 and printer in deeds1:
                    print("You own " + printer + " and are allowed to stay for free")
                    time.sleep(1)
                elif i ==2 and printer in deeds2:
                    print("You own " + printer + " and are allowed to stay for free")
                    time.sleep(1)
                elif i ==3 and printer in deeds3:
                    print("You own " + printer + " and are allowed to stay for free")
                    time.sleep(1)
                elif i ==4 and printer in deeds4:
                    print("You own " + printer + " and are allowed to stay for free")
                    time.sleep(1)

                elif isnumeric(determine) == True and printer not in deeds:
                    time.sleep(1)
                    if check[colors[printer]] == 1:
                        if house[housing[printer]] == 0:
                            tax = price(determine)

                if printer in deeds1 and i != 1:
                        print("Player 1 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[!] += tax

                if printer in deeds2 and i != 2:
                        print("Player 2 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[!] += tax

                if printer in deeds3 and i != 3:
                        print("Player 3 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[!] += tax

                if printer in deeds4 and i != 4:
                        print("Player 4 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[!] += tax


                money[i] -= tax

            elif determine == "R" and printer in deeds:
                prop = 1
                inputBuy = input("Type 'yes' to buy " + printer + " for $" + str(200) + ")
                if inputBuy.lower() == "yes":
                    if i == 1:
                        money[i] -= 200
                        deeds.remove(printer)
                        deeds1.append(printer)
                        rail1.add(printer)

                    if i == 2:
                        money[i] -= 200
                        deeds.remove(printer)
                        deeds2.append(printer)
                        rail2.add(printer)

                    if i == 3:
                        money[i] -= 200
                        deeds.remove(printer)
                        deeds3.append(printer)
                        rail3.add(printer)

                    if i == 4:
                        money[i] -= 200
                        deeds.remove(printer)
                        deeds4.append(printer)
                        rail4.add(printer)

                else:
                    nobuy = 1

            elif determine == "R" and printer not in deeds:
                time.sleep(1)
#Determines the amount player must pay to another player for landing on railway, depending on how many railways the other player owns.
            if printer in deeds1 and i != 1:
                if en(rail1) == 1:
                    tax = 25
                elif len(rail1) == 2:
                    tax = 50
                elif len(rail1) == 3:
                    tax = 100
                elif len(rail1) == 4:
                    tax = 200
            if printer in deeds2 and i != 2:
                if en(rail2) == 1:
                    tax = 25
                elif len(rail2) == 2:
                    tax = 50
                elif len(rail2) == 3:
                    tax = 100
                elif len(rail2) == 4:
                    tax = 200
            if printer in deeds3 and i != 3:
                if en(rail3) == 1:
                    tax = 25
                elif len(rail3) == 2:
                    tax = 50
                elif len(rail3) == 3:
                    tax = 100
                elif len(rail3) == 4:
                    tax = 200
            if printer in deeds4 and i != 4:
                if en(rail4) == 1:
                    tax = 25
                elif len(rail4) == 2:
                    tax = 50
                elif len(rail4) == 3:
                    tax = 100
                elif len(rail4) == 4:
                    tax = 200

            if printer in deeds1 and i != 1:
                print("Player 1 owns this property and so you are forced to pay $" + str(tax) + " for your stay")
                money[i]+= tax

            if printer in deeds2 and i != 2:
                print("Player 2 owns this property and so you are forced to pay $" + str(tax) + " for your stay")
                money[i]+= tax

            if printer in deeds3 and i != 3:
                print("Player 3 owns this property and so you are forced to pay $" + str(tax) + " for your stay")
                money[i]+= tax

            if printer in deeds4 and i != 4:
                print("Player 4 owns this property and so you are forced to pay $" + str(tax) + " for your stay")
                money[i]+= tax

            money[i] -= tax

            elif determine == "j" and printer not in deeds:
                time.sleep(1)

                print("You have been put in Jail")
                j[i] += 1
                space[i] = 11

            elif determine == "E" and printer in deeds:
                inputBuy = input("Type 'yes' to buy " + printer + "for $" + str(150) + ';'")
                if inputBuy.lower() == "yes":
                    if i == 1:
                        money[i] -= 150
                        deeds.remove(printer
                        deeds1.append(printer)
                        util1.add(printer)
                    elif i == 2:
                        money[i] -= 150
                        deeds.remove(printer
                        deeds2.append(printer)
                        util1.add(printer)
                    elif i == 3:
                        money[i] -= 150
                        deeds.remove(printer
                        deeds3.append(printer)
                        util1.add(printer)
                    elif i == 4:
                        money[i] -= 150
                        deeds.remove(printer
                        deeds4 .append(printer)
                        util1.add(printer)
                else:
                    nobuy = 1

                elif determine == "E" and printer not in deeds:
                    inputBlank = input("Press enter to roll your fee")
                    tax = roll(2)
                    if printer in deeds1 and i != 1:
                        if len(util1) == 1:
                            tax = tax*4
                        elif len(util1) == 2:
                            tax = tax*10
                    if printer in deeds2 and i != 2:
                        if len(util1) == 1:
                            tax = tax*4
                        elif len(util1) == 2:
                            tax = tax*10
                    if printer in deeds3 and i != 3:
                        if len(util1) == 1:
                            tax = tax*4
                        elif len(util1) == 2:
                            tax = tax*10
                    if printer in deeds4 and i != 4:
                        if len(util1) == 1:
                            tax = tax*4
                        elif len(util1) == 2:
                            tax = tax*10

                if printer in deeds1 and i != 1:
                        print("Player 1 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[1] += tax

                 if printer in deeds1 and i != 2:
                        print("Player 2 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[2] += tax

                if printer in deeds1 and i != 3:
                        print("Player 3 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[3] += tax

                if printer in deeds1 and i != 4:
                        print("Player 4 owns this property and you are forced to pay $" + str(tax) + " for your stay")
                        money[4] += tax


                money[i] -= tax
#Frees players in event of successful dice roll
                if j[i] == 1:
                    if jailfree[i] > 0:
                        inputFree = input("Type 'yes' to use your get out of jail free card: ")
                        if inputFree.lower() == "yes":
                            j[i] = 0
                        inputFree = input("Type 'yes' to use your get out of jail free card: ")
                        if inputFree
                        
