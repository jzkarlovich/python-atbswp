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

## Return Values and Return Statements
When you call the `len()` function and pass it an argument such as 'Hello', the function call evaluates to the integer value `5`, which is the length of the string you passed it. 

*return value* = the value that a function call evaluates to.  

A `return` statement consists of the following: 

1. The `return` keyword. 
2. The value or expression that the function should return. 

## The None Value
`None` is a value which represents the abscence of a value. The `None` value is the only value of the `NoneType` data type. This value-without-a-value can be helpful when you need to store something that won't be confused for a real value in a variable.  One where `None` is used is as the return value of print().

````python
>>> spam = print('Hello!')
Hello!
>>> None == spam
True
````

## Keyword Arguments and the *print()* Function
Most arguments are identified by their position in the function call. For example, `random.randint(1,10)` is different than `random.randint(10,1)`.  The first argument is the low end and the second argument is the high end.  

*keyword arguments* are identified by the keyword put before them in the function call. Keyword arguments are often used for optional parameters. Review examples...

> Some functions have optional keyword arguments that can be specified when the function is called. 

## The Call Stack
The current topic is always at the top of the stack. **Function calls always return to the line mumber they were called from.**

## Local and Global Scope
- *local scope* = parameters and variables that are assigned in a called function
- *global scope* = variables assigned outside all functions  

*Scope* can be through of as a container of variables. When a scope is destroyed, all of teh values stored in the scope's variables are forgotten.  There is only one global scope, and it is created when the program begins. When the program terminates, the global scope is destroyed. 

The *local scope* is created whenever a function is called. Any variables assigned in the function exist within the function's local scope. When the function returns, the local scope is destroyed and the variables are forgotten. Scope's matter for several reasons: 

- Code in the global scope, outside of all functions, cannot use any local variables. 
- However, code in a local scope can access global variables. 
- Code in a function's local scope cannot use variables in any other local scope. 
- You can use the same name for different variables if they are in different scopes. That is there can be a local variables named `spam` and a global variable named `spam`. 

It is a bad habbit to rely on global variables as programs get larger and larger. 

### *Local Variables Cannot be used in the Global Scopes

### *Local Scopes Cannot use Variables in Other Local Scopes*

### *Global Variables Can Be Read from a Local Scope*

## The Global Satement
`global eggs` means that within a function, it refers to the global variable `eggs`.   

**4 Rules to tell whether a variable is in a local scope or a global scope:**
1. If a variable is being used in the global scope (that is, outside of the functions), then it is always a global variable. 
2. If there is a `global` statement for that variable in a function, it is a global variable. 
3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable. 
4. But, if the variable is not used in an assignment statement, it is a global variable. 

## Exception Handling
Getting an *exception* is an error.  Errors can be handled with `try` and `except` clauses.