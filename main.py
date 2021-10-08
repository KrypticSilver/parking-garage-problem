# makes a string of 50 equals signs for a line break
separator = "=" * 50

if True: print("hi") else: print("no")

# creates a 2d list with 10 rows
car_park = [[] for i in range(10)]

# filling the car park
for i in range(10):
  for j in range(6):
    car_park[i].append("E") # e stands for empty


# creates the interface for allowing the user to leave 
def leave_menu():
  print(separator)
  print("Do you want to try again or exit to main menu?")
  print("1 = Try again.")
  print("2 = Exit to main menu.")
  print(separator)
  exit_choice = input(">>> ")

  if exit_choice == "2":
    return True

  else:
    return False


# goes through each index of the park and makes it "e"
def empty_park():
  for i in range(10):
    for j in range(6):
      car_park[i][j] = "E"
  
  print(separator)
  print("Success, all spaces now are empty.")


# allows the user to remove a car based on its plate
def remove_car():
  removed = False

  while not(removed):
    print(separator)
    print("What is the number plate of the car?")
    print(separator)
    plate_number = input(">>> ")

    for index_i, i in enumerate(car_park):
      for index_j, j in enumerate(i):
        if j == plate_number:
          car_park[index_i][index_j] = "E";
          removed = True

    if not(removed):
      print(separator)
      print(f"Could not find car with registration '{plate_number}', please try again.")

      if leave_menu():
        break

      else:
        continue

    
    else:
      print(separator)
      print(f"Congratulations car with registration '{plate_number}' has\nsuccessfully been removed.")
          

    
# allows the user to add a number plate to the garage
def park_car():
  while True:
    print(separator)
    print("What row are you parking in?")
    print("Rows must be between 1 and 10.")
    print(separator)
    row = input(">>> ")

    print(separator)
    print("What space are you parking in?")
    print("Spaces must be between 1 and 6.")
    print(separator)
    column = input(">>> ")

    print(separator)
    print("What is your registration number?")
    print(separator)
    plate_number = input(">>> ")

    print(separator)
    print(f"Car with registration '{plate_number}' has\nsuccessfully been parked in row {row}, column {column}.")

    try:
      row = int(row)
      column = int(column)
      column_arr = []

      car_park[row - 1][column - 1] = plate_number

      for c, i in enumerate(car_park):
        column_arr.append(car_park[c][column - 1])

      max_length = len(max(column_arr, key=len))

      for c, i in enumerate(car_park):
        i[column - 1] = i[column - 1] + (" " * (max_length - len(i[column - 1])))

      break

    except:
      print(separator)
      print(f"Invalid input detected, please try again.")

      if leave_menu():
        break

      else:
        continue


# displays the entire garage in a neat format for the user
def show_park():
  print(separator)
  print("Parking Garage: ")
  print(" ")

  for c, i in enumerate(car_park):
    print(f"[ {'  '.join(i)} ]")

  print("\n* E stands for empty.")

while True:
  print(separator)
  print("What would you like to do?")
  print("1 = Set all spaces to empty.")
  print("2 = Park a car.")
  print("3 = Remove a car.")
  print("4 = Display the parking grid.")
  print("5 = Quit.")
  print(separator)

  option_chosen = input(">>> ")

  if option_chosen == "1":
    empty_park()

  elif option_chosen == "2":
    park_car()

  elif option_chosen == "3":
    remove_car()

  elif option_chosen == "4":
    show_park()

  elif option_chosen == "5":
    print(separator)
    print("Success, program has quit.")
    print(separator)
    quit()

  else:
    print(separator)
    print("Option not recognised, please try again")

