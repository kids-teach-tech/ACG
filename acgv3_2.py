#Init

coins = 10000000
health = 100

Boss_Cheese_Man = ["Cheese Man", 10, 60, 1000]
Boss_Ninja = ["Ninja", 20, 100, 2000]
Boss_Giant = ["Giant", 40, 400, 4000]
Boss_Boulder_Bro = ["Boulder Bro", 100, 1000, 8000]

Boss_Main = (Boss_Cheese_Man,Boss_Ninja,Boss_Giant,Boss_Boulder_Bro)

Item_Dual_Katana = ["Dual Katana", 200000, 1]
Item_LifelessEdge = ["Lifeless Edge", 30, 1000]
Item_Goats_Horn = ["Goat's Horn", 20, 300]
Item_Astral_Dagger = ["Astral Dagger", 300, 4000]
Item_Rusty_Dagger = ["Rusty Dagger", 2, 2]

Weapons4Life = ("Weapons4Life",Item_Dual_Katana,Item_LifelessEdge,Item_Astral_Dagger,Item_Rusty_Dagger)

Harmful_Vibes = ("Harmful Vibes",Item_Dual_Katana,Item_LifelessEdge,Item_Goats_Horn,Item_Rusty_Dagger)

Shops_Main = ("Shops", Weapons4Life, Harmful_Vibes)

inventory = {
  "sword": "None",
  "sheild": "None",
  "armor": {
    "helmet": "None",
    "chestplate": "None",
    "leggings": "None",
    "boots": "None"
  }
}

Speech_Main = [("Mayor: Welcome to the city of CHEESE!","Mayor: You must be tired from your long travel...","Mayor: Before you rest, I would like to award you for your heroic actions.","Mayor: I the ruler of this peaceful land, bestow upon you 500 of the regional coins"),("You: Now I should explore this wonderful city","You: I wonder what exciting things I can find...","Y0u: what I can find about myself...","Y0=: my past...","*0=: my future..."),("Citizen: OH MY, THANK YOU SO MUCH, I THOUGH I WAS GOING TO DIE")]

#Def

def valcoins(action, evalcoins, printcoins):
  global coins
  timemachine_coins = coins
  if action == "-":
    coins -= evalcoins
  elif action == "+":
    coins += evalcoins
  if coins <= 0:
    coins = timemachine_coins
    if printcoins == True:
      print ("No sufficcent balance -")
      print ("[You now have", coins, "coins]")
    return False
  else:
    if printcoins == True:
      print ("[You now have", coins, "coins]")
    return True

def shop():
  print ("- Choose one of the following shops -")
  for s in range(1,len(Shops_Main)):
    print("{" + str(s) + "} ", end=(""))
    print(Shops_Main[s][0], end=("\n"))
  shoptype = int(input("=- "))
  print("Clerk: Welcome to", Shops_Main[shoptype][0] + "!\nClerk: What can I get for you today?\nYou have", coins, "coins")
  for i in range(1,len(Shops_Main[shoptype])):
    print ("____________________")
    print ("{" + str(i) + "}", Shops_Main[shoptype][i][0])
    print ("--Damage:", Shops_Main[shoptype][i][1])
    print ("--Price:", Shops_Main[shoptype][i][2], "coins")
  userbuy = int(input("____________________\nWhich would you like to buy?\n- Choose one of the above -\n=- "))
  if userbuy == 0:
    print("Clerk: Sorry to see you go!")
    return False
  elif valcoins("-", Shops_Main[shoptype][userbuy][2], True) != False:
    inventory["sword"] = Shops_Main[shoptype][userbuy]
    print("You bought the", inventory["sword"][0], "!")
    return True
  else:
    return False
    quit("Invalid Answer")

#Runtime

shop()
