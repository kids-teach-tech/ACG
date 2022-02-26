#Init

import random as r

Fist = ("Dual Katana", 1, 0, ["sword"])
Item_Dual_Katana = ("Dual Katana", 200000, 1, ["sword", 0])
Item_LifelessEdge = ("Lifeless Edge", 30, 1000, ["sword", 0])
Item_Goats_Horn = ("Goat's Horn", 20, 300, ["sword", 0])
Item_Astral_Dagger = ("Astral Dagger", 300, 4000, ["sword", 0])
Item_Rusty_Dagger = ("Rusty Dagger", 2, 2, ["sword", 0])
Item_Dev_Sword = ("Dev Sword", 10000000000000, 1, ["sword", 0])

Armor_Brass_Helmet = ("Brass Helmet", 5, 1, ["armor", "helmet"])
Armor_Brass_Chestplate = ("Brass Chestplate", 5, 1, ["armor", "chestplate"])
Armor_Brass_Leggings = ("Brass Leggings", 5, 1, ["armor", "leggings"])
Armor_Brass_Boots = ("Brass Boots", 5, 1, ["armor", "boots"])

Boss_Cheese_Man = ["Cheese Man", [1,30], [100,100], 1000, [Armor_Brass_Helmet, Armor_Brass_Chestplate, Armor_Brass_Leggings, Armor_Brass_Boots]]
Boss_Ninja = ["Ninja", [20,60], [300,300], 2000, [Armor_Brass_Helmet, Armor_Brass_Chestplate, Armor_Brass_Leggings, Armor_Brass_Boots]]
Boss_Giant = ["Giant", [50,80], [500,500], 4000, [Armor_Brass_Helmet, Armor_Brass_Chestplate, Armor_Brass_Leggings, Armor_Brass_Boots]]
Boss_Boulder_Bro = ["Boulder Bro", [80,110], [1000,1000], 8000, [Armor_Brass_Helmet, Armor_Brass_Chestplate, Armor_Brass_Leggings, Armor_Brass_Boots]]

Weapons4Life = ["Weapons4Life", Item_Dev_Sword, Item_Dual_Katana, Item_LifelessEdge, Item_Astral_Dagger, Item_Rusty_Dagger]

Harmful_Vibes = ["Harmful Vibes",Item_Dev_Sword , Item_Dual_Katana, Item_LifelessEdge, Item_Goats_Horn, Item_Rusty_Dagger]

Armor_Extravaganza = ["Armor Extravaganza", Armor_Brass_Helmet, Armor_Brass_Chestplate, Armor_Brass_Leggings, Armor_Brass_Boots]

Shops_Main = ["Shops", Weapons4Life, Harmful_Vibes, Armor_Extravaganza]

Boss_Main = (Boss_Cheese_Man,Boss_Ninja,Boss_Giant,Boss_Boulder_Bro)

player = {
  "coins": 0,
  "health": [100,100],
  "inventory": {
    "sword": {
      0: Fist},
    "armor": {
      "helmet": "None",
      "chestplate": Armor_Brass_Chestplate,
      "leggings": Armor_Brass_Leggings,
      "boots": Armor_Brass_Boots}}}

Speech_Main = [("Mayor: Welcome to the city of CHEESE!","Mayor: You must be tired from your long travel...","Mayor: Before you rest, I would like to award you for your heroic actions.","Mayor: I the ruler of this peaceful land, bestow upon you 500 of the regional coins"),("You: Now I should explore this wonderful city","You: I wonder what exciting things I can find...","Y0u: what I can find about myself...","Y0=: my past...","*0=: my future..."),("Citizen: OH MY, THANK YOU SO MUCH, I THOUGH I WAS GOING TO DIE")]

#Def

def valcoins(action, evalcoins, printcoins):
  global player
  timemachine_coins = player["coins"]
  if action == "-":
    player["coins"] -= evalcoins
  elif action == "+":
    player["coins"] += evalcoins
  if player["coins"] <= 0:
    player["coins"] = timemachine_coins
    if printcoins == True:
      print ("No sufficcent balance -")
      print ("[You now have", player["coins"], "coins]")
    return False
  else:
    if printcoins == True:
      print ("[You now have", player["coins"], "coins]")
    return True

def valhealth(action, evalhealth, printhealth):
  global player
  if action == "-":
    print("Your armor blocked", evalhealth * ((player["inventory"]["armor"]["helmet"][1] + player["inventory"]["armor"]["chestplate"][1] + player["inventory"]["armor"]["leggings"][1] + player["inventory"]["armor"]["boots"][1])/100), "damage and", end = " ")
    evalhealth *= 1 - ((player["inventory"]["armor"]["helmet"][1] + player["inventory"]["armor"]["chestplate"][1] + player["inventory"]["armor"]["leggings"][1] + player["inventory"]["armor"]["boots"][1])/100)
    player["health"][0] -= evalhealth
    print("you lost", evalhealth, "health.")
  elif action == "+":
    player["health"][0] += evalhealth
    print("You gained", evalhealth, "health.")
  elif action == "res":
    player["health"][0] = player["health"][1]
    print("You restored yourself to", player["health"][1], "health.")
  if printhealth == True:
    print("Your health is now:", player["health"][0], "/", player["health"][1], "[",end = "")
    for i in range(1,11):
      if i <= round((player["health"][0] / player["health"][1])*10):
        print("=", end = "")
      else:
        print("-", end = "")
    print("]")
  if player["health"][0] < 1:
    quit("You Died!")

def shop():
  global player
  print ("- Choose one of the following shops -")
  for s in range(1,len(Shops_Main)):
    print("{" + str(s) + "} ", end=(""))
    print(Shops_Main[s][0], end=("\n"))
  shoptype = int(input("=- "))
  if shoptype == 0:
    return False
  print("\n-------- SHOP:", Shops_Main[shoptype][0], "--------\nClerk: Welcome to", Shops_Main[shoptype][0] + "!\nClerk: What can I get for you today?\nYou have", player["coins"], "coins")
  for i in range(1,len(Shops_Main[shoptype])):
    print ("____________________\n{" + str(i) + "}", Shops_Main[shoptype][i][0], "\n --Damage:", Shops_Main[shoptype][i][1], "\n --Price:", Shops_Main[shoptype][i][2], "coins")
  userbuy = int(input("____________________\nWhich would you like to buy?\n- Choose one of the above -\n=- "))
  if userbuy == 0:
    print("Clerk: Sorry to see you go!")
    return False
  elif valcoins("-", Shops_Main[shoptype][userbuy][2], True) != False:
    player["inventory"][Shops_Main[shoptype][userbuy][3][0]][Shops_Main[shoptype][userbuy][3][1]] = Shops_Main[shoptype][userbuy]
    print("You bought the", Shops_Main[shoptype][userbuy][0] + "!")
    return True
  else:
    return False
    quit("Invalid Answer")

def bossfight(bossnum):
  global player
  boss = Boss_Main[bossnum]
  print ("\n-------- BOSS BATTLE:", boss[0], "--------\n" + boss[0], "has appeared!")
  bossdeath = 1
  while bossdeath != 0:
    playerchoice = int(input("- Choose one of the below -\n{1} Attack\n{2} Defend\n=- "))
    if playerchoice == 1:
      print("You chose to attack -")
      boss[2][0] -= player["inventory"]["sword"][1]
      print("You attacked", boss[0], "for", player["inventory"]["sword"][1], "damage.")
      print(boss[0], "'s health is now:", boss[2][0], "/", boss[2][1], "[", end = "")
      for i in range(1,11):
        if i <= round((boss[2][0] / boss[2][1])*10):
          print("=", end = "")
        else:
          print("-", end = "")
      print("]")
      if boss[2][0] / boss[2][1] < 0.08:
        bossdeath = 0
      if bossdeath != 0:
        print(boss[0], "attacked!")
        valhealth("-", r.randint(boss[1][0],boss[1][1]), True)
    elif playerchoice == 2: 
      print("You chose to defend -")
      print(boss[0], "attacked!")
      print("You deflected", r.randint(boss[1][0],boss[1][1]), "damage.")
  loot = r.sample(boss[4] ,k=1)
  print(loot)
  print(boss[0], "dropped", boss[3], "coins and a", loot[0] + "!")
  valcoins("+", boss[3], True)
  print("Mayor: For this valiant deed I shall bestow upon you... 100 Health!")
  player["health"][1] += 100
  valhealth("res", 0, True)

#RunTime

valcoins("+", 100000000, True)
shop()
print(player)
bossfight(0)
