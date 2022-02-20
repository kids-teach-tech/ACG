import sys
#Init

import time

countvar = 1
coins = 0
choice1 = 0
choice2 = 0
health = 100

#Bosses

# [Name, Damage, Health, Reward]
Boss_Cheese_Man = ["Cheese Man", 10, 60, 1000]
Boss_Ninja = ["Ninja", 20, 100, 2000]
Boss_Giant = ["Giant", 40, 400, 4000]
Boss_Boulder_Bro = ["Boulder Bro", 100, 1000, 8000]

Bosses = {
  1: Boss_Cheese_Man,
  2: Boss_Ninja,
  3: Boss_Giant,
  4: Boss_Boulder_Bro,
}

#Items

# [Name, Damage, Price]
Item_Dual_Katana = ["Dual Katana", 20, 500]
Item_LifelessEdge = ["Lifeless Edge", 30, 1000]
Item_Goats_Horn = ["Goat's Horn", 20, 300]
Item_Astral_Dagger = ["Astral Dagger", 300, 4000]
Item_Rusty_Dagger = ["Rusty Dagger", 2, 2]
Item_Gold_Dagger = ["Ekxsy Dagger", 32000, 320000]
Item_Cyber_Dagger = ["Cyber Dagger", 75, 1]
Aahan_infinity_blade = ["Aahan Infinty Blade", 1000000, 500]
Rohans_gauntlet = ["Rohan's Gauntlet", 10000000000000000000000000000000, 1]
#Shops

Weapons4Life = {
  1: Item_Dual_Katana,
  2: Item_LifelessEdge,
  3: Item_Astral_Dagger,
  4: Item_Cyber_Dagger,
  5: Item_Gold_Dagger
}

Harmful_Vibes = {
  1: Item_Dual_Katana,
  2: Item_LifelessEdge,
  3: Item_Goats_Horn,
  4: Item_Rusty_Dagger,
}

Aahan_shop = {
  1: Aahan_infinity_blade,
  2: Rohans_gauntlet
}

shops = ["Weapons4Life", "Harmful Vibes", "Aahan's Bazaar"]
shopsvars = [Weapons4Life, Harmful_Vibes, Aahan_shop]

#Inventory

inventory = {
  "sword": "None",
}

#Dialogue

Dialouge1 = ("Mayor: Welcome to the city of CHEESE!", "Mayor: You must be tired from your long travel...", "Mayor: Before you rest, I would like to award you for your heroic actions.", "Mayor: I the ruler of this peaceful land, bestow upon you 500 of the regional coins")

Dialouge2 = ("You: What is this place?", "You: Why am I here?", "{1} Enter Shop\n{2} Go to Bed")

Dialouge3 = ("You: Now I should  explore this wonderful city", "You: I wonder what exciting things I can find...", "Y0u: what I can find about myself...", "Y0=: my past...", "*0=: my future...")

Dialouge4 = ("Citizen: OH MY, THANK YOU SO MUCH, I THOUGH I WAS GONNA DIE")

Dialouge5 = ("{1} Enter Shop\n{2} Go to Bed")

#Defintions

def valcoins(action, evalcoins, printcoins):
  global coins
  timemachine_coins = coins
  if action == "-":
    coins -= evalcoins
  elif action == "+":
    coins += evalcoins
  if coins < 0:
    coins = timemachine_coins
    if printcoins == True:
      print ("No sufficcent balance -")
      time.sleep(1)
      print ("[You now have", coins, "coins]")
    return False
  else:
    if printcoins == True:
      time.sleep(1)
      print ("[You now have", coins, "coins]")
    return True

def shop(shoptype):
  print("Clerk: Welcome to", str(shops[shoptype-1]) + "!\nClerk: What can I get for you today?\nYou have", coins, "coins")
  currentshop = shopsvars[shoptype-1].copy()
  for i in range(len(currentshop)):
    replogi = currentshop[i+1]
    for l in range(len(replogi)+1):
      if l != 0:
        replogl = replogi[l-1]
      if l == 0:
        print ("____________________")
      elif l == 1:
        print ("{" + str(i) + "}", replogl)
      elif l == 2:
        print ("--Damage:", replogl)
      elif l == 3:
        print ("--Price:", replogl, "coins")
  print("____________________\nWhich would you like to buy?")
  userbuy = int(input("Press the number of the item you would like: "))
  for i in range(len(currentshop)):
    replogi = currentshop[i+1]
    if i == userbuy:
      userbuy = replogi
  if valcoins("-", userbuy[2], True) == True:
    inventory["sword"] = userbuy

def bossfight(bosstype):
  global health
  currentboss = Bosses[bosstype].copy()
  weapon = inventory["sword"]
  print(currentboss[0], "has arisen!\n" + str(currentboss[0]) + ": Grumble Grumble")
  while (currentboss[2] > 0) and (health > 0):
    bosschoice = int(input("{1} Attack\n{2} Defend\nEnter number: "))
    if bosschoice == 1:
      currentboss[2] -= weapon[1]
      print ("You attacked for", str(weapon[1]), "damage.\n[" + str(currentboss[0]), "now has", str(currentboss[2]), "health]")
      health -= currentboss[1]
      print (str(currentboss[0]), "attacked for", str(currentboss[1]), "damage.\n[You now have", health, "health]")
    else:
      print (str(currentboss[0]), "attacked for", str(currentboss[1]), "damage.\n[You still have", health, "health]")
  if health > 0:
    print ("You gained", currentboss[3], "coins and 100 health from defeating", currentboss[0] + "!")
    valcoins("+", currentboss[3], True)
    if bosstype == 4:
      print("You: I guess I know who I am now...\n.*-: The overseer of this world!\nYou: That cant be right...\nAnd as everything goes black you remember who you really are.")
      quit()
    return True
  else:
    print ("You Died!")
    valcoins("-", currentboss[3]/4  , True)
    return False


#Game

for i in range(len(Dialouge1)):
  print(Dialouge1[i])
#  time.sleep(2)

valcoins("+", 500, True)

for i in range(len(Dialouge2)):
  print(Dialouge2[i])
#  time.sleep(2)

choice1=int(input("Press a number: "))
if choice1 == 1:
  print:("Which shop would you like to enter?")
  print("What shop would you like to enter?\n{1} Weapons4Life\n{2} Harmful Vibes")
  choice2=int(input("Press a number: "))
  shop(choice2)
else:
  sys.exit("repl proccess died unexpectidly due to the database of lava pouring on the ecosystem of Mayor due to the calibration of the enums in process exerted with enumeration of 1 next to area 17.5 in codeset 4 block 8 section 32 category 5 server 212. to report this error go to error.enum/external/rewerite/ovr/nexterror/report/export/create/new/true/bycode/code/198120391203/priceable/next and enter category number 𝔞𝔡𝔰𝔣𝔰𝔡𝔣𝔰𝔞𝔡𝔣 and exterior surface number 3")

for i in range(len(Dialouge3)):
  print(Dialouge3[i])
#  time.sleep(2)

bossfight(1)

print(Dialouge4)

while True == True:
  countvar = countvar + 1
  health = countvar*100
  print(Dialouge5)
  choice1=int(input("Press a number: "))
  if choice1 == 1:
    print:("Which shop would you like to enter?")
    print("What shop would you like to enter?\n{1} Weapons4Life\n{2} Harmful Vibes\n{3} Aahan's Bazaar")
    choice2=int(input("Press a number: "))
    shop(choice2)
  else:
    print("You watch as the world slowly fades to black and you are at peace...")
    quit()
  bossfight(countvar)
