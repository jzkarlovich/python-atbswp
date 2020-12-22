1. Why are functions advantageous to have in your programs?   
Functions are advantageous becuase they can make use of local variables and return values that can then be executed on. You can execute a block of code over and over again without having to write it out explicitely. 

> functions reduce the need for duplicate code, making programs shorter, easeier to read, and easier to update. 

2. When does the code in a function execute: when the function is defined or when the function is called?  
When the function is called not when the function is first defined. 

3. What statement creates a function?  
A `def` statement. 

4. What is the difference between a function and a function call?  
A function is a code block that executes only when called. A function call executes a function code block. 

5. How many global scopes are there in a Python program? How many local scopes?  
There is only one global scope and it is created when the program begins. 

6. What happens to variables in a local scope when the function call returns?  
Varibables in a local scope are forgotten when a function call returns. 

7. What is a return value? Can a return value be part of an expression?  
A return value is an output of a function and it can be part of an expression. 

8. If a function does not have a return statement, what is the return value of a call to that function?  
If a function does not have a return statement, it returns a value `None`. 

9. How can you force a variable in a function to refer to the global variable?  
In a function you can refer to the global variable by using the keyword `global` preceeding the variable. 

10. What is the data type of `None`?  
data type of `None` = `NoneType`

11. What does the `import areallyourpetsnamederic` statement do?  
It imports a module named `areallyourpetsnamederic`. 

12. If you had a function named `bacon()` in a module named `spam`, how would you call it after importing `spam`?

````python
import spam

spam.bacon()
````

13. How can you prevent a program from crashing when it gets an error?  
You can use `try` and `except` clauses.

14. What goes in the `try` clause? What goes in the `except` clause?  
In a `try` clause, the function evaluates to a return value - if there is an error then it moves to the `except` clause.  After executing the `except` clause the program excutes as normal. 