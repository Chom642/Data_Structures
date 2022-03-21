InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Chris",  
               "LastName": "Hom",  
               "DOB": "Nov 05",  
               "Residence": "San Diego",  
               "Favorite food": "Rice",  
              })  

InfoDb.append({  
               "FirstName": "Kyle",  
               "LastName": "mans",  
               "DOB": "June 7",  
               "Residence": "New York",  
               "Favorite Food": "Lettuce",
              })

InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Man",  
               "DOB": "October 23",  
               "Residence": "San Jose",  
               "Favorite Food": "Pizza", 
              })

InfoDb.append({  
               "FirstName": "Jeremy",  
               "LastName": "Money",  
               "DOB": "None",  
               "Residence": "Unknown",  
               "Favorite Food": "Rice",
               })

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

def for_loop(n):
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

# this is test driver or code that plays when executed directly, versus import which will not run these statements
def tester1():
    num = int(input("Enter a number for factorial: "))
    # check if the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", recur_factorial(num))
