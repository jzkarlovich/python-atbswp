# Chapter 4 - Lists - Notes
## The List Data Type
A *list* is a value that contains multiple values in an ordered sequence. The term *list value* refers to the list itself (which is a value that can be stored in a variable or passed to a function like any other value), not the values inside the list value. A list value looks like:

> `['cat', 'bat', 'rat', 'elephant']`

A list begins with an opening square bracket and ends with a closing square bracket `[]`.  Values insdie the list are also called *items*.  Items are seperated with commas (comma-delimited). 

````python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
````

In the example above, the variable `spam` is still only asigned to one value, and that is a list value, containing the items (or values) `['cat', 'bat', 'rat', 'elephant']`.   

The value `[]` is an empty list value.  Similar to an epmty string value `''`.  The first index value is always `[0]`.

### *Getting Individual Values in a List with Indexes*
An index can pull a single value from a list.  The index always starts with the value 0 --> that is the first item in the list. 

<p align="center">
    <img src="index_example.jpg" />
</p> 

Indexes can only be integers, not floats. A `TypeError` will be generated if that is the case. Lists can also contain other list values.  

````python
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
````

The first index dictates which list value to use, the second indicates the value within the list value. 

### *Negative Indexes*
While indexes start at 0 and go up, you can also use negative integers for the index.  The integer value `-1` refers to the last index in a list value, the value `-2` refers to the second to last index in a list.

````python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'The elephant is afraid of the bat.'
````  

### *Getting a List from Another List with Slices*
- spam[2] is a list with an index (one integer).
- spam[1:4] is a list with a slice (two integers).

A slice evaluates to a new list value. You can leave out one or both of the indexes o neither side of the colon in the slice. Leaving out the first index is the same as using 0, or the beginning of the list, leaving out the second index is the same as using the length of the list - which will slice to the end of the list. 

````python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']
````

### *Getting a List's Length with the len() Function*
The `len()` function will return the number of values that ar ein a list value passed to it. 

````python
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
````

### *Changing Values in a List with Indexes*
You can use an index of a list to change the value at that index. `spam[1] = 'aardvark'` means "Assign the value at index 1 in the list `spam` to the string `'aardvark'`. 

````python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]
````

### *List Concatenation and List Replication
Lists can be concatenated and replicated just like strings. The `+` operator combines two lists to create a new list value and the `*` operator can be used with a list and an integer value to replicate the list.

````python
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']
````

It always evaluates to a new list value. + is concatenate, * is replicate. 

### *Removing Values from Lists with del Statements* 
`del` statement will delete values at an index in a list. All of the values in the list after the deleted value will be moved up one index. 

````python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']
````
The `del` statement can also be used on variables. 

## Working with Lists
Good to work with lists instead of multiple repetitive variables.  See exmaple code in all_my_cats_1.py and all_my_cats_2.py. 

### *Using for Loops with Lists*
`for` loops execute a block of code a certain number of times. A `for` loop repeats the code block once for each item in a list value. 

````python
for i in range(4):
    print(i)
````

`range(4)` is a sequence value that Python considers similar to [0,1,2,3]. 

````python
for i in [0,1,2,3]:
    print(i)
````
**COMMON PYTHON TECHNIQUE** = use `range(len(*some_list*))` with a `for` loop to iterate over the indexes of a list. Example:

````python
>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
>>> for i in range(len(supplies)):
...     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
````

### *The in and not in Operators*
The `in` and `not in` operators can be used to determine whether a value is in a list or not. `in` and `not in` are used in expressions and connect two values: a value to look for in a list and the list where it may be found. These expressions will evaluate to a **Boolean** value. 

````python
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
````

### *The Multiple Assignment Trick*
The *multiple assignment trick* (technically *tuple unpacking*) lets you assign multiple variables with the values in a list in one line of code. 

Example:
````python
>>> cat = ['fat', 'gray', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
````
*Multiple Assignment Trick Example:*
````python
>>> cat = ['fat', 'gray', 'loud']
>>> size, color, disposition = cat
````

The number of variables and the length of the list must be exactly equal or you will get a `ValueError`. 

### *Using the enumerate() Function with Lists*
Instead of using the trick `range(len(*some_list*))` with a `for` loop to obtain the integer index of the imtes in the list, you can call the `enumerate()` function instead. `enumerate() will return two values: the index of the item in the list and the item  in the list itself. 

````python
>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
>>> for index, item in enumerate(supplies):
...     print('Index ' + str(index) + ' in supplies is: ' + item)

Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
````
### *Using the random.choice() and the random.shuffle() Functions with Lists*
`random.choice()` function will return a redomly selected item from the list.   
`random.shuffle()` function will reorder the items in a list. This function modifies the list in place rather than returning a new list. 

## Augmented Assignment Operators