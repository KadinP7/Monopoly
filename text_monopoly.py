import random
import time

money = [0,1500,1500,1500]

assets  = []
assets2 = []
assets3 = []
assets4 = []


mortgage  = [] 
mortgage2 = []
mortgage3 = []
mortgage4 = []

space = [0,1,1,1]

railway  = set()
railway2 = set()
railway3 = set()
railway4 = set()

util =  set()
util2 = set()
util3 = set()
util4 = set()

j = [0,0,0,0,0]
jailfree = [0,0,0,0]
check = [0,0,0,0,0,0,0,0,0]


def roll(a):
    b = 0
    for i in range(a):
       c = random.radiant(1,6)
    b = c
    return b

def is_numeric(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def price(x):
    b = a - 30
    c = b / 2
    return int(z)

properties = {1: "Go", 2: "Peachtree Avenue", 3: "Community Chest", 4: "Cherokee Avenue", 5: "Income Tax", 6: "Great Walton Railroad", 7: "Piedmont Avenue", 8: "Chance", 9: "Almenta Avenue", 10: "Chicago Avenue", 11: "Jail", 12: "Jesse Hill Jr. Drive", 13: "Electric Company", 14: "Xermona Clayton Drive", 15: "Hamilton E. Holmes Drive", 16: "Western and Atlantic Railroad", 17: "Chance", 18: "Go to Jail", 19: "Decatur Avenue", 20: "Buckhead Avenue"}
              
prices = ["A", 50, "B", 50, "C", 100, "D", 100, "E", 150, "F", 180, "G", 240, "H", 260]

deeds = ["Peachtree Avenue", "Cherokee Avenue", "Great Walton Railroad", "Piedmont Avenue", "Almenta Avenue", "Chicago Avenue", "Jesse Hill Jr. Drive", "Electric Company", "Xermona Clayton Drive", "Hamilton E. Holmes Drive", "Western and Atlantic Railroad", "Decatur Avenue", "Buckhead Avenue"]

colors = {"Peachtree Avenue": 1, "Cherokee Avenue": 1, "Great Walton Railroad" : 2, "Piedmont Avenue" : 1, "Almenta Avenue" : 3, "Chicago Avenue" : 3, "Jesse Hill Jr. Drive" : 4, "Electric Company" : 2, "Xermona Clayton Drive" : 4, "Hamilton E. Holmes Drive" : 2, "Western and Atlantic Railroad" : 2, "Decatur Avenue" : 5, "Buckhead Avenue" : 5}

chance = {1: "Advance to Go and collect $200", 2: "Go directly to Jail.", 3: "You have been elected Chairman of the Board. Pay each player $50." , 4: "Advance to Cherokee Avenue", 5: "Banking error - you collect $100", 6: "Advance to Electric Company", 7: "Advance to Xermona Clayton Drive", 8: "Your loan matures. Collect $200", 9: "Speeding ticket - pay $50"}

chest = {1: "Go directly to jail.", 2: "You win first place in a knitting contest - collect $30.", 3: "You sprain your wrist - pay $80 in medical fees", 4: "You win the lottery - collect $750",5: "Speeding ticket - pay $50", 6: "Your wallet is stolen - Pay $10", 7: "Nothing happens - how boring."}


blankInput = ("Welcome to Monopoly! \n\n This game is a simplified text-adventure version of the classic monopoly game that takes place in Atlanta, Georgia instead of Atlantic City, New Jersey. \n To make for a more simpler experience some features have been removed/changed (i.e. no houses or hotels, board is 20 tiles instead of 40).")

number_players = int(input("How many people are playing (2-4:"))
                     
                
if number_players > 4:
    number_players  = 4
elif number_players < 2:
    number_players = 2


if i == 1:
    printer = properties[space[i]]
    print ("You have $" + str(money[i]] + ", you have " + str(len(deeds)) + " deeds, and you are on " + printer + ". ")

elif i == 2:
    printer = properties[space[i]]
    print 
