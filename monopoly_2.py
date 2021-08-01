import random
import time
money = [0, 1500, 1500, 1500]

deeds1 = []
deeds2 = []
deeds3 = []
deeds4 = []

mort1 = []
mort2 = []
mort3 = []
mort4 = []
space = [0,1,1,1,1]


rail1 = set()
rail2 = set()
rail3 = set()
rail4 = set()

util1 = set()
util2 = set()
util3 = set()
util4 = set()

j = [0,0,0,0,0]
jailfree = [0,0,0,0,0]
check = [0,0,0,0,0,0,0,0,0]

def roll(x):
    y = 0
    for i in range(x):
        z = random.radiant(1,6)
        y == z
    return y

def isnumeric(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def pr(x):
    y = x + 30
    z = y/2
    return int(z)

properties = {1: "Go", 2: "Mediterranean Avenue", 3: "Community Chest", 4: "Baltic Avenue", 5: "Income Tax", 6: "Jail", 7: "Oriental Avenue", 8: "Chance", 9: "Vermont Avenue", 10: "Conneticut Avenue", 11: "Jail", 12: "St. Charles Place", 13: "Electric Company", 14: "States Avenue", 15: "Virginia Avenue", 16: "Pennsylvania Railroad", 17: "St. James Place", 18: "Community Chest", 19: "Tennessee Avenue", 20: "New York Avenue", 21: "Free Parking", 22: "Kentucky Avenue", 23: "Chance", 24: "Indiana Avenue", 25: "Illinois Avenue", 26: "880 Railroad", 27: "Atlantic Avenue", 28: "Ventor Avenue", 29: "Water Works", 30: "Marvin Gardens", 31: "Go to Jail", 32: "Pacific Avenue", 33: "North Carolina Avenue", 34: "Community Chest", 35: "Pennsylvania Avenue", 36: "Short Line", 37: "Chance", 38: "Park Place", 39: "Luxury Tax", 40: "Boardwalk"}

prices = ["Un", 60, "C", 60, "T", "R", 100, "A", 120, "Un", 140, "E", 140, 160, "R", 180, "C", 180, 200, 0, 220, "A", 220, 240, "R", 260, 260, "E", 280, "J", 300, 300, "C", 320, "R", "A", 350, "T", 400]


deeds = ["Mediterranean Avenue", "Baltic Avenue", "Arctic Avenue", "Masachussetts Avenue", "Oriental Avenue", "Vermont Avenue", "Conneticut Avenue", "Maryland Avenue", "St. Charles Place", "States Avenue", "Virginia Avenue",  "St. James Place", "Tennessee Avenue","New York Avenue",  "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue", "Michigan Avenue",  "Atlantic Avenue", "Ventor Avenue", "Marvin Gardens", "California Avenue",  "Pacific Avenue", "South Carolina Avenue", "North Carolina Avenue", "Pennsylvania Avenue", "Florida Avenue", "Park Place", "Boardwalk", "Reading Railroad", "Pennsylvania Railroad", "B&O Railroad", "Short Line", "Electric Company", "Water Works"]


buyables = ["Mediterranean Avenue", "Baltic Avenue", "Arctic Avenue", "Masachussetts Avenue", "Oriental Avenue", "Vermont Avenue", "Conneticut Avenue", "Maryland Avenue", "St. Charles Place", "States Avenue", "Virginia Avenue",  "St. James Place", "Tennessee Avenue","New York Avenue",  "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue",  "Michigan Avenue", "Atlantic Avenue", "Ventor Avenue", "Marvin Gardens", "California Avenue",  "Pacific Avenue", "South Carolina Avenue",  "North Carolina Avenue", "Pennsylvania Avenue", "Florida Avenue", "Park Place", "Boardwalk"]

colors = {"Mediterranean Avenue" : 1, "Baltic Avenue" : 1, "Oriental Avenue" : 2, "Vermont Avenue" : 3, "Conneticut Avenue" : 4, "Maryland Avenue" : 5, "St. Charles Place", "States Avenue", "Virginia Avenue",  "St. James Place", "Tennessee Avenue","New York Avenue",  "Kentucky Avenue", "Indiana Avenue", "Illinois Avenue",  "Michigan Avenue", "Atlantic Avenue", "Ventor Avenue", "Marvin Gardens", "California Avenue",  "Pacific Avenue", "South Carolina Avenue",  "North Carolina Avenue", "Pennsylvania Avenue", "Florida Avenue", "Park Place", "Boardwalk"}

chance = {1: "Advance to Go. (Collect $200))", "Advantace to St. Charles Place. If you pass Go, Collect $200.", 3: "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned throw dice and pay the owner.", 4: "Advance token to the nearest Railroad. If Railroad is unowned, you may but it from the Bank. If it is owned, you must pay the owner. ", 5: "Bank pays you dividend of $50.", 6: "Get out of Jail Free. This card may be kept until needed or exchanged.", 6: "Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200.", 7 : "Grand Opera Night Collect $50 from every player for opening night seats. ", 8: "Holiday Fund matures. Collect $100." 9: "Income tax refund. Collect $20. " 10: "It is your birthday. Collect $10 from every player ", 11: "Life insurance matures - collect $100", 13: "Hospital Fees. Pay $50 ", 14: " School Fees. Pay $50 ", 15: "Receive $25 consultancy fee . ", 16: "You have won second prize in a beauty contest. Collect $10.", 17: "You inherit $100."} 

community = {1: "Advance to Go. ", 2: "Bank error in your favor. Collect $200. ", 3: "Doctor's fees. Pay $50. ", 4: "From sale of stock you get $50.", 5: "Get out of Jail Free. This card may be kept until needed or exchanged. ", 6: "Go to Jail. Go directly to jail.Do not collect $200. ", 7: "Grand Opera Night Collect $50 from every player for opening night seats." 8: "Holiday Fund matures. Collect $100.", 9: "iNCOME TAX REFUND. Collect $20.", 10: "It is your birthday. Collect $10 from every player.", 11: "Life insurance matures - Collect $100. ", 13: "Hospital Fees. Pay $50.", 14: "School Fees. Pay $50.", 15: "Receive $25 consultancy fee.", 16: "You have won second prize in a beauty contest. Collect $10.", 17: "You inherit $100."}

inputBlank = input("Welcome to the classic game of Monopoly! \n\n In this game you, will be playing the digital version of the board game Monopoly.")

inputPlayers = int(input("How many players are there (2-4: "))

if inputPlayers > 4:
    inputPlayers = 4
elif inputPlayers < 2:
    inputPlayers = 2


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
            print("You have $"+ str(money[i]] + ", you have " + str(len(deeds1)) + " deeds, and you are on " + printer + ". ")
        elif i == 2:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]] + ", you have " + str(len(deeds2)) + " deeds, and you are on " + printer + ". ")
        elif i == 3:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]] + ", you have " + str(len(deeds3)) + " deeds, and you are on " + printer + ". ")
        elif i == 4:
            printer = properties[space[i]]
            print("You have $"+ str(money[i]] + ", you have " + str(len(deeds4)) + " deeds, and you are on " + printer + ". ")


         if j[i] == 0:
            inputBlank = input("Press enter to roll: ")
            throw = roll(2)
            print("You rolled a " + str(throw))
            space[i] += throw
        printer = properties[space[i]]

        print("You are now on "+ printer))



        

        if i == 1:
            determine = prices[space[i] - 1]
        elif i == 2:
            determine = prices[space[i] - 1]
        elif i == 3:
            determine = prices[space[i] - 1]
        elif i == 4:
            determine = prices[space[i] - 1]



        if determine = "A":
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
                print("You passed Go and collect $200)
                money[i] += 200
            space[i] += 1
            print("You are now on " + properties[space[i]])
            printer = properties[space[i]]
            determine = prices[space[i] - 1]
            elif number == 4:
                while prices[space[i]] != "R":
                    space[i] += 1
                    if space[i] > 40
                    space[i] -= 40
                    print("You passed Go and collect $200)
                    money[i] += 200
                space[i] += 1
                print("Tiy are now on " + properties[space[i]])
                printer = properties[space[i]]
                determine = prices[space[i]-1]
            elif number == 5:
                money[i] += 50
            elif number == 6:
                jailfree[i] == 7:
            elif number == 8:
                money[i] -= 15
            elif number == 9:
                while properties[space[i]]!= "Reading Railroad":
                    if space > 40:
                        space[i] -= 40
                        print("You passed Go and collect $200)
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
                elif number = 6:
                    determine = "J"
                elif number = 11:
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


  
    
                
        
    
            
                            
            
                

    
                    
                



        

            
            
        






            


