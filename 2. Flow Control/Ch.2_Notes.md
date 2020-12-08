# Chapter 2 - Flow Control - Notes 
## Boolean Values
There are only two Boolean values `True` and `False`.  They do not have '' quotes around them, the first letter `T` and `F` are always capitalized, and the rest of the characters are always lowercase.  
They are used in expressions and can be stored in variables. 

## Comparison Operators
***Comparison operators* or *relational operators* compare two values and evaluate to a single Boolean value**.  That is to say that they evaluate to `True` or `False` . There are six in total: 

|Operator | Meaning|
|:--------|:-------|
|  `==` | equal to |
| `!=` | not equal |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |

NOTE: `==` and `!=` can be used on values of any data type. 

## Boolean Operators
There are three Boolean operators used to compare Boolean values. The three operators are `and`, `or`, and `not`. 

### Binary Boolean Operators
The two binanry Boolean Operators are `and` and `or`.  This means that they always take two Boolean values (or expressions). 

The `and` operator evaluates the expression to be `True` if both Boolean values are `True`.  
The `and` Operator's Truth Table
| Expression | Evaluates to... |
|:---------|:----------------|
|`True and True` | `True`   |
|`True and False`| `False`  |
|`False and True`| `False`  |
|`False and False`| `False` |

The `or` operator evaluates to `True` if *either* of the two Boolean values is `True`.  
The `or` Operator's Truth Table
| Expression | Exvaluates to... |
|:-----------|:-----------------|
|`True and True` | `True`   |
|`True and False`| `True`  |
|`False and True`| `True`  |
|`False and False`| `False` |

### Unary Operator
The `not` operator only operates on one Boolean value.  It simple evaluates to the oposite Boolean value.  
The `not` Operator's Truth Table
| Expression | Exvaluates to... |
|:-----------|:-----------------|
|`not True` | `False`   |
|`not False`| `True`  |