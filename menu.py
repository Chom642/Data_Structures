# menuy.py - function style menu
# Imports typically listed at top
import time
keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [" ", 0, " "]]
# each import enables us to use logic that has been abstracted to other files and folders


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()

# ----------------------------------------------------------

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[3;0H\u001B[2"
ANIMATION_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def animation_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(ANIMATION_COLOR, end="")
    print(sp + "  ______")
    print(sp + " /|_||_\`.__")
    print(sp + "|   _    _ _\"")
    print(sp + "=`-(_)--(_)-'")
    print(RESET_COLOR)

def animation():
    start = 0
    distance = 30
    step = 1

    for position in range(start, distance, step):
        animation_print(position)
        time.sleep(.1)

def matrix():
    for i in keypad:
        for j in i:
            print(j, end=" ")
        print()

def triangle_pattern():
    row = 9

    for i in range(row):
        for j in range(row-i):
            print(' ', end='')

        for j in range(2*i+1):
            print('*',end='')
        print()
    print("---------------------")

def swap():
    a = input("enter first number: ")
    b = input("enter second number: ")
    print("swapping if second number is less than first.")
    print(f"original sequence:  {a}, {b}")
    if b < a:
        b, a = a, b
    print(f"Sequence after swap: {a}, {b}")
    print("---------------------")

# ----------------------------------------------------------

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    buildMenu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)


def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)


main_menu = [
    ["Animation", animation],
    ["Pattern", patterns_submenu],
    ["Numbers", submenu],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu

sub_menu = [
    ["Matrix", matrix],
    ["Swap", swap],
]

patterns_sub_menu = [
    ["Triangle", triangle_pattern],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


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
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

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