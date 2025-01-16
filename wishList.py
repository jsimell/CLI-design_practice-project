# Prints a list of all the available commands
def help():
  print("""Please enter one of the following commands:\n
  - add <item>        adds an item to the wish list
  - remove <item>     removes an item from the wish list
  - list              lists the items in the wish list
  - help              lists the available commands
  - quit              closes the application""")


print("\n*** Welcome to the wish list app! ***\n")
help()
wishList = []
quit = False

### Main loop ###
while not quit:
  print()  # Print an empty line before each input
  cmd = input("> ")
  print("  ", end="")  # To align the output nicely with the input

  if not cmd.strip(): continue  # If command is empty, do nothing

  match cmd.split(maxsplit=1):  # Split the input into the command and the possible item
    
    case ["add", item]:
      wishList.append(item)
      print(f"Item {item} added to wish list.")
    
    case ["remove", item]:
      if item in wishList:
        wishList.remove(item)
        print(f"Item {item} removed from wish list.")
      else:
        print(f"Can't remove {item}. No such item in the wish list.")

    case ["list"]:
      if len(wishList) == 0:
        print("Wish list is empty.")
      else:
        print("Items in wish list:")
        [print(f"  - {item}") for item in wishList]
    
    case ["quit"]:
      print("Closing the application...\n")
      quit = True
  
    case ["help"]:
      help()

    case _:
      print("Invalid command. Type 'help' to see the available commands.")