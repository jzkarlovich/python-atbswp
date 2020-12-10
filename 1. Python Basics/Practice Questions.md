# Practice Questions

1. Which of the following are operators, and which are values?   
    `*` = operator  
    `'hello'` = value  
    `-88.8` = value  
    `-` = operator  
    `/` = operator  
    `+` = operator  
    `5` = value  

2. Which of the following is a variable, and which is a strign?     
    `spam` = variable  
    `'spam'` = string

3. Name three data types. 
    - Integers or *ints* = `int()`
    - Floating-point-numbers or *floats* = `float()`
    - Strings or *strs* = `str()`

4. What is and expression made up of?  What does an expression do?     
    An expression is made up of an input that evaluates to a single value output. 
    >Expressions consist of `values` and `operators` and can always *evaluate* down to a single value. 

5. This chapter introduced assignment statements, like `spam = 10`. What is the difference between an *expression* and a *statement*?   
    An expression can be evaluated while a *statement* assigns a value to a variable.  Assignment statements can be used and evaluated in expressions. 

6. What does the variable `bacon` contain after the following code runs? 
    >`bacon = 20`  
    >`bacon + 1`
  
    `bacon` contains the integer value = 20.  The expression `bacon + 1` evaluates to the integer value of `21`. 

7. What should the following two expressions evaluate to? 
    >`'spam' + 'spamspam'`  
    >`'spam' * 3`
  
    Line 1 evaluates to the string `'spamspamspam'`.  
    Line 2 evaluates to the string `'spamspamspam'`. 

8. Why is `eggs` a valid variable name while `100` in invalid?   
    Variable names cannot start with a number. `eggs` does not contain any invalid characters and does not start with a number. 

9. What three functions can be used to get the integer, floating-point-numner, or string version of a value?   
    The three functions that can be called are `int()`, `float()`, and `str()`. 

10. Why does expression cause an error? How can you fix it?   
    >`'I have eaten ' + 99 + ' burritos.'`

    The expression causes an error becuase it is not Python grammatically correct to concatenate a string with an integer value. In order to fix it you need to convert the `99` to a string value.   
    >`'I have eaten ' + str(99) + ' burritos.'`  
    Which would evaluate to to the string value, `I have eaten 99 burritos.`.

