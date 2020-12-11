# Chapter 2 Practice Questions

1. What are teh two values of the Boolean data type.  

The two values of the Boolean data type are `True` and `False`. 

2. What are the three Boolean operators? 

    and, or, not

3. Truth Tables for Boolean Operators

`and` Truth Table
| Operator | Evaluates to... |
|:---------|:----------------|
| `True and True` | `True` |
| `True and False` | `False` |
| `False and True` | `False` |
| `Flase and Flase` | `False` |

`or` Truth Table
| Operator | Evaluates to... |
|:---------|:----------------|
| `True and True` | `True` |
| `True and False` | `True` |
| `False and True` | `True` |
| `Flase and Flase` | `False` |  

`not` Truth Table
| Operator | Evaluates to... |
|:---------|:----------------|
| `not True` | `False` |
| `not False` | `True` |

4. What do the following expressions evaluate to? 

(5 > 4) and (3 == 5)  
`False`  
not (5 > 4)  
`False `  
(5 > 4) or (3 == 5)   
`True  `  
not ((5 > 4) or (3 == 5))    
`True `   
(True and True) and (True == False)    
`False  `  
(not False) or (not True)    
`True  `  

5. What are the 6 comparison operators? 

| Operator | Meaning |
|:---------|:--------|
| `==` | equal to |
| `!=` | not equal to |
| `<`  | less than |
| `>`  | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |  

6.  What is the difference between the equal operator and the assignment operator?   

The `=` assignment operator, assigns a value to a variable.  The `==` is a comparison operator that checks if two assignments are equal to one another and evaluate to the Boolean data type `True` or `False`.  

7. Explain what a condition is and where you would use one?  

A condition is an expression and it evaluates down to a Boolean data type. You would use a condition as a flow control statement in order to define how a program is to continue.  

8. Identify the three blocks in this code:  
````python
spam = 0
if spam == 10:
    print('eggs') #1
    if spam > 5:
        print('bacon') #2
    else:
        print('ham') #3
    print('spam')
print('spam')  
````
9. Write code that prints 'Hello' if 1 is stored in spam, prints 'Howdy if 2 is stored in 'spam' and prints 'Greetings!' if anything else is stored in spam.  
````python
import random

spam = str(random.randint(1,3))
print('Random spam value generated is ' + spam + '.')
if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings')  
````
10. What can you press if your program is stuck in an infinite loop?
^C  

11. What is the difference between `break` and `continue`? 
A `break` is used to get out of a loop, while a `continue` loops back to the initial condition. 

12. What is the difference between `range(10)`, `range(0,10)`, and `range(0, 10, 1)` in a for loop?  

The range function has 3 arguments that can be passed to the function `range()`.  Those three arguments are integers that represent the initial value, the final value, and the step argument.  

````python
range(10) will provide a range of 0 to 9 by 1.  
range(0, 10) provide a range of 0 to 9 by 1. 
range(0, 10, 1) will provide a range of 0 to 10 by 1. 

for i in range(10)
    print(i)
````

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.  

````python
for i in range(10):
    print(str(i + 1))


n = 0
while n < 10:
    for n in range(10):
        print(str(n + 1))
    break 
````
