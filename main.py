import json
import requests
import locale


print("=== CS Inventory ===")

locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

inventory = []

def load_data():
  global inventory
  try:
    with open("inventory.json", "r") as file:
      inventory = json.load(file)
  except:
    inventory = []
def save_data():
  with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)
def add_skin():
  print("\n=== Add New Skin ===")

  weapon = input("Input Weapon Name :")
  name = input("Input Skin Name :")
  rarity = input("Input Skin Rarity :")
  condition = input("Input Skin Condition :")
  float_value = float(input("Input Skin Float :"))
  price = int(input("Input Skin Price :"))
  recent_price = int(input("Input Recent Price :"))
  profit = recent_price - price
  market_hash_name = f"{weapon} | {name} ({condition})"
  
  skin = {
        "weapon": weapon,
        "name": name,
        "rarity": rarity,
        "condition": condition,
        "float_value": float_value,
        "price": price,
        "recent_price": recent_price,
        "profit": profit
      }

  inventory.append(skin)
  print("✅Skin added to inventory")
def show_skin():
  print("\n=== Database Skin ===")

  if len(inventory) == 0:
    print("Inventory is empty")

  for i, skin in enumerate(inventory):
      print(f"\n=== Skin {i+1} ===")

      print("\nWeapon:", skin["weapon"])
      print("Name:", skin["name"])
      print("Rarity:", skin["rarity"])
      print("Condition:", skin["condition"])
      print("Float:", skin["float_value"])
      print("Price:", skin["price"])
      print("Recent_Price:", skin["recent_price"])
      print("Profit:", skin["profit"])
def search_skin():
  print("\n=== Search Skin ===")

  if len(inventory) == 0:
      print("Inventory is empty")
      return

  keyword = input("Enter Skin Name: ").lower()
  found = False

  for skin in inventory:
    if keyword in skin["name"].lower():
      print("\nName:", skin["name"])
      print("Rarity:", skin["rarity"])
      print("Condition:", skin["condition"])
      print("Float:", skin["float_value"])
      print("Price:", skin["price"])
      print("Recent_Price:", skin["recent_price"])
      print("Profit:", skin["profit"])
      found = True
  if not found:
    print("Skin not found!")
def delete_skin():
  print("\n=== Delete Skin ===")

  if len(inventory) == 0:
    print("Inventory is empty")
    return

  for i, skin in enumerate(inventory):
    print(f"{i+1}. {skin['name']}")

  try:
    choice = int(input("Choose skin to delete: "))
    index = choice - 1

    if 0 <= index < len(inventory):
      deleted_skin = inventory.pop(index)
      print(f"✅ {deleted_skin['name']} has been deleted")
    else:
      print("Invalid number!")

  except ValueError:
    print("Please enter a valid number!")   
def update_skin():
  print("\n=== Update Skin ===")

  if len(inventory) == 0:
    print("Inventory is empty")
    return

  for i, skin in enumerate(inventory):
    print(f"{i+1}. {skin['name']}")

  try:
    choice = int(input("Choose Skin Number to Update: "))
    index = choice - 1

    if 0 <= index < len(inventory):
      skin = inventory[index]

      print("\nPress Enter to keep current value")
      new_name = input(f"Enter Skin Name [{skin['name']}]: ")
      new_rarity = input(f"Enter Skin Rarity [{skin['rarity']}]: ")
      new_condition = input(f"Enter Skin Condition [{skin['condition']}]: ")
      new_float = input(f"Enter Skin Float [{skin['float_value']}]: ")
      new_price = input(f"Enter Skin Price [{skin['price']}]: ")
      new_recent_price = input(f"Enter Skin Recent Price [{skin['recent_price']}]: ")

      if new_name:
        skin["name"] = new_name
      if new_rarity:
        skin["rarity"] = new_rarity
      if new_condition:
        skin["condition"] = new_condition
      if new_float:
        skin["float_value"] = float(new_float)
      if new_price:
        skin["price"] = int(new_price)
      if new_recent_price:
        skin["recent_price"] = int(new_recent_price)
        
      skin["profit"] = skin["recent_price"] - skin["price"]

      print("✅ Skin updated successfully!")

    else:
      print("Invalid number!")

  except ValueError:
    print("Please enter a valid number!")
def sort_profit():
  print("\n=== Sort by Profit ===")

  if len(inventory) == 0:
    print("Inventory is empty")
    return

  sorted_skin = sorted(inventory, key=lambda skin: skin["profit"], reverse=True)

  for skin in sorted_skin:
    print("\nName:", skin["name"])
    print("Rarity:", skin["rarity"])
    print("Condition:", skin["condition"])
    print("Float:", skin["float_value"])
    print("Price:", skin["price"])
    print("Recent_Price:", skin["recent_price"])
    print("Profit:", skin["profit"])
def summary():
  print("\n=== Inventory Summary ===")

  if len(inventory) == 0:
    print("Inventory is empty")
    return

  total_buy = 0
  total_profit = 0

  for skin in inventory:
    total_buy += skin["price"]
    total_profit += skin["profit"]

  average_profit = total_profit / len(inventory)

  print("Total Skin:", len(inventory))
  print("Total Buy: ", total_buy)
  print("Total Profit: ", total_profit)
  print("Average Profit: ", round(average_profit, 2))
def get_steam_price(market_hash_name):
  url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={market_hash_name}"

  params = {
    "appid": 730,
    "currency": 1,
    "market_hash_name": market_hash_name
  }
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
  
  response = requests.get(url, params=params, headers=headers)
  data = response.json()
      
  if data.get("success"):
      price = data.get("lowest_price") or data.get("median_price")

      if price:
        price = price.replace("$", "").replace(",", "")
        return float(price)
  
  return None
def update_steam_price():
  print("\n=== Update Steam Price ===")
  if len(inventory) == 0:
    print("Inventory is empty")
    return

  for skin in inventory:
    steam_market_price = skin.get("market_hash_name")

    if not steam_market_price : steam_market_price = f"{skin['weapon']} | {skin['name']} ({skin['condition']})"
    steam_price = get_steam_price(steam_market_price)
    
    if steam_price:
      skin["recent_price"] = steam_price
      skin["profit"] = skin["recent_price"] - skin["price"]

      print(f"{steam_market_price} updated")

    else:
      print(f"{steam_market_price} price not found")

  save_data()
    

load_data()

# Main Menu

while True:
  print("\n=== Inventory Menu ===")
  print("1. Add Skin")
  print("2. Show Skin")
  print("3. Search Skin")
  print("4. Delete Skin")
  print("5. Update Skin")
  print("6. Summary")
  print("7. Sort by Profit")
  print("8. Update Steam Price")
  print("9. Exit")

  choice = input("Choose Menu :")

  if choice == "1":
    add_skin()
    save_data()
  elif choice == "2":
    show_skin()    
  elif choice == "3":
    search_skin()     
  elif choice == "4":
    delete_skin()
    save_data()
  elif choice == "5":
    update_skin()
    save_data()
  elif choice == "6":
    summary()
  elif choice == "7":
    sort_profit()
  elif choice == "8":
    update_steam_price()
  elif choice == "9":
    print("Thank you for using CS Inventory!")
    break
  else:
    print("Invalid Choice!")




#if you want donate some skin to me, you can send it to my steam trade link below
#https://steamcommunity.com/tradeoffer/new/?partner=396225350&token=6B7gp8nQ