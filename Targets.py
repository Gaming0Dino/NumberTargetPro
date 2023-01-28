import os, time, colorama #os for clearing screen, time to stop program, colorama for color
from colorama import Fore #to change color
import pickle
os.system("cls") #start it

# Define a dictionary to store the targets
targets = {}

# Define a filename to save the targets to
filename = "targets.pickle"

# Define a function to create a new target
def create_target(name, value):
    targets[name] = value
    print(f"Target {name} created with value {value}.")
    save_targets()

# Define a function to add to a target
def add_to_target(name, value):
    if name in targets:
        targets[name] += value
        print(f"Added {value} to target {name}. New value: {targets[name]}.")
        save_targets()
    else:
        print(f"Target {name} does not exist.")

# Define a function to subtract from a target
def subtract_from_target(name, value):
    if name in targets:
        targets[name] -= value
        print(f"Subtracted {value} from target {name}. New value: {targets[name]}.")
        save_targets()
    else:
        print(f"Target {name} does not exist.")

# Define a function to delete a target
def delete_target(name):
    if name in targets:
        del targets[name]
        print(f"Target {name} deleted.")
        save_targets()
    else:
        print(f"Target {name} does not exist.")

# Define a function to subtract from a target
def readtarget(name):
    if name in targets:
        print(f"Target {name} has {targets[name]}")
    else:
        print(f"Target {name} does not exist.")

# Define a function to save the targets to a file
def save_targets():
    with open(filename, "wb") as f:
        pickle.dump(targets, f)

# Define a function to load the targets from a file
def load_targets():
    global targets
    try:
        with open(filename, "rb") as f:
            targets = pickle.load(f)
    except:
        pass

# load targets when the program starts
load_targets()

#Keep open
close = False
while not close:
    os.system("cls")#clear
    #selection
    print(Fore.CYAN + "  Number Targets   ")
    print(Fore.LIGHTGREEN_EX + "Made By GamingoDino")
    print(Fore.RESET)

    print("1) Make Target")
    print("2) Delete Target")
    print("3) Read Target")
    print()
    print("4) Add To Target")
    print("5) Subtract From Target")
    print()
    print("6) Exit")
    print()


    sel=input(Fore.LIGHTBLACK_EX + "Select: ")
    os.system("cls")#clear
    if sel=="1":
        newName=input("Name: ")#new
        number=input("Number: ")
        print()
        if not newName=="":
            create_target(newName, int(number))
        else:
            print("Name can not be blank")
        time.sleep(2)
    elif sel=="2":
        newName=input("Name: ")#del
        print()
        delete_target(newName)
        time.sleep(2)
    elif sel=="3":
        newName=input("Name: ")#read
        print()
        readtarget(newName)
        time.sleep(2)
    elif sel=="4":
        newName=input("Name: ")#add
        number=input("Amount: ")
        if number == "":
            number="0"
        print()
        add_to_target(newName, int(number))
        time.sleep(2)
    elif sel=="5":
        newName=input("Name: ")#sub
        number=input("Amount: ")
        if number == "":
            number="0"
        print()
        subtract_from_target(newName, int(number))
        time.sleep(2)
    elif sel=="6":
        close = True#close
    else:
        print("Action not found")#none
        time.sleep(2)