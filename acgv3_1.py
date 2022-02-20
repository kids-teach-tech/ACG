#Init

coins = 0
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

Weapons4Life = ("Weapons4Life",Item_Dual_Katana,Item_LifelessEdge,Item_Astral_Dagger)

Harmful_Vibes = ("Harmful Vibes",Item_Dual_Katana,Item_LifelessEdge,Item_Goats_Horn,Item_Rusty_Dagger)

Shops_Main = (Weapons4Life, Harmful_Vibes)

inventory = {
  "sword": "None",
  "sword": "None",
  "armor": {
    "helmet": "None",
    "chestplate": "None",
    "leggings": "None",
    "boots": "None"
  }
}

Speech_Main = [("Mayor: Welcome to the city of CHEESE!","Mayor: You must be tired from your long travel...","Mayor: Before you rest, I would like to award you for your heroic actions.","Mayor: I the ruler of this peaceful land, bestow upon you 500 of the regional coins"),("You: Now I should  explore this wonderful city","You: I wonder what exciting things I can find...","Y0u: what I can find about myself...","Y0=: my past...","*0=: my future..."),("Citizen: OH MY, THANK YOU SO MUCH, I THOUGH I WAS GOING TO DIE")]

#Definitions

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
      print ("[You now have", coins, "coins]")
    return False
  else:
    if printcoins == True:
      print ("[You now have", coins, "coins]")
    return True

def shop():
  print("Clerk: Welcome to", Shops_Main[shoptype][0] + "!\nClerk: What can I get for you today?\nYou have", coins, "coins")
  for i in range(1,len(Shops_Main[shoptype])):
    for l in range(len(Shops_Main[shoptype][i])):
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
  for i in range(len(Shops_Main[shoptype])):
    replogi = Shops_Main[shoptype][i]
    if i == userbuy:
      userbuy = replogi
  if valcoins("-", userbuy[2], True) == True:
    inventory["sword"] = userbuy
