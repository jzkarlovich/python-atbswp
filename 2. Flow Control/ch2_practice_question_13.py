# Write a short program that prints the numbers 1 to 10 using a for loop. 
# Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# for loop:
for i in range(10):
    print(str(i + 1))

# while loop equivalent:
n = 0
while n < 10:
    for n in range(10):
        print(str(n + 1))
    break