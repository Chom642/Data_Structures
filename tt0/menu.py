import time
from TT1 import fibonacci
from TT1 import loops


menu_options = {
	1: 'Swap',
	2: 'Animation',
	3: 'Loops',
	4: 'Fibonacci',
	5: 'Exit',
}

submenu_swap = {
	1: 'Number Swap', 
	2: 'Lesser Number 1st',
	3: 'Back',
	4: 'Exit',
}

submenu_loop = {
	1: 'For Loop', 
	2: 'While Loop',
	3: 'Recursive Loop',
	4: 'Back',
	5: 'Exit',
}


def print_options():
	for key in menu_options.keys():
		print('\x1B[3m', key, '--', menu_options[key], '\x1B[0m' )
	runOptions1()

def print_sm_options():
	for key in submenu_swap.keys():
		print('\x1B[3m', key, '--', submenu_swap[key], '\x1B[0m' )
	runOptions2()

def print_sml_options():
	for key in submenu_loop.keys():
		print('\x1B[3m', key, '--', submenu_loop[key], '\x1B[0m' )
	runOptions3()

def runOptions1():
	while True:
		try:
			option = int(input('\n' + 'Select a number 1-5: '))
			if option == 1:
				print_sm_options()
			elif option == 2:
				dance()
			elif option == 3:
				print_sml_options()
			elif option == 4:
				fibonacci()
			elif option == 5:  
				print('Goodbye!')
				exit() 
			else:
				print('Invalid input. Please enter a number between 1-3.')
		except ValueError:
			print('Invalid input. Please enter an integer input.')

def runOptions2():
	while True:
		try:
			option = int(input('Select a number 1-4: '))
			if option == 1:
				swap()
			elif option == 2:
				lessNumSwap()
			elif option == 3:
				print("Returning to the main menu...")  
				runOptions1()
			elif option == 4:
				print('You will now exit the menu')
				exit() 
			else:
				print('Invalid option. Please enter a number between 1-4.')
		except ValueError:
			print('Invalid input. Please enter an integer input.')

def runOptions3():
	while True:
		try:
			option = int(input('Select a number 1-5: '))
			if option == 1:
				for_loop(n)
			elif option ==2:
				while_loop(n)
			elif option == 3:
				recursive_loop(n)
			elif option == 4:
				print('Returning to the main menu...')
				runOptions1()
			elif option == 5:
				print('You will now exit the menu')
				exit()
			else:
				print('Invalid option. Please enter a number between 1-5')
		except ValueError:
			print('Invalid input. Please enter an interger input.')

def swap():	
	x = input('Enter value of x: ')
	y = input('Enter value of y: ')
	
	temp = x
	x = y
	y = temp
	
	print('\nThe value of x after swapping: {}'.format(x))
	print('The value of y after swapping: {}'.format(y), '\n')

def lessNumSwap():
	x = input('Enter value of x: ')
	y = input('Enter value of y: ')
	
	if x > y:
		print('\n''{}'.format(x), 'is greater than', '{}'.format(y))
	elif x == y:
		print('{}'.format(x), 'is equal to', '{}'.format(y))
	else:
		print('\n''{}'.format(y), 'is greater than', '{}'.format(x))

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[3;0H\u001B[2"
SMILE_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def dance_print(position):
	print(ANSI_HOME_CURSOR)
	print(RESET_COLOR)
	sp = " " * position
	print('\n')
	print('\n')
	print(SMILE_COLOR, end='')
	print(sp + '\(*_*)')
	print(sp + '   ))Z ')
	print(sp + '  / \ ')
	print(RESET_COLOR)

def dance():
	start = 0
	distance = 30 
	step = 1

	for position in range(start, distance, step):
		dance_print(position)  
		time.sleep(.1)
