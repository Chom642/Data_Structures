ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[2;0H\u001B[2"
SMILE_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

from tt1 import loops
from tt2 import classes
# from tt3 import
# from tt4 import
# from tt5 import
# from tt6 import
# from tt7 import
# from tt8 import
# from tt9 import
# from tt10 import
# from tt11 import
# from tt12 import
import time

def smile_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(SMILE_COLOR, end="")
    print(sp + "   ( * _ * )  ")
    print(sp + "   < )  ) /   ")
    print(sp + "     /  \     ")
    print(RESET_COLOR)

def smile():
  start = 0
  distance = 30 
  step = 1

  for position in range(start, distance, step):
      smile_print(position)  
      time.sleep(.1)

def diamond():
  sp1 = " " * 4
  sp2 = " " * 2
  print(sp1 + "↑" + sp1)
  print(sp2 + "↑   ↑" + sp2)
  print("←       →")
  print(sp2 + "↓   ↓" + sp2)
  print(sp1 + "↓" + sp1)


def numberSwapper():
  age1 = input('Enter 1st Number: ')
  age2 = input('Enter 2nd Number: ')
  temp = age1
  age1 = age2
  age2 = temp
  print(age1, age2)

def lessNumSwap():
  age1 = input('Enter 1st Number: ')
  age2 = input('Enter 2nd Number: ')
  if age2 > age1:
    print(age1, age2)
  else:
    print(age2, age1)

# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Swapping", numberSwapper],
    ["Smaller # 1st", lessNumSwap],
]

sub_menu0 = [
    ["Animation", smile],
    ["Diamond", diamond],
]

sub_menu1 = [
    ["List Printer", loops.tester],
    ["Fibonacci", "tt1/fibonacci.py"],
]

sub_menu2 = [
  ["Factorial", classes.factorial_print],
  ["Sequential Sum (OOP)", classes.consec_print],
  ["Sequential Sum (Imperative)", classes.seq_sum],
  ["Palindrome Tester", classes.pali_tester],
]

# Menu banner is typically defined by menu owner
border1 = "~" * 25
border2 = "~" * 25 
banner = f"\n{border1}\nSelect An Option\n{border2}"



# def patterns_submenuc
# using patterns_sub_menu list:
# patterns_submenuc works similarly to menuc

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "\n" + "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Swap Menu", submenu])
    menu_list.append(["Animations (tt0)", submenu0])
    menu_list.append(["Lists & Fibonacci (tt1)", submenu1])
    menu_list.append(["Math (tt2)", submenu2])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "\n" + "Swap Submenu" + banner
    buildMenu(title, sub_menu)

def submenu0():
    title = "\n" + "TT0 Submenu" + banner
    buildMenu(title, sub_menu0)

def submenu1():
    title = "\n" + "TT1 Submenu" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "\n" + "TT2 Submenu" + banner
    buildMenu(title, sub_menu2)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '─', value[0])

    # get user choice
    choice = input("Type your choice: ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
