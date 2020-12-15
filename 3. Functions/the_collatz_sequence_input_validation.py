# add try and except cluase to detect if the user types in a noninteger string
## it must go inside the collatz function block

# collatz function with parameter = number
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return(3 * number + 1)

## main program
chosen_number = ''

while True:
    if chosen_number != 1:
        print('Enter a number: ', end='')
        try:
            chosen_number = int(input())
            while chosen_number != 1:  
                chosen_number = collatz(chosen_number)
        except ValueError:
            print('Please input an integer value...')
    else:
        break