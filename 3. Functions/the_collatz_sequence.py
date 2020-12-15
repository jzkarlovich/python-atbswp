# collatz function with parameter = number
def collatz(number):
    # if number is even print(number//2)
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    # if number is odd print and return 3 * number + 1
    else:
        return 3 * number + 1
        print(3 * number + 1)

## main program
# define number
print('Enter a number: ')
chosen_number = int(input())

while chosen_number != 1:  
    chosen_number = collatz(chosen_number)

