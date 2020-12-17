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
| Augmented Assignment Statement | Equivalent Assignment Statement |
|:-------------------------------|:--------------------------------|
| `spam += 1` | `spam = spam + 1 |
| `spam -= 1` | `spam = spam - 1 |
| `spam *= 1` | `spam = spam * 1 |
| `spam /= 1` | `spam = spam / 1 |
| `spam %= 1` | `spam = spam % 1 |  

THe `+=` operator can also do string and list concatenation and the `*=` operator can do string and list replication. 

## Methods
A *method* is the same thing as a function, ecept it is "called on" a value.  Example: a list value is stored in the variable `spam`, you would call the `index()` list method on that list like so, `spam.index('hello')`. 

### *Finding a Value in a List with the index() Method*
List values have an `index()` method that can be passed a value - and if that value exists in the list, the index of the value is returned. If the value isn't in the list, then Python produces a `ValueError`. 

````python
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list
````

When there are duplicates of the value in the list, the index of its first appearance is returned. 

### *Adding Values to Lists with the append() and insert() Methods*
`append()` and `insert()` methods are used to add new values to a list. 

````python 
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bat', 'moose']
````

The `append()` method adds the argument to the end of the list. The `insert()` method can insert a value at any index in the list. The first argument to `insert()` is the index for the new value, and the second argument is the new value to be inserted. 

````python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
````

Methods belong to a single data type.  In the above examples `append()` and `insert()` are methods of the list data type and can be only called on list values, not on other values such as strings or integers. 

````python
>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    bacon.insert(1, 'world')
AttributeError: 'int' object has no attribute 'insert'
````

### *Removing Values from Lists with the remove() Method*
The `remove()` method is passed the avlue to be removed from the list it is called on. 

````python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']
````

Attempting to delete a value that does not exist in the list will result in a `ValueError`. If the value appears more than once in the list, only the first instance of that value will be removed. 

**The `del` statement is good to use when you know the index of the value you want to remove from the list. The `remove()` method is useful when you know the value you want to remove from the list.**

### *Sorting the Values in a List with the sort() Method*
Lists of number values or lists of strings can be sorted with the `sort()` method. 

````python
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
````

You can pass `True` for the `reverse` keyword argument to have `sort()` sort the values in reverse order. Three things to note about the `sort()` method. 

1. The `sort()` method sorts the list in place. Don't try to capture the return value by writing code like `spam = spam.sort()`
2. You cannot sort lists that have both number values and strings. 
3. `sort()` usees "ASCIIbetical order" - that means that uppercase letters come before lowercase letters. The lowercase *a* is sorted *after* the uppercase *Z*. 

````python
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
````

If you need to sort the values in regular alphabetical order, pass `str.lower` for the `key` keyword argument in the `sort()` method call. 

````python
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
````

### *Reversing the Values in a List with the reverse() Method* 
To quickly reverse the order of the items in a list, you can call the `reverse()` list method. 

````python
>>> spam = ['cat', 'dog', 'moose']
>>> spam.reverse()
>>> spam
['moose', 'dog', 'cat']
````

Like `sort()`, the `reverse()` list method does not return a list. 

## Example Program: Magic 8 Ball with a List
See `magic_8_ball2.py`. 

## Sequence Data Types
Strings, like lists, are also represented by ordered sequences of values. A string, `'python'`, can be thought of as a "list" of single text characters. 

````python
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
...     print('* * * ' + i + ' * * *')

* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
````

### *Mutable and Immutable Data Types*
Lists and strings are different in an important way.   

**A list value is a *mutable* data type: it can have values added, removed, or changed.**  

**A string value is *immutable* data type: it cannot be changed.**  

Trying to reassign a signle value in a string will result in a `TypeError`.  The proper way to "mutate" a string is to use slicing and concatenation to build a *new* string by copying parts of the hold string. 

````python
>>> name = 'Zophie a cat'
>>> new_name = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> new_name
'Zophie the cat'
````

Mutable vs Immutable is an important distinction with calling functions with mutable arguments vs immutable arguments. 

### *The Tuple Data Type*
The *tuple* is typed with parentheses, `()`, instead of square brackets. It is almost identical to a list. 

````python
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs
('hello', 42, 0.5)
>>> eggs[0:2]
('hello', 42)
>>> eggs[0:3]
('hello', 42, 0.5)
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3
````

***Tuples* like strings, are immutable.**  Tuples cannot have their values modified, appended, or removed.  

````python
>>> eggs = ('hello', 42, 0.5)
>>> eggs[1] = 99
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    eggs[1] = 99
TypeError: 'tuple' object does not support item assignment
````

The `type()` function can be used to identify the data type of a value.  For the tuple data type, if you have only a single value in the tuple, you indicate that to Python by adding a trailing comma. 

````python
>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>
````

Tuples can be used to convey to readers of the code that you do not intend for the values in that sequence to change. If you need an ordered sequence of values that never changes, use a tuple. This can help in optimization of code. 

### *Converting Types with the list() and tuple() Functions*
The functions `list()` and `tuple()` will return a list and tuple of the values passed to them. 

````python
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
````

Notice the `()` and the `[]` in the above example.  Recall that tuples use `()` and lists use `[]`. Converting a tuple to a list is handy when you need a mutable version of a tuple value. 

## References
Variables are storing references to the computer memory locations where the values are stored. 

````python
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
````

When `42` is assigned to the variable `spam`, what is actaully taking place is that the value `42` is being stored in the computer's memory and storing a *reference* to it in the variable `spam`. When `cheese` is assigned to `spam`, cheese is actually being copied the referece of `spam` which was stored as the value `42`.  At this point, both `spam` and `cheese` reference the value `42`.  When spam is reassigned the value `100`, a new value of `100` is created as the reference to `spam` but the initial reference of `42` was assigned prior to the reassignment.  That is why when `spam` is executed, the value `100` is returned, and when `cheese` is executed a value of `42` is returned.

This doesn't affect the value in `cheese` = Integers are immutable.  

Lists don't work this way becuase lists are mutable. 

````python
>>> spam = [0,1,2,3,4,5]
>>> cheese = spam # The reference is being copied, not the list. 
>>> cheese[1] = 'Hello' # This changes the list value. 
>>> spam
[0, 'Hello', 2, 3, 4, 5]
>>> cheese # The cheese variable refers to the same list. 
[0, 'Hello', 2, 3, 4, 5]
````

`Line 1` when you create the list, you assign a reference to it in the `spam` variable. `Line 2` copies only the reference in `spam` to `cheese`, not the list value itself. This means that the value stored in `spam` and `cheese` now both refer to the same list. So when you modify the first element of `cheese`, you are modifying the smae list that `spam` refers to. 

The section in the book as good pictures to represent references. Python variables technically contain references. 

### *Identity and the id() Function*
All values in Python have a unique identiy that can be obtained with the `id()` function.  

````python
>>> id('Howdy')
2900643048944
````

`'Howdy'` is a string, therefore it is immutable.  This value is stored in memory with the address in bytes `2900643048944`. 

````python
>>> bacon = 'Hello'
>>> id(bacon)
2900643016240
>>> bacon += 'world!'
>>> id(bacon)
2900642320304
>>> bacon
'Helloworld!'
````

Lists can be modified because they are mutable.  The reference will remain the same but the list value will be changed. 

````python
>>> eggs = ['cat','dog']
>>> id(eggs)
2900643175168
>>> eggs.append('moose')
>>> id(eggs)
2900643175168
>>> eggs = ['bat', 'rat', 'cow']
>>> id(eggs)
2900643172736
````

If two variables refer to the same list, and the list value changes, both variables are affected because they both refer to the same list. The `append()`, `extend()`, `remove()`, `sort()`, `reverse()`, and other list methods modify their lists **in place**. 

### *Passing References*
References are important for understanding how arguments get passed to functions. When a function is called - the arguments are copied to the parameter variables. For lists - this means a copy of the reference is used for the parameter. 

### *The copy Modules copy() and deepcopy() Functions*
The `copy` module can be used to retain an original list or dictionary value if their of those values have been modified by a function. `copy.copy()` will make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference. 

````python
>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> id(spam)
2020709622272
>>> cheese = copy.copy(spam)
>>> id(cheese)
2020714764160
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']
````

If the list you need to copy contains lists, then use the `copy.deepcopy()` function instead of `copy.copy()`.  The `deepcopy()` function will copy the inner lsits as well. 