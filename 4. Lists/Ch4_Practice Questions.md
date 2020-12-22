1. What is `[]`?
`[]` is used to denote a sequence of values - either lists or tuples. Tuples are immutable and lists are mutable. 

> `[]` is an empty list value that contains no items. This is similar to how `''` is the empty string value. 

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

````python
spam = [2,4,6,8,10]
spam[2] = 'hello'
print(spam)
````

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int(int('3' * 2) // 11)] evaluate to?

````python
spam = ['a', 'b', 'c', 'd']
spam[int(int('3' * 2) //11)]
````
Evaluates to `'d'`

4. What does spam[-1] evaluate to?  
`'d'`

5. What does spam[:2] evaluate to?  
`['a', 'b']"`

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?   
1

7. What does bacon.append(99) make the list value in bacon look like?  
[3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?  
[3.14, 'cat', 11, True]

9. What are the operators for list concatenation and list replication?  
List concatenation `+` and for list replication `*`

10. What is the difference between the append() and insert() list methods?  
The `append()` method adds the arguments to the end of the list, while the `insert()` method will insert the arguments at a specified location in a list value. 

11. What are two ways to remove values from a list?  
The `del` statement is good to use when you know the index of the value you want to remove from the list. The `remove()` method is useful when you know the value you want to remove from the list.

12. Name a few ways that list values are similar to string values.

13. What is the difference between lists and tuples?

14. How do you type the tuple value that has just the integer value 42 in it?

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

17. What is the difference between copy.copy() and copy.deepcopy()?