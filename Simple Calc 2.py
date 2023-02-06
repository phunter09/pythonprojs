operator = ""
first = 0
second = 0
output = 0

print('''
*****Types of operation*****

1. +

2. -

3. *

4. /

****************************
''')

while operator != "Q":

    operator = str(input("Key in the number for operator (1 to 4 or Q to quit): "))
        
    if operator == "Q":
        break

    first = int(input("Enter your first number? "))

    second = int(input("Enter your second number? "))

    if operator == "1":
        output = first + second
        print(output)
        
    elif operator == "2":
        output = first - second
        print(output)
        
    elif operator == "3":
        output = first * second
        print(output)
        
    elif operator == "4":
        output = first / second
        print(output)

print("Thank you for using this calculator!")


    




      
