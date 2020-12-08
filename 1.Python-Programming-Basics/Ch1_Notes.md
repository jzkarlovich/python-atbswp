# Chapter 1 - Python Basics - Notes
## Math Operators from Highest to Lowest Precedence
| Operator | Operation | Example | Evaluates to... |
|:---------|:----------|:--------|:----------------|
|**        |Exponent   |2**3     |8                |
|%         |Remainder  |22 % 8   |6                |
|//        |Integer Division/Floored Quotient|22 // 8| 2|
|/         |Division   |22 / 8   |2.75             |
|*         |Multiplication|3 * 5 |15               |
|-         |Subtraction|5 - 2    |3                |
|+         |Addition   |2 + 2    |4                |

Python evaluates each expression (see the examples in the table above) line by line and always evaluate down to a single value.  The *order of operations*, also called precedence, of Python is similar to that of mathematics. 

Parenthesis can be used to overide the precedence when needed. White space between operators does not matter in Python, but indentations at the start of a line DO matter. A signle space between operators is convention. 

## Data Types
There are three primary *data types* in Python. 

|**Data Type**  |**Examples**|
|:--------------|:-----------|
|Integers       |`-2, -1, 0, 1, 2, 3, 4, 5`  |
|Floats         |`-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25`|
|Strings        |`'a', 'aa', 'aaa', 'Hello!', '11 cats'`|

*Integers* or *ints* indicate values that are whole numbers. 

*Floating-point-numbers* or *floats* are numbers with a decimal point. 

*Strings* or *strs* are text values. '*strs*' are always surrounded by single quotes. For example, `'Hello world!'` or `'Goodbye cruel world!;`.  The text between the single quote represent the string data type in Python. 

NOTE: Error message: >`SyntaxError: EOL while scanning string literal`
Likely means there is a missing single quote character at the end of a string. 

## Variables
A *variable* can be used to store a single value. Variables are assigned through an *assignment statement*, which consists of a variable name, an equals sign, and the value to be stored. 

`spam = 42`

The variable `spam` now is equal to the integer value `42`. The variable is initialzied the first time it is created, and can then be overwritten with use. 

### Variable Names
A good variable name describes the data it contains.  Three rules for naming a variable: 
1. It can be only one word with no spaces. 
2. It can use only letters, numbers, and the underscore (_) character. 
3. It can't begin with a number.

|**Valid Variable Names**   |**Invalid Variable Names** |
|:--------------------------|:--------------------------|
|`current_balance`          |`current-balance` (no hyphens)|
|`currentBalance`           |`current balance` (no spaces)|
|`account4`                 |`4account` (can't begin with #)|
|`_42`                      |`42` (can't begin with #)|
|`TOTAL_SUM`                |`TOTAL_$UM` (no special characters)|
|`hello`                    |`'hello'` (no special characters)|

Variable names are case sensitive, meaning `spam`, `SPAM`, `Spam`, `SpAm`, and `SpaM` are all different and valid variable names. 

**Python convention is to start with variable names as lowercase**

## Functions used in hello.py Example
### Print()
`print()` = displays the string value in parenthesis on the screen. `print('Hello!')` in this example the string 'Hello!' in the parentesis is being passed to the *function* `print()`. 

When Python executes the `print()` function, it is said that Python is *calling* the `print()` function and the string value is being *passed* to the function. **A value that is passed to a function call is an *argument*.**

When the function `print()` is called with no argument passed, a blank line is the output. 

### Input()
`input()` = this function call waits for input from the user from a keybaord.  The `input()` function call evaluates to a string equal to the user's text. 


### Len()
`len()` = When you pass a string to the `len()` function, it evaluates to an integer value of the number of characters in that string. 

**Example**
Assigment:  `myName = 'zach'`
Expression: `len(myName)`
Evaluates:  `4`

The argument, in this case a variable named `myName` is passed to the function `len()`.  When the `len()` function is called with the argument `myName` it evaluates to the integer value of `4` which is the number of characters. 

### Data Type Functions int(), str(), float()
`int()`

`str()`

`float()`
