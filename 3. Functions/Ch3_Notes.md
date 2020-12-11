# Chapter 3 - Functions - Notes 
## *def* Statements with Parameters
The folling function `hello()` is defined below.  When a function is called - the lines following the `def` statement `hello()` - the program jumps back to where the function is defined and is excuted.

````python
def hello():
    print('Howdy')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()  
````  

When the above function `hello()` is called three times, it executes the function three times. 

When you call a function like `print()` or `len()`, you pass it arguments by writing values in the parentheses.  

`def` = defines a function.  This is a define statement. The code block following a `def` statement is the body of the function. The function is executed when it is called, not when it is defined. 

````python
def hello(name):
    print('Hello, ' + name)

hello('Kelsey')
hello('Finn')
````  

In the above program, I define the function `hello()` and pass it a parameter called `name`. *Parameters* are variables that contain arguments. When a function is called with an arguments, the arguments are stored as parameters. In the axample above, the first function call `hello('Kelsey')` is passed the argument `'Kelsey'`, the program execution enters the function, and the parameter `name` is automatically set to `Kelsey`, the argument passed in the call function. The program will then print `'Hello, Kelsey'` as the outut of the function that one function call.  

>The value stored as a parameter is forgotten when the function returns. 

## *Define, Call, Pass, Argument, Parameter*
````python
def say_hello(name):
    print('Hello, ' + name)
say_hello('Al')
````

To *define* a function is to create it. In the example above we define the function `say_hello()` with the `def` statement.  The line `say_hello('Al')` *calls* the defined function, sending the program execution to the top of the functions code. This function *call* is also known as *passing* the argument `'Al'` to the function. 

>The value being passed to a function in a *function call* is an argument. 

The argument `'Al'` is then assigned to the local variable `name`.  Variables that have arguments assigned to them are *parameters*. 