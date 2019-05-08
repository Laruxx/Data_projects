# You can use the # symbol to comment your Python code

''' Another way to comment your Python code is to use
a multiline string that is opened and closed with three single or double quotation marks
'''

"""
this is also a comment"""

####################
### INSTALLATION ###
####################

# 5 MINUTES

# Install the latest version of Python using Anaconda from https://www.anaconda.com/distribution/#download-section
# After installing, using the Start Menu open either iPython or Anaconda Prompt from the Anaconda app
# If using the Anaconda Prompt, type "ipython" and hit ENTER to launch the iPython shell
# The iPython shell will display "In [#]:" when a command is entered and "Out[#]:" when displaying the output of a command

# FULL PYTHON INSTALLATION INSTRUCTIONS CAN BE FOUND IN APPENDIX

#################
### LIBRARIES ###
#################

# 5 MINUTES

# Libraries can be imported into a Python file session using the "import" command

In [22]: import math

# To see some of the documentation associated with an imported library, use the help(library) function
# Scrolling through the output of help(math) using the Enter key, we see "ceil" is a function inside of math
# There can be a significant amount of help output; to get through it quickly use CTRL+C (this stops what is currently processing in Python; CTRL+D exits iPython shell)
# *** CTRL+C is very useful! Don't forget about it! ***

In [23]: ceil(1/2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-23-864ea98b5f8d> in <module>()
----> 1 ceil(1/2)

NameError: name 'ceil' is not defined

# When calling specific functions from a library, it's necessary to preceed the function with the library's name

In [24]: math.ceil(1/2)
Out[24]: 1

# Alternatively, to avoid having to preceed every function, import the function directly from the library

In [25]: from math import ceil

In [26]: ceil(1/2)
Out[26]: 1

# Alternatively, create a shortcut by aliasing a library's name, just be careful to not use an alias you will need later on

In [27]: import math as m

In [28]: m.ceil(1/2)
Out[28]: 1

#################
### SECTION 1 ###
#################

# 80 MINUTES

# The primitive classes / data types in Python include Integers, Floats, Strings, Booleans

# It's easy to declare variables and assign values to them with the "=" operator, which will establish their Types
# Types are dynamic in Python, meaning it's possible to change a variable's type repeatedly

In [1]: x = 25

In [2]: type(x)
Out[2]: int

In [3]: x = str(25)

In [4]: type(x)
Out[4]: str

In [5]: float(x)  # re-cast a string as a float
Out[5]: 25.0

In [1]: z = 1.313

In [2]: type(z)
Out[2]: float

In [3]: y = 'global insights is awesome'

In [4]: type(y)
Out[4]: str

In [42]: print(y)
global insights is awesome

# You can print multiple items using a single print statement
# You can also print new lines using the newline character "\n"

In [47]: print(y, x)
global insights is awesome 25

In [53]: print(y, '\n', 'and so are you!')
global insights is awesome
 and so are you!

In [10]: y + x  # you cannot add strings and integers
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-adce3e2171e0> in <module>()
----> 1 y + x

TypeError: must be str, not int

In [11]: y*x  # but you can "multiply" strings by integers to create longer concatenated strings
Out[11]: 'global insights is awesomeglobal insights is awesomeglobal insights is awesomeglobal insights is awesome...'  # note '...' is not actually printed

In [5]: x == y   # you can perform boolean comparisons using operators such as ==, =!, >=, <=
Out[5]: False  # Note Python True and False are title cased

In [45]: x != y
Out[45]: True

In [1]: x = True

In [2]: x
Out[2]: True

In [3]: x == False  # notice the difference between the assignment operator "=" and the equality comparison operator "=="
Out[3]: False

In [4]: type(x)
Out[4]: bool

In [5]: print('123', x)
123 True

# Python's primitive types also include collection objects -- Lists, Tuples, Dictionaries, which can be declared in different ways

In [42]: x = list()

In [46]: type(x)
Out[46]: list

In [1]: x = []  # square brackets

In [2]: type(x)
Out[2]: list

In [43]: y = tuple()

In [47]: type(y)
Out[47]: tuple

In [3]: y = ()  # parentheses

In [4]: type(y)
Out[4]: tuple

In [44]: z = dict()

In [48]: type(z)
Out[48]: dict

In [5]: z = {}  # curly braces

In [6]: type(z)
Out[6]: dict

# Lists and Tuples are examples of ordered collection objects, while Dictionaries are not ordered
# You can access an ordered collection object's items using an index operator, formatted as object[index]... Python index always begin with 0!

In [6]: list_x = [1, 2, 3, 4]

In [7]: list_x
Out[7]: [1, 2, 3, 4]

In [4]: list_x[0]
Out[4]: 1

In [5]: list_x[1]
Out[5]: 2

In [6]: list_x[-1]  # negative indices start from the end, -1 is the last element in the List
Out[6]: 4

In [7]: list_x[0:2]  # slice a list using list[index1:index2] ... IMPORTANT this will return all items UP TO BUT NOT INCLUDING the item at the end of the slice range!
Out[7]: [1, 2]

In [14]: len(list_x)
Out[14]: 4

In [13]: list_x[0:len(list_x)]
Out[13]: [1, 2, 3, 4]

In [8]: list_x[0:-1]
Out[8]: [1, 2, 3]

In [9]: list_x[:-1]  # leaving the indices blank on either side of the colon means to start from the beginning or go to the end
Out[9]: [1, 2, 3]

In [11]: list_x[1:]
Out[11]: [2, 3, 4]

# List can include items of multiple types

In [74]: random_list = ['hello!', 'HELLO!', 0, [2, 3]]

In [75]: random_list
Out[75]: ['hello!', 'HELLO!', 0, [2, 3]]

# random_list is a list of strings (Sir Annoy-O says hello! HELLO!), an integer, and a List of integers

# Items in a list can be replaced; for this reason a list is called a "mutable" object (think "mutation" ... complete)

In [14]: random_list[3] = (8,9,10)  # this replaces the 4th item in the list (the list [2,3]) with a tuple (8, 9, 10)

In [15]: random_list
Out[15]: ['hello!', 'HELLO!', 0, (8, 9, 10)]

# Unlike lists, however, tuples are NOT mutable (they cannot be changed after instantiation)

In [19]: tuple_x = (1,2,3)

In [20]: tuple_x[0]
Out[20]: 1

In [21]: tuple_x[0] = 11
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-622e4f267299> in <module>()
----> 1 tuple_x[0] = 11

TypeError: 'tuple' object does not support item assignment

# It's easy to change between types

In [93]: type(tuple_x)
Out[93]: tuple

In [94]: list_x = list(tuple_x)

In [96]: type(list_x)
Out[96]: list

In [21]: list_x[0] = 11
In [95]: list_x
Out[95]: [11, 2, 3]

# The values of a list or tuple can be unpacked using the "multiple assignment" shortcut

In [22]: a, b = 2+3, 10

In [23]: a
Out[23]: 5

In [24]: b
Out[24]: 10

In [15]: random_list = ['hello!', 'HELLO!', 0, (8, 9, 10)]

In [17]: a,b,c,d = random_list

In [18]: a
Out[18]: 'hello!'

In [19]: b
Out[19]: 'HELLO!'

In [20]: c
Out[20]: 0

In [21]: d
Out[21]: (8, 9, 10)

In [16]: a, b, c = random_list  # make sure to unpack all the values of the list
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-16-8ead02d17252> in <module>()
----> 1 a, b, c = random_list

ValueError: too many values to unpack (expected 3)

# The last collection object type to mention is the Dictionary
# Dictionaries are NOT ordered but support a different type of "indexing" (similar to keys in a SQL table)

In [10]: dict_y = {'roland':'male', 'jennifer':'female'}

In [14]: dict_y['roland']
Out[14]: 'male'

In [155]: dict_y['lucky'] = 'dog'

In [156]: dict_y
Out[156]: {'roland': 'male', 'jennifer': 'female', 'lucky': 'dog'}

In [58]: dict_y[0]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-58-9f03f94768f3> in <module>()
----> 1 dict_y[0]

KeyError: 0

# Each type/class has a set of functions called METHODS that operate specifically on that object type

# List methods

In [37]: list_x = [1,2,3,4]

In [18]: list_x.append(5)  # concatenates an item to the end of the list

In [19]: list_x
Out[19]: [1, 2, 3, 4, 5]

In [20]: list_x.remove(5)  # removes the first occurrence of an item

In [21]: list_x
Out[21]: [1, 2, 3, 4]

In [43]: list_x.append([5,6,7,8])

In [44]: list_x
Out[44]: [1, 2, 3, 4, [5, 6, 7, 8]]

In [37]: list_x = [1,2,3,4]

In [25]: list_x.extend(list_x)  # extends the list with the items in another list; NOTE the difference between extend() and append()!

In [26]: list_x
Out[26]: [1, 2, 3, 4, 1, 2, 3, 4]

In [37]: list_x = [1,2,3,4]

In [23]: list_x.pop()  # .pop(x) removes the item at the index passed to the method (no argument defaults to last item)
Out[23]: 4

In [24]: list_x
Out[24]: [1, 2, 3]

In [45]: list_x = [1,2,3,1,2,3]

In [27]: list_x.count(1)  # counts occurrences of items in a list
Out[27]: 2

In [28]: list_x.sort()

In [29]: list_x
Out[29]: [1, 1, 2, 2, 3, 3]

In [30]: list_x.reverse()

In [31]: list_x
Out[31]: [3, 3, 2, 2, 1, 1]

In [36]: list_x.insert(1,5)  # insert(x,y) inserts value y at index x, and increments all other items to the next index

In [37]: list_x
Out[37]: [3, 5, 3, 2, 2, 1, 1]

# Use the set() operator to remove duplicate items from a list

In [91]: list(set(list_x))
Out[91]: [1, 2, 3, 5]

# Lists are useful for flow control when iterating through FOR LOOPS

In [37]: list_x = [1,2,3,4]

In [8]: for item in list_x:     # a list is an example of an "iterable"; aliases such as "item" can be used to track steps in the for loop
   ...:     print(item)         # Python uses an indentation scheme (4 spaces) for flow control... not indenting correctly will generate errors!
   ...:
1
2
3
4

In [12]: for item in list_x:
    ...: print(item)
  File "<ipython-input-12-a8065a013cab>", line 2
    print(item)
        ^
IndentationError: expected an indented block

# IF-THEN statements and loops can be easily nested using indentation

In [39]: list_x = [1,2,3,4]
    ...: for itemXXX in list_x:  # this alias scheme is directly assigning elements from the list to itemXXX
    ...:     if itemXXX >= 2 and itemXXX % 3 == 0:  # % is remainder division; the only item in list_x satsifying these conditions is 3
    ...:         for rand0 in [9,7,4]:
    ...:             print(itemXXX+rand0)
    ...:
12
10
7

# Range objects created based on lists lengths can be used to assign index values to aliases, which can then be used to reference values from the list using list[alias]

In [12]: range(10)
Out[12]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [13]: range(3,6)
Out[13]: [3, 4, 5]

In [59]: for qqq in range(len(list_x)):
    ...:     print(qqq, list_x[qqq])
    ...:
0 1
1 2
2 3
3 4

# String Interpolation involves passing arguments to placeholders in a string
# String Interp method 1 uses curly braces {index} indexing and the string .format() method to pass arguments to their relative placeholders

In [50]: print('Hello my name is {0}... I, {0}, have a dog named {1}.'.format('Roland', 'Lucky'))
Hello my name is Roland... I, Roland, have a dog named Lucky.

# String Interp method 2 uses %s as placeholder and % after the string instead of the .format() method
# The disadvantage of method 2 is that it does not map single arguments to multiple placeholders
# In other words, String Interp method 2 requires each placeholder to have an explicit argument passed to it

In [51]: print('Hello my name is %s... I, %s, have a dog named %s.' % ('Roland','Roland','Lucky'))
Hello my name is Roland... I, Roland, have a dog named Lucky.

# Using String Interp it's possible to modify the contents of the string within a loop and print the changing string

In [60]: for index in range(len(list_x)):
    ...:     print('The item at index {0} is {1}'.format(index, list_x[index]))
    ...:
The item at index 0 is 1
The item at index 1 is 2
The item at index 2 is 3
The item at index 3 is 4

# This can be very useful when debugging and tracking steps during program execution
# CAUTION: Do not alter the iterable as you are iterating through it! Python's internal indexing scheme may get thrown off, leading to unexpected behavior!

In [9]: for item in list_x:
   ...:     list_x.remove(item)
   ...:     print(list_x)
   ...:
[2, 3, 4]
[2, 4]

# In the first iteration, Python searches for index 0 in the list [1,2,3,4], finds 1, and removes it, leaving [2,3,4]
# In the next iteration, Python searches for index 1 in the list [2,3,4], finds 3, and removes it, leaving [2,4]
# In the next iteration, Python searches for index 2 in the list [2,4], finds no such index, and exits the loop

# If you need to change a list, it's generally a better idea to work with copies or clones of the list
# CAUTION: new_list = old_list will NOT create a clone of the list!
# Instead it will just create a VIEW of the original list, and operating on the "new list" will similarly operate on the original list!

In [63]: list_x_false_clone = list_x

In [64]: list_x_false_clone
Out[64]: [1, 2, 3, 4]

In [65]: list_x_false_clone.pop()
Out[65]: 4

In [66]: list_x  # list_x was affected by operating on list_x_false_clone, which is just a view of list_x
Out[66]: [1, 2, 3]

In [37]: list_x = [1,2,3,4]

In [61]: list_x_correct_clone = list_x[:]  # [:] is the list clone syntax

In [62]: list_x_correct_clone
Out[62]: [1, 2, 3, 4]

In [70]: for item in list_x:
    ...:     list_x_correct_clone.remove(item)
    ...:     print(list_x_correct_clone)
    ...:
[2, 3, 4]
[3, 4]
[4]
[]

In [50]: list_x_correct_clone
Out[50]: []

In [49]: list_x  # list_x_correct_clone is empty and list_x is unaffected
Out[49]: [1, 2, 3, 4]

# It is sometimes preferable to alter a list using the indexing approach instead of the item assignment approach

In [61]: list_x_correct_clone = list_x[:]

In [82]: for indexHAHA in range(len(list_x)):  # South Sea Deckhand, anyone?
    ...:     list_x_clone.remove(list_x[indexHAHA])
    ...:     print(list_x_clone)
    ...:
[2, 3, 4]
[3, 4]
[4]
[]

# Loops are also useful for accumulating output into a new list

In [16]: list_x_sq = []

In [104]: for i in range(len(list_x)):
     ...:     list_x_sq.append(list_x[i]**2)  # Python uses ** for exponentiation
     ...:     print(list_x_sq)
     ...:
[1]
[1, 4]
[1, 4, 9]
[1, 4, 9, 16]

In [112]: list_x_sq_strs = []

In [113]: for i in range(len(list_x)):
     ...:     list_x_sq_strs.append('The value of {0} squared is {1}!'.format(list_x[i], list_x[i]**2))
     ...: print(list_x_sq_strs)
['The value of 1 squared is 1!', 'The value of 2 squared is 4!', 'The value of 3 squared is 9!', 'The value of 4 squared is 16!']

# Note the print statement above is not indented so it only prints once after the loop has finished

# Loops can be exited from after meeting a specific condition (this can help improve average program runtime)
# This can be done using the "break" keyword, which will exit out of the CURRENT loop

In [100]: counter = 0
     ...: for item in range(len(list_x)):
     ...:     counter += 1  # using += is a shortcut for counter = counter + 1
     ...:     if list_x[item] <= 2:
     ...:         continue  # the continue keyword sends you directly to the next iteration of the current loop
     ...:     else:
     ...:         break
     ...: print('Number of times passing through loop: {}'.format(counter))
Number of times passing through loop: 3

# In the example above, counter increments when item = 1, 2, 3, and then exits the loop when item = 3

In [101]: counter = 0
     ...: for item in range(len(list_x)):
     ...:     if list_x[item] <= 2:
     ...:         pass  # the pass keyword exits the if-then statement and continues with the current loop iteration
     ...:     else:
     ...:         break
     ...:     counter += 1
     ...: print('Number of times passing through loop: {}'.format(counter))
Number of times passing through loop: 2

# In the example above, counter increments when item = 1, 2, and then exits the loop when item = 3
# Although the loop iterated 3 times, counter was only incremented twice with the use of break

In [102]: counter = 0
     ...: for item in range(len(list_x)):
     ...:     if list_x[item] <= 2:
     ...:         continue
     ...:     else:
     ...:         break
     ...:     counter += 1
     ...: print('Number of times passing through loop: {}'.format(counter))
Number of times passing through loop: 0

# In the example above, counter never increments because the loop moves to the next loop iteration when item = 1,2 and exits the loop when item = 3

# NOTE: if you break out of an inner loop within an outer loop, the outer loop will continue to the next iteration and may re-enter the inner loop!
# There are other flow control strategies you should consider, such as breaking using if-then statements while outside the current loop based on variables meeting certain conditions inside the current loop
# For more reference, see https://docs.python.org/3/tutorial/controlflow.html

In [120]: list_of_lists = [[1,2,3], [5,6,7], [8,9,10]]
     ...: breaker = 0
     ...: for x in range(len(list_of_lists)):  # length 3
     ...:     list_sum = 0  # reset the list sum when moving to a new list in list_of_lists
     ...:     for y in range(len(list_of_lists[x])):  # also length 3
     ...:         print(list_of_lists[x][y])  # print the current item in the list within list_of_lists
     ...:         list_sum += list_of_lists[x][y]
     ...:         if list_sum > 10:  # if the running sum in the list within list_of_lists > 10, set breaker to 1
     ...:             breaker = 1
     ...:     if breaker == 1:  # after running through the current list within list_of_lists, test value of breaker to break or not from the outer-most for loop
     ...:         break
     ...:
1
2
3
5
6
7

# In the example above, even though list_sum > 10 after 5,6 in [5,6,7], the break does not occur until after the entire inner loop finishes

# Instead of using a for loop with an iterable, WHILE loops check the truth of a CONDITION on every iteration. If true, re-enter the loop, if false, exit the loop
# Below is an example of a while loop that does NOT result in output

In [125]: for i in range(len(list_x)):
     ...:     while list_x[i] <= 2:
     ...:         list_x_sq_strs.append('The value of {0} squared is {1}!'.format(list_x[i], list_x[i]**2))
     ...: print(list_x_sq_strs)

# There is no output because the while loop never exits
# Instead it gets stuck at i=0 (when list_x[0] is 1) because i does not change inside the while loop (so list_x[i] <= 2 is ALWAYS True) and continues forever
# To break out of a while loop use a value that gets tested at each iteration and incremented or changed from inside the loop

In [143]: counter = 0
     ...: list_x_sq_strs = []
     ...: while list_x[counter] <= 2:
     ...:         list_x_sq_strs.append('The value of {0} squared is {1}!'.format(list_x[counter], list_x[counter]**2))
     ...:         counter += 1
     ...: print(list_x_sq_strs)
['The value of 1 squared is 1!', 'The value of 2 squared is 4!']

# Using a while loop with breaks can also be effective

In [69]: list_x_sq_strs = []
    ...: counter = 0
    ...:
    ...: while True:  # this loop condition is set to always be True, and so it will continue forever until there is a break from within
    ...:     if list_x[counter] <= 2:
    ...:         list_x_sq_strs.append('The value of {0} squared is {1}!'.format(list_x[counter], list_x[counter]**2))
    ...:     else:
    ...:         break
    ...:     counter += 1
    ...: print(list_x_sq_strs)
    ...: print('Number of times passing through loop: {}'.format(counter))
['The value of 1 squared is 1!', 'The value of 2 squared is 4!']
Number of times passing through loop: 2

In [69]: list_x_sq_strs = []
    ...: counter = 0
    ...: breaker = 0
    ...:
    ...: while breaker == 0:
    ...:     if list_x[counter] <= 2:
    ...:         list_x_sq_strs.append('The value of {0} squared is {1}!'.format(list_x[counter], list_x[counter]**2))
    ...:     else:
    ...:         breaker = 1
    ...:     counter += 1
    ...: print(list_x_sq_strs)
    ...: print('Number of times passing through loop: {}'.format(counter))
['The value of 1 squared is 1!', 'The value of 2 squared is 4!']
Number of times passing through loop: 3

# There is a difference between the two implementations above 
# The first immediately breaks out of the while loop during the if-then statement
# The second waits until the current iteration of the loop finishes (incrementing counter by 1) and then exists the loop after testing the value of breaker at the while loop

# Here's an example of a loop that will produce an error

In [154]: list_x = [1,2,3,4]

In [155]: list_y = [1,2,3,4,5]

In [157]: for index in range(len(list_y)):
     ...:     print(list_x[index] + list_y[index])
2
4
6
8
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-157-d5a388fcd7ac> in <module>()
      1 for index in range(len(list_y)):
----> 2     print(list_x[index] + list_y[index])

IndexError: list index out of range

# An error occurs because the iteration count is built using list_y's index and there was no corresponding list_x[4]
# The TRY and EXCEPT keywords can be used to tell Python what to do when an error occurs 

In [158]: for index in range(len(list_y)):
     ...:     try:
     ...:         print(list_x[index] + list_y[index])
     ...:     except:
     ...:         print('Something went wrong!') 
     ...:         pass
     ...:
2
4
6
8
Something went wrong!

# Lists can be built with for loops using list comprehensions, which can offer readability and performance benefits

In [159]: [x**2 for x in list_x]
Out[159]: [1, 4, 9, 16]

In [160]: [x**2 for x in list_x if x <= 2]
Out[160]: [1, 4]

# List comprehensions are read left to right: "for x in list_x: if x <= 2: append x**2 to the list"

# Python Functions take input arguments and returns outputs. The "def" keyword is used to define a function

In [161]: def RolandsFunc(x,y):
     ...:     print('Processing multiplication with values {0} and {1}'.format(x,y))
     ...:     return x*y

# NOTE a function will finish after a return statement; the return statement should thus be used at the end of the function (after any print statements, etc)

In [162]: value = RolandsFunc(2,3)
Processing multiplication with values 2 and 3

In [163]: value
Out[163]: 6

In [86]: type(RolandsFunc)  # functions have their own data type
Out[86]: function

In [87]: LuckysFunc = RolandsFunc  # you can assign functions to other variables

In [88]: LuckysFunc(2,3)
Out[88]: 6

# This session will not cover global vs. local variable scope, but by default any variables not passed into the function cannot be accessed from inside it
# Likewise, any variables defined inside the function cannot be accessed from outside it

# Functions can have default values for arguments that aren't necessary to provide, which is standard when functions can take many arguments or have multiple settings
# Default values must always appear last in the function arguments

In [164]: def powerfunc(x,n):  # no default values
     ...:     return x**n

In [165]: powerfunc(2,3)
Out[165]: 8

In [170]: def powerfunc(x,n=2):  # here n defaults to 2 if omitted
     ...:     return x**n

In [171]: powerfunc(2)
Out[171]: 4

# Functional programming often uses recursion (functions calling themselves inside the function)

In [185]: def factorial(x):
     ...:     if x >= 1:
     ...:         return x*factorial(x-1)
     ...:     else:
     ...:         return 1  # recursive calls must have a terminal condition in order to be evaluated

In [186]: factorial(4)
Out[186]: 24

In [37]: list_x = [1,2,3,4]

In [61]: def sum_sq(list_x):
    ...:     if len(list_x) > 1:
    ...:         return list_x[0]**2 + sum_sq(list_x[1:])
    ...:     elif len(list_x) == 1:
    ...:         return list_x[0]**2

In [62]: sum_sq(list_x)
Out[62]: 30

# Note this could have also been accomplished using for loops... there are generally many ways to accomplish the same result in Python

# Anonymous functions use lambda notation as a shortcut for building functions -- also refered to as "synctactic sugar"
# Think of this as using shorthand to create an f(x) on the spot which does not need to be preserved in memory after it is used

In [64]: (lambda x: x**2)(2)  # (lambda x: x**s) plays the role of f, translating to f(2)
Out[64]: 4

# Lambdas can be used to easily pass functions as arguments to other functions

In [37]: list_x = [1,2,3,4]

In [71]: def sum_f(list_x,f):
    ...:     if len(list_x) > 1:
    ...:         return f(list_x[0]) + sum_f(list_x[1:],f)
    ...:     elif len(list_x) == 1:
    ...:         return f(list_x[0])

In [73]: sum_power(list_x,lambda x: x**3)
Out[73]: 100

# There are some additional list methods: map, filter, reduce, that can be applied very quickly using lambdas; of these MAP is probably the most useful

# Map applies a function to every item in a list (assuming it is possible to do so) and returns a "map object" that can be converted into a list

In [83]: list_x
Out[83]: [1, 2, 3, 4]

In [84]: list(map(lambda s: s**2, list_x))
Out[84]: [1, 4, 9, 16]

# Filter returns a list items for which the function application evaluates to TRUE

In [86]: list(filter(lambda s: s%2 == 0, list_x))
Out[86]: [2, 4]

# Reduce applies a function to a sequence of list items and aggregates using a rolling computation 

In [98]: product = reduce(lambda s,z: s*z, list_x)

In [99]: product
Out[99]: 24

# product is the evaluation of ((list_x[0]*list_x[1])*list_x[2])*list_x[3]

# Lastly, functions can include comments or docstrings with important information and can be referenced using the help(function) command

In [125]: def new_func(x):
     ...:     ''' this is the docstring '''
     ...:     return x

In [126]: help(new_func)
Help on function new_func in module __main__:

new_func(x)
    this is the docstring

##########################
### SECTION 1 EXERCISE ###
##########################

# 30 MINUTES

(1) Write a Python function called connect_db that accepts one argument with default value 'td'
    The function should have the following properties:
    - A docstring that contains the text 'This is the docstring for connect_db'
    - If the argument passed to the function is 'td', return an object with two variables packed into it, con and cur, with values 'td_con' and 'td_cur'
    - If the argument passed to the function is 'hive', return an object with two variables packed into it, con and cur, with values 'hive_con' and 'hive_cur'
    - A print statement that displays 'Connection to [DATABASE] Successful!', depending on which argument was passed to the connection
    - Test the function with "connect_db('hive')" and "connect_db()"


(2) Write a Python function called join_str_args that accepts two arguments (both of these arguments will be lists)
    The function should have the following properties
    - Takes two list of integers (e.g. [1,2,3,4] and [5,6,7,8,9]) and uses the map() function to create 2 new lists of strings (e.g. ['1','2','3','4'], ['5','6','7','8','9'])
    - Loops over an iterable with length of the longest of the two lists and returns a new combined list str_list that looks like ['1 5','2 6','3 7',...] (hint: use String Interpolation)
    - If an error is encountered during the construction of str_list, print 'Error due to list length mismatch!'
    - Test your script with join_str_args([1,2,3,4], [5,6,7,8,9])


#################
### SECTION 2 ###
#################

# 120 MINUTES

####################################
### PANDAS SERIES AND DATAFRAMES ###
####################################

In [15]: import pandas as pd

# A pandas SERIES is a column of data and can be constructed using either lists or dictionaries

In [40]: pd.Series({'jasper' : 29, 'roland' : 32, 'broesch': 32, 'minh' : 35}, name='age')  # Series have an optional name argument (useful for assigning column names)

Out[40]:
broesch    32
jasper     29
minh       35
roland     32
Name: age, dtype: int64

# Series that are constructed from Dictionaries will also be unordered 
# However, the Series will use an order if it gets passed to the index argument

In [41]: pd.Series({'jasper' : 29, 'roland' : 32, 'broesch': 32, 'minh' : 35}, index = ['jasper', 'roland', 'minh', 'broesch'], name='age')

Out[41]:
jasper     29
roland     32
minh       35
broesch    32
Name: age, dtype: int64


In [26]: pd.Series({'jasper' : 29, 'roland' : 32, 'broesch': 32, 'minh' : 35}, index = ['jasper', 'roland', 'jasper'], name='age')

Out[26]:
jasper    29
roland    32
jasper    29
Name: age, dtype: int64


In [12]: pd.Series([29, 32, 32, 35], index=['jasper', 'roland', 'broesch', 'minh'])  

Out[12]:
jasper     29
roland     32
broesch    32
minh       35
dtype: int64


In [27]: pd.Series([[29,29], [32, 32], [32, 32], [35, 35]], index=['jasper', 'roland', 'broesch', 'minh'])  # lists are passed as the Series data

Out[27]:
jasper     [29, 29]
roland     [32, 32]
broesch    [32, 32]
minh       [35, 35]
dtype: object


In [27]: pd.Series([[29,29], [32, 32], [32, 32], [35, 35]])  # no index passed to Series results in default range index being used

Out[27]:
0    [29, 29]
1    [32, 32]
2    [32, 32]
3    [35, 35]
dtype: object

# Take note of the data types the Series is storing
# dtypes can be checked using Series.dtype and DataFrame.dtypes (each column in a DataFrame and the index object will have a dtype)

In [25]: pd.Series([29, 32, 32, [35, 36]], index=['jasper', 'roland', 'broesch', 'minh']).dtype

Out[25]: dtype('O')  

# 'O' stands for object, the designation for mixed types (which include strings)
# NOTE pay careful attention to dtypes as they can suggest when Pandas does not understand how to type the data, which can lead to undesirable behavior
# Pandas uses "duck typing", i.e. "if it looks like a duck and quacks like a duck, it's probably a duck"; it will try to figure out the type

# There are a few different ways to construct Pandas DATAFRAMES using lists, dictionaries, or Series
# When passing a single list or Series to a DataFrame, the data will be interpreted as column data
# When passing multiple lists or Series to a DataFrame, the data will be interpreted as row data
# When passing a single or multiple dictionaries to a DataFrame, the data will be interpreted as row data; however a single Dictionary can be very flexible!
# This can be a little confusing so play around with DataFrame construction to get comfortable with them

In [20]: pd.DataFrame(pd.Series({'jasper' : 29, 'roland' : 32, 'broesch': 32, 'minh' : 35}, name = 'age'))  # single Series

Out[20]:
         age
broesch   32
jasper    29
minh      35
roland    32


In [21]: pd.DataFrame([29, 32, 32, 35], columns = ['age'], index = ['jasper', 'roland', 'broesch', 'minh'])  # single list

Out[21]:
         age
jasper    29
roland    32
broesch   32
minh      35


In [19]: pd.DataFrame({'jasper' : 29, 'roland' : 32, 'broesch': 32, 'minh' : 35}, index = ['age'])  # single Dictionary

Out[19]:
     broesch  jasper  minh  roland
age       32      29    35      32


In [29]: pd.DataFrame({'age':{'jasper':29,'roland':32,'broesch':32,'minh':35}})  # single Dictionary

Out[29]:
         age
broesch   32
jasper    29
minh      35
roland    32


In [24]: pd.DataFrame({'age':[29,32,32,35],'department':['bnet','tox','bnet','esports']}, index=['jasper','roland','broesch','minh'])  # single Dictionary

Out[24]:
         age department
jasper    29       bnet
roland    32        tox
broesch   32       bnet
minh      35    esports


In [24]: pd.DataFrame({'age':[29,32,32,35],'department':['bnet','tox','bnet','esports']}, index=['jasper','roland','broesch','minh'])  # single Dictionary

Out[24]:
         age department
jasper    29       bnet
roland    32        tox
broesch   32       bnet
minh      35    esports


In [24]: pd.DataFrame({'age':{'jasper':29,'roland':32,'broesch':32,'minh':35},'department':{'roland':'tox','broesch':'bnet','minh':'esports','jasper':'bnet'}}, index=['jasper','roland','broesch','minh'])  # single Dictionary

Out[24]:
         age department
jasper    29       bnet
roland    32        tox
broesch   32       bnet
minh      35    esports


In [30]: pd.DataFrame({'jasper':{'age':29,'department':'bnet'}, 'roland':{'age':32,'department':'tox'}})  # single Dictionary

Out[30]:
           jasper roland
age            29     32
department   bnet    tox


In [23]: pd.DataFrame([[29, 32, 32, 35], ['m', 'm', 'm', 'm']], columns = ['jasper', 'roland', 'broesch', 'minh'], index = ['age', 'sex'])  # multiple lists

Out[23]:
    jasper roland broesch minh
age     29     32      32   35
sex      m      m       m    m

# DataFrames can be transposed using df.T

In [23]: pd.DataFrame([[29, 32, 32, 35], ['m', 'm', 'm', 'm']], columns = ['jasper', 'roland', 'broesch', 'minh'], index = ['age', 'sex']).T  # multiple lists

Out[32]:
        age sex
jasper   29   m
roland   32   m
broesch  32   m
minh     35   m

# The above transpose is equivalent to the formulation below 

In [31]: pd.DataFrame([[29,'m'], [32,'m'], [32,'m'], [35,'m']], columns = ['age','sex'], index = ['jasper', 'roland', 'broesch', 'minh'])  # multiple lists

Out[31]:
         age sex
jasper    29   m
roland    32   m
broesch   32   m
minh      35   m


In [100]: pd.DataFrame([pd.Series({'age':29,'sex':'m'},name='jasper'), pd.Series({'age':32,'sex':'m'},name='roland'), pd.Series({'age':32,'sex':'m'},name='broesch'), pd.Series({'age':35,'sex':'m'},name='minh')])
# multiple Series

Out[100]:
         age sex
jasper    29   m
roland    32   m
broesch   32   m
minh      35   m


In [30]: pd.DataFrame([{'roland' : 32, 'jasper' : 29, 'minh' : 35, 'broesch' : 32}, {'roland' : 'm', 'jasper' : 'm', 'broesch' : 'm', 'minh': 'm'}], index = ['age', 'sex'])
# multiple Dictionaries

Out[30]:
    broesch jasper minh roland
age      32     29   35     32
sex       m      m    m      m

# DataFrames can also be built from external sources, including read_csv(), read_excel(), and read_sql(); Python can also connect to APIs
# There are many arguments that can be passed to these functions, such as whether to include a header, how many lines to skip, etc; see documentation for more details

In [20]: df = pd.read_excel('C:\\users\\rheinze\\desktop\\test_excel.xlsx')
In [21]: df

Out[21]:
         age      department
jasper    29     bnet
roland    32      tox
broesch   32     bnet
minh      35  esports


In [46]: from roland_toolbox import connect_db, query_db
In [47]: td = connect_db('td')
In [48]: df2 = query_db(td, 'select * from dlab_rheinze.wow_free_game_time_times sample 1')
In [49]: df2

Out[49]:
   agent_key  issue_key          created_at           closed_at  gm_time
0    0.25345   2.599012 2017-10-08 11:51:08 2017-10-08 11:51:08      0.0

#########################################
### FILTERING AND QUERYING DATAFRAMES ###
#########################################

In [53]: df

Out[53]:
         age department
jasper    29       bnet
roland    32        tox
broesch   32       bnet
minh      35    esports

# To gather some quick information on a df use descriptive methods such as .shape, .index, .columns, .dtypes, and .describe()

In [58]: df.shape

Out[58]: (4, 2)


In [59]: df.index

Out[59]: Index(['jasper', 'roland', 'broesch', 'minh'], dtype='object')  # Index is its own type of object in Pandas


In [60]: df.columns

Out[60]: Index(['age', 'department'], dtype='object')  # columns also use Index objects; MultiIndex objects are used to create hierarchies on either index or columns


In [61]: df.dtypes

Out[61]:
age            int64
department    object
dtype: object


In [11]: df.describe()

Out[11]:
            age
count   4.00000
mean   32.00000
std     2.44949
min    29.00000
25%    31.25000
50%    32.00000
75%    32.75000
max    35.00000

# To filter columns, pass the df a single column name using the attribute operator . or a list of column names using the indexing operator []

In [20]: df.age

Out[20]:
jasper     29
roland     32
broesch    32
minh       35
Name: age, dtype: int64


In [20]: df['age']

Out[20]:
jasper     29
roland     32
broesch    32
minh       35
Name: age, dtype: int64


In [54]: df[['age','department']]

Out[54]:
         age department
jasper    29       bnet
roland    32        tox
broesch   32       bnet
minh      35    esports

# To filter rows, first create a BOOLEAN MASK to calculate the truth of a set of conditions for each index
# The boolean mask is a Series with True/False labels for each index

In [28]: df['age']==32

Out[28]:
jasper     False
roland      True
broesch     True
minh       False
Name: age, dtype: bool

# Then pass the boolean mask to the df

In [62]: df[df['age']==32]

Out[62]:
         age department
roland    32        tox
broesch   32       bnet

# Use other operators (such as ~, >, <, !=) or methods (such as .isin(), .contains(), isnull()) to modify the conditions of the boolean mask

In [30]: df[df['age'].isin([32,35])]

Out[30]:
         age      dpt
roland    32      tox
broesch   32      tox
minh      35  esports


In [69]: df[~(df['age'] < 34)]  # as a best practice always encapsulate conditions in parentheses 

Out[69]:
      age department
minh   35    esports


In [67]: df[df['department'].str.contains('o')]  # when using string methods you must generally pass the .str accessor to a Series

Out[67]:
        age department
roland   32        tox
minh     35    esports


In [65]: df[df['age'].isnull()]  # Note NaN is not the same as None, more reference at https://stackoverflow.com/questions/17534106/what-is-the-difference-between-nan-and-none

Out[65]:
Empty DataFrame
Columns: [age, department]
Index: []

# Boolean masks can be created using multiple conditions; the operators for "and" and "or" are & and | respectively

In [32]: df[(~df['age'].isin([32])) & (df['dpt']=='bnet')]

Out[32]:
        age   dpt
jasper   29  bnet


In [33]: df[(~df['age'].isin([32])) & ~(df['dpt']=='bnet')]

Out[33]:
      age      dpt
minh   35  esports


In [34]: df[(~df['age'].isin([32])) | ~(df['dpt']=='bnet')]

Out[34]:
         age      dpt
jasper    29     bnet
roland    32      tox
broesch   32      tox
minh      35  esports

# At this point, consider querying only a specific column or set of columns using what is called "chain indexing"

In [71]: In [33]: df[(~df['age'].isin([32])) & ~(df['department']=='bnet')]['age']

Out[71]:
minh    35
Name: age, dtype: int64

# While this can still work depending on the task, it is generally considered BAD PRACTICE to chain like this! 
# *** Rule of Thumb: never use back-to-back brackets! ][ ***
# For more reference see the first section of https://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
# The problem comes down to unpredictable behavior about whether the object returned is a copy or a view of the df

# Instead there are two better ways to query dfs, .loc and .iloc attributes
# Try to remember .loc as "name-based" and .iloc as "index-based" querying

In [73]: df.loc['roland']  # name-based querying on the index

Out[73]:
age            32
department    tox
Name: roland, dtype: object


In [74]: df.iloc['roland']  # attempting to pass a name to an index-based query results in an error
# TypeError: cannot do positional indexing on class pandas.core.indexes.base.Index with these indexers [roland] of class str


In [75]: df.iloc[1]  # index location 1 is the same as name-based location 'roland'

Out[75]:
age            32
department    tox
Name: roland, dtype: object

# The first argument of the .loc and .iloc methods is the rows index and the second argument is the columns index (not necessary to include a columns index)
# Use boolean masks to pass conditions to the indices/rows and also pass a list of columns to return
# Note how passing lists vs. singular values can lead to different results of DataFrame vs. Series... this can be confusing!
# Below are various examples for reference

In [307]: df.loc['roland']  # Series

Out[307]:
age            32
department    tox
Name: roland, dtype: object  # declaration of Series name and dtype


In [312]: df.loc[['roland']]  # DataFrame

Out[312]:
        age department
roland   32        tox


In [322]: df.loc[['roland'],'age']  # Series

Out[322]:
roland    32
Name: age, dtype: int64


In [324]: df.loc['roland',['age']]  # Series, but with a different index and name!

Out[324]:
age    32
Name: roland, dtype: object


In [323]: df.loc[['roland'],['age']]  # DataFrame

Out[323]:
        age
roland   32


In [313]: df.loc['roland','age']  # scalar :)

Out[313]: 32


In [156]: df.loc[:]  # the : operator returns a list of indices, DataFrame

Out[156]:
         age department
jasper    29       bnet
roland    32        tox
broesch   32       bnet
minh      35    esports


In [155]: df.loc[:,['age']]  # DataFrame

Out[155]:
         age
jasper    29
roland    32
broesch   32
minh      35


In [157]: df.loc[:,'age']  # Series

Out[157]:
jasper     29
roland     32
broesch    32
minh       35
Name: age, dtype: int64


In [140]: df.loc[df['age']==32,['age']]  # boolean mask returns a list with multiple indices, DataFrame

Out[140]:
         age
roland    32
broesch   32


In [144]: df.loc[df['age']==32,'age']  # Series

Out[144]:
roland     32
broesch    32
Name: age, dtype: int64

# To return a value from a SERIES with a single entry use the .item() method; note if the query returns multiple values this will generate an error

In [146]: df.loc[df['age']==32,'age'].item()  # Series with multiple values
# ValueError: can only convert an array of size 1 to a Python scalar


In [147]: df.loc[df['age']==35,'age'].item()  # Series with single value

Out[147]: 35

############################
### MODIFYING DATAFRAMES ###
############################

# To create a copy of a df slice use the .copy() method

In [81]: df2 = df.loc['roland'].copy()

In [81]: df2
In [82]: df2

Out[82]:
age            32
department    tox
Name: roland, dtype: object

# df slices can be modified using loc/iloc and new columns can be defined directly using scalars, lists, existing columns, or Series

In [154]: df2.loc['roland','age'] = 33

Out[82]:
age            33
department    tox
Name: roland, dtype: object


In [43]: df['tenure'] = 0
In [44]: df

Out[44]:
         age department  tenure
jasper    29       bnet       0
roland    32        tox       0
broesch   32        tox       0
minh      35    esports       0


In [50]: df2['tenure'] = [1,1,2,10]
In [51]: df2

Out[51]:
         age department  tenure
jasper    29       bnet       1
roland    32        tox       1
broesch   32        tox       2
minh      35    esports      10


In [88]: df['tenure'] = df['age']/2
In [89]: df

Out[89]:
         age department  tenure
jasper    29       bnet    14.5
roland    32        tox    16.0
broesch   32       bnet    16.0
minh      35    esports    17.5


In [94]: df['tenure'] = pd.Series({'roland': 2, 'jasper' : 0, 'broesch' : 3, 'minh' : 10})
In [95]: df

Out[95]:
         age department  tenure
jasper    29       bnet       0
roland    32        tox       2
broesch   32       bnet       3
minh      35    esports      10

# Add rows to the df using the .append() method

In [241]: df2 = df.copy()
In [251]: df2.append(pd.Series({'age':26,'sex':'male'},name='kier'))  # unassigned data will be filled with NaNs

Out[251]:
         age department  tenure   sex
jasper    29       bnet     0.0   NaN
roland    32        tox     2.0   NaN
broesch   32       bnet     3.0   NaN
minh      35    esports    10.0   NaN
kier      26        NaN     NaN  male

# To rename a column, use the .rename() method and assign a dictionary to the "columns" argument

In [96]: df.rename(columns={'tenure' : 'years'})

Out[96]:
         age department  years
jasper    29       bnet      0
roland    32        tox      2
broesch   32       bnet      3
minh      35    esports     10


In [97]: df

Out[97]:
         age department  tenure
jasper    29       bnet       0
roland    32        tox       2
broesch   32       bnet       3
minh      35    esports      10

# NOTE *** sometimes calling a method on a df will not change the original df and will simply output a copy of the df with the changes applied ***
# To apply changes to the original df, either assign the modified df to a new df or use the "inplace" argument within the method

In [98]: df = df.rename(columns={'tenure' : 'years'})
In [99]: df

Out[99]:
         age department  years
jasper    29       bnet      0
roland    32        tox      2
broesch   32       bnet      3
minh      35    esports     10


In [100]: df.rename(columns={'years' : 'tenure'}, inplace=True)
In [101]: df

Out[101]:
         age department  tenure
jasper    29       bnet       0
roland    32        tox       2
broesch   32       bnet       3
minh      35    esports      10

# To rename a row, use the "index" argument instead of the "columns" argument

In [164]: df2 = df.rename(index={'jasper' : 'kush'})
In [165]: df2

Out[165]:
         age department  tenure
kush      29       bnet       0
roland    32        tox       2
broesch   32       bnet       3
minh      35    esports      10

# To delete columns use the .drop() method with the "columns" argument

In [102]: df2 = df.drop(columns=['department','tenure'])
In [103]: df2

Out[103]:
         age
jasper    29
roland    32
broesch   32
minh      35

# To delete rows pass the indices to the .drop() method (with or without the "index" argument), or alternatively use a boolean mask to create a new df!

In [104]: df2 = df.drop(['roland'])
In [105]: df2

Out[105]:
         age department  tenure
jasper    29       bnet       0
broesch   32       bnet       3
minh      35    esports      10


In [166]: df2 = df.drop(index=['roland'])
In [167]: df2

Out[167]:
         age department  tenure
jasper    29       bnet       0
broesch   32       bnet       3
minh      35    esports      10


In [111]: df2 = df.loc[~(df.index=='roland')]
In [112]: df2

Out[112]:
         age department  tenure
jasper    29       bnet       0
broesch   32       bnet       3
minh      35    esports      10


In [115]: df2 = df.drop(df[df['department']=='bnet'].index)
In [116]: df2

Out[116]:
        age department  tenure
roland   32        tox       2
minh     35    esports      10


In [117]: df2 = df[~(df['department']=='bnet')]  # no .drop() method, only using a boolean mask
In [118]: df2

Out[118]:
        age department  tenure
roland   32        tox       2
minh     35    esports      10

# Drop duplicates by passing a list of columns to the .drop_duplicates() method

In [95]: df2.drop_duplicates(['department'])

Out[95]:
        age department
jasper   29       bnet
roland   32        tox
minh     35    esports


In [96]: df2.drop_duplicates(['department'],keep='last')

Out[96]:
         age department
roland    32        tox
broesch   32       bnet
minh      35    esports

# Use the .dropna() method as a shortcut to remove subsets of the df with missing values (instead of using boolean masks)
# By default, this method applies to rows (axis=0) but can also apply to columns (axis=1)
# By default, this method drops rows/columns with 'any' missing values but can also drop rows/columns with 'all' missing values using the 'how' argument

In [254]: import numpy as np
In [219]: df2 = df.copy().append(pd.Series(name='kier'))
In [231]: df2['sex'] = np.nan
In [220]: df2

Out[233]:
          age department  tenure  sex
jasper   29.0       bnet     0.0  NaN
roland   32.0        tox     2.0  NaN
broesch  32.0       bnet     3.0  NaN
minh     35.0    esports    10.0  NaN
kier      NaN        NaN     NaN  NaN


In [223]: df2.dropna()  # this drops rows with any missing values (which is all rows)

Out[234]:
Empty DataFrame
Columns: [age, department, tenure, sex]
Index: []


In [237]: df2.dropna(how='all')  # this drops rows with all values missing (which is only kier)
Out[237]:
          age department  tenure  sex
jasper   29.0       bnet     0.0  NaN
roland   32.0        tox     2.0  NaN
broesch  32.0       bnet     3.0  NaN
minh     35.0    esports    10.0  NaN


In [235]: df2.dropna(axis=1)  # this drops columns with any missing values (which is all columns because kier row is missing all values)

Out[235]:
Empty DataFrame
Columns: []
Index: [jasper, roland, broesch, minh, kier]


In [238]: df2.dropna(axis=1, how='all')  # this drops columns with all values missing (which is only sex)

Out[238]:
          age department  tenure
jasper   29.0       bnet     0.0
roland   32.0        tox     2.0
broesch  32.0       bnet     3.0
minh     35.0    esports    10.0
kier      NaN        NaN     NaN


In [266]: df2.dropna(subset=['tenure','sex'],how='any')  # drop rows where either 'tenure' or 'sex' have any missing values (which is all rows since sex has all values missing)

Out[266]:
Empty DataFrame
Columns: [age, department, tenure, sex]
Index: []


In [265]: df2.dropna(subset=['tenure','sex'],how='all')  # drop rows where both 'tenure' and 'sex' have all values missing (which is only kier)

Out[265]:
          age department  tenure  sex
jasper   29.0       bnet     0.0  NaN
roland   32.0        tox     2.0  NaN
broesch  32.0       bnet     3.0  NaN
minh     35.0    esports    10.0  NaN


In [270]: df2.dropna(axis=1,subset=['jasper','kier'])  # drop columns where either jasper or kier have any missing values (which is all columns since kier has all values missing)

Out[270]:
Empty DataFrame
Columns: []
Index: [jasper, roland, broesch, minh, kier]


In [271]: df2.dropna(axis=1,subset=['jasper','kier'],how='all')  # drop columns where both jasper and kier have all values missing (which is only sex)

Out[271]:
          age department  tenure
jasper   29.0       bnet     0.0
roland   32.0        tox     2.0
broesch  32.0       bnet     3.0
minh     35.0    esports    10.0
kier      NaN        NaN     NaN

# Use .fillna() to fill missing values instead of dropping them; fillna() offers both forward and back fill methods, which are useful for time series data

In [285]: df2.fillna('filled')  # applies to all missing values

Out[285]:
            age department  tenure     sex
jasper       29       bnet       0  filled
roland       32        tox       2  filled
broesch      32       bnet       3  filled
minh         35    esports      10  filled
kier     filled     filled  filled  filled


In [278]: df2['sex'] = df2['sex'].fillna('male')  # queries the 'sex' column, fills missing values with 'male' and replaces the existing 'sex' column in df2 with the filled Series
In [279]: df2

Out[279]:
          age department  tenure   sex
jasper   29.0       bnet     0.0  male
roland   32.0        tox     2.0  male
broesch  32.0       bnet     3.0  male
minh     35.0    esports    10.0  male
kier      NaN        NaN     NaN  male


In [302]: df2.fillna({'age' : 'who', 'department' : 'wha', 'tenure' : '?', 'sex' : 'whoa there...'})  # pass a dictionary of each column and its fill value

Out[302]:
               age department tenure            sex
jasper          29       bnet      0  whoa there...
roland          32        tox      2  whoa there...
broesch         32       bnet      3  whoa there... 
minh            35    esports     10  whoa there...
kier            who       wha     ?   whoa there...


In [293]: df2.loc['roland','sex'] = 'male'
In [294]: df2.loc['minh','sex'] = 'cooler male'
In [295]: df2

Out[295]:
          age department  tenure          sex
jasper   29.0       bnet     0.0          NaN
roland   32.0        tox     2.0         male
broesch  32.0       bnet     3.0          NaN
minh     35.0    esports    10.0  cooler male
kier      NaN        NaN     NaN          NaN


In [296]: df2.fillna(method='ffill')  # fills using the previous non-null value, if it exists

Out[296]:
          age department  tenure          sex
jasper   29.0       bnet     0.0          NaN  # no previous value
roland   32.0        tox     2.0         male
broesch  32.0       bnet     3.0         male  # filled by roland
minh     35.0    esports    10.0  cooler male
kier     35.0    esports    10.0  cooler male  # filled by minh


In [297]: df2.fillna(method='bfill')  # fills using the next non-null value, if it exists

Out[297]:
          age department  tenure          sex
jasper   29.0       bnet     0.0         male  # filled by roland
roland   32.0        tox     2.0         male
broesch  32.0       bnet     3.0  cooler male  # filled by minh
minh     35.0    esports    10.0  cooler male
kier      NaN        NaN     NaN          NaN  # no value after

# To change the columns of data used as the index of the df use the .set_index() method
# This can be useful to assign new column data to a df with a Series

In [170]: df.set_index(pd.Series(['a','b','c','d']))

Out[170]:
   age department  tenure
a   29       bnet       0
b   32        tox       2
c   32       bnet       3
d   35    esports      10

# Instead of directly replacing the current index, append another level to the index (creating a MultiIndex) using the "append" argument

In [183]: df2 = df.set_index(pd.Series(['a','b','c','d']), append=True)  # indexes with multiple levels are called MultiIndex
In [185]: df2

Out[185]:
           age department  tenure
jasper  a   29       bnet       0
roland  b   32        tox       2
broesch c   32       bnet       3
minh    d   35    esports      10


In [186]: df2 = df.set_index(['department', 'tenure'])

Out[190]:
                   age
department tenure
bnet       0        29
tox        2        32
bnet       3        32
esports    10       35


In [191]: df2.index

Out[191]:
MultiIndex(levels=[['bnet', 'esports', 'tox'], [0, 2, 3, 10]],
           labels=[[0, 2, 0, 1], [0, 1, 2, 3]],
           names=['department', 'tenure'])

# Resetting the index of a df can be useful when indices are duplicated, such as after concatenating multiple dfs together
# However the current index can hold valuable data, so it is generally desirable to rename and write it to the df as a new column
# .reset_index() by default promotes the existing index into a new column and applies a new range index to the df

In [211]: df2 = df.copy()
In [211]: df2.index.name = 'emp'
In [204]: df2.reset_index()

Out[204]:
       emp  age department  tenure
0   jasper   29       bnet       0
1   roland   32        tox       2
2  broesch   32       bnet       3
3     minh   35    esports      10

# Group By can sometimes result in indices with tuples and needs to be converted into MultiIndex before being promoted into columns using .reset_index()
# df.index = pd.MultiIndex.from_tuples(df.index)
# df.reset_index(level=[0,1])  0 is the outer-most index in either a row or column MultiIndex

###################
### AGGREGATION ###
###################

# For additional reference on concat and merge see https://pandas.pydata.org/pandas-docs/stable/merging.html
# For additional reference on aggregation see https://pandas.pydata.org/pandas-docs/stable/groupby.html

# .append() was introduced earlier as a method to add rows to a df, and is a shortcut for .concat()
# .concat() can append either rows or columns to a df
# .merge() is the analog to SQL join

In [69]: df3 = pd.DataFrame({'age':{'jasper':80,'n':5,'s':12},'dpt':{'jasper':None,'n':None,'s':None}},index=['jasper','n','s'])

In [69]: df4 = pd.concat([df2,df3], axis=0)  # concat along rows

In [70]: df4
Out[70]:
         age      dpt
jasper    29     bnet
roland    32      tox
broesch   32      tox
minh      35  esports
jasper    80     None  # duplicate index is allowed
n          5     None
s         12     None

In [71]: df4 = pd.concat([df2,df3],axis=1)  # concat along columns

In [73]: df4
Out[73]:
          age      dpt   age   dpt
broesch  32.0      tox   NaN   NaN
jasper   29.0     bnet  80.0   NaN  # jasper is the only row from df2 with data in the 'age' column
minh     35.0  esports   NaN   NaN
n         NaN      NaN   5.0  none
roland   32.0      tox   NaN   NaN
s         NaN      NaN  12.0  none

# concat is very useful for aggregating DataFrames using for loops

# MERGE

# Pandas features a wide range of general aggregation and window functions

In [75]: df2['age'].max()
Out[75]: 35

# These can be applied to columns of groupby sub-frames

In [76]: df2.groupby(['dpt'])['age'].agg('max')
Out[76]:
dpt
bnet       29
esports    35
tox        32
Name: age, dtype: int64

# Can Pass functions to Groupby to essentially create hash functions / similar to CASE in SQL
# Can also sequentially merge groupbys to the original data frame to concatenate levels of detail
# Merges follow the df.merge(df2, how, left, right) format, where how can be inner, left, right, outer, and left/right are left_index=True or right_on= list of columns depending on keys or columns are being joined on
# APPLY


###########################
### SECTION 2 EXERCISES ###
###########################

"""

40 MINUTES

(1) Write a function called connect_db that accepts a single argument with default value 'td'
    The function should have the following properties:
    - A docstring that states your name
    - A print statement that displays your name using string interpolation
    - If the argument passed to the function is 'hive', return a variable with two lists packed into it [1,2,3,4] and [5,6,7,8,9]
    - If the argument passed to the function is 'td', return a list that uses an anonymous function to take sqrt of all the values in [1,2,3,4]
    - Test your function with "connect_db('hive')" and "connect_db()"

In [142]: from math import sqrt
     ...: def connect_db(x='td'):
     ...:     '''roland'''
     ...:     print('{}'.format('roland'))
     ...:     if x == 'hive':
     ...:         return ([1,2,3,4],[5,6,7,8,9])
     ...:     if x == 'td':
     ...:         return list(map(lambda x: sqrt(x), [1,2,3,4]))
     ...:

(2) Write a script that does the following:
    - Takes a list of lists of integers [[1,2,3,4],[5,6,7,8,9]] and creates 2 new lists where each list is a list of strings of those same integers
    - Loops over an iterable with length of the longest list in the set and creates a new list str_list that looks like ['1 5','2 6','3 7',...]
    - If an error is encountered, print 'Error due to list length mismatch!'
    - Test your script with "str_list"

In [140]: list1 = [1,2,3,4]
     ...: list2 = [5,6,7,8,9]
     ...: list1 = list(map(lambda x: str(x),list1))
     ...: list2 = list(map(lambda x: str(x),list2))
     ...: str_list = []
     ...: for i in range(max(len(list1),len(list2))):
     ...:     try:
     ...:         str_list.append('{0} {1}'.format(list1[i],list2[i]))
     ...:     except:
     ...:         print('Error due to list length mismatch!') 

"""

#################
### SECTION 3 ###
#################

# ROLAND_TOOLBOX

# The functions in roland_toolbox are shortcuts to improve data source connectivity and the ability to write tables from SQL queries and DataFrames
# These functions make heavy use of pyodbc connections, which include both a connection and a cursor object

def connect_db(db_name='td'):

    """
    use format " conn_obj = connect_db(str) ", e.g. " hive = connect_db('hive') "
    """
    
    print('CALLED CONNECT_DB FROM ROLAND_TOOLBOX')

    if db_name == 'hive':
        con = pyodbc.connect(dsn='{}'.format(os.environ.get('HIVE_DSN')),  # os library calls system environment variable 'HIVE_DSN' which is my odbc connection name in Windows
                            trusted_connection='yes',
                            autocommit=True)
        print('Connected to Hive!')

    elif db_name == 'irvaag':
        con = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',  # this connection string specifies everything directly instead of calling the odbc connection name
                            server='irvaag4003.corp.blizzard.net,54003',
                            database='salesforce',
                            trusted_connection='yes',
                            autocommit=True)
        print('Connected to IRVAAG!')

    elif db_name == 'td':
        con = pyodbc.connect(dsn='{}'.format(os.environ.get('TD_DSN')),  # odbc connection name
                            database='bidw',
                            autocommit=True)
        print('Connected to Teradata!')

    elif db_name == 'tox':
        con = pyodbc.connect(driver='{MySQL ODBC 8.0 ANSI Driver}',
                            server='dev17-bi-toxicity.dev.cloud.blizzard.net',
                            port='3306',
                            database='toxic_db',
                            user='{%s}' % (os.environ.get('TOX_LOGIN')),  # os library calls my logins and passwords
                            password='{%s}' % (os.environ.get('TOX_PASS')))
        print('Connected to ToxOrNot!')

    cur = con.cursor()
    return con, cur


# query_db returns a df as a result of running query_str against src_obj

def query_db(src_obj, query_str):

    print('CALLED QUERY_DB FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj

    start_time = time.time()  # counts time required for query execution
    df = pd.read_sql(query_str, src_con)
    end_time = time.time()
    
    print('Successfully Ran Query in {} Minutes!'.format(round((end_time-start_time)/60, 1)))
    return df


# write_table_from_query writes the output of query_str against src_obj to table in dst_obj with defined cols and types

def write_table_from_query(src_obj, dst_obj, query_str, table, cols, types, primary_index = None):

    """
    this function writes single rows sequentially to a table
    pass connect_db objects to src_obj and dst_obj
    e.g. write_table_from_query(td, hive, ...)
    pass column names and data types as lists of strings
    e.g. write_table_from_query(..., ['name_col1', 'name_col2'], ['data_type_col1', 'data_type_col2'], ...)
    primary_index is not required, but must be passed as a list of strings if included
    """

    print('CALLED WRITE_TABLE_FROM_QUERY FROM ROLAND_TOOLBOX')

    src_con, src_cur = src_obj
    dst_con, dst_cur = dst_obj

    cols_str = ', '.join(map(lambda x: str(x), cols))  # create a single string of columns from the list
    
    cols_types_str = ''
    for element in range(len(cols)):
        cols_types_str = cols_types_str + '{} {},'.format(cols[element], types[element])
    cols_types_str = cols_types_str[:len(cols_types_str)-1]  # drop the last comma

    df = pd.read_sql(query_str,src_con)
    df.dropna(how='all', inplace=True)

    try:
        dst_cur.execute('drop table {}'.format(table))
        print('{} Table Dropped!'.format(table))
    except:
        print('No {} Table to Drop!'.format(table))

    try:
        if primary_index == None:
            dst_cur.execute('create table {} ( {} )'.format(table, cols_types_str))
            print('Table {} Created!'.format(table))
        else:
            primary_index_str = ','.join(primary_index)
            dst_cur.execute('create table {} ( {} ) unique primary index ( {} )'.format(table, cols_types_str, primary_index_str))  # this needs to be updated to be any custom text
            print('Table {} Created!'.format(table))
    except:
        print('{} Table Already Exists!'.format(table))

    df_tuples = list(map(lambda x: tuple(x), df.values.tolist()))

    values_str = '?,'*len(cols)
    values_str = values_str[:len(values_str)-1]  # removes the last comma

    print('Writing {} Records to {}...'.format(len(df_tuples), table))
    start_time = time.time()
    dst_cur.executemany('insert into {} ( {} ) values ( {} )'.format(table, cols_str, values_str), df_tuples)
    end_time = time.time()

    print('Table {} Successfully Written in {} Minutes!'.format(table, round((end_time-start_time)/60, 1)))

###########################
### SECTION 3 EXERCISES ###
###########################

# Practice using the roland_toolbox functions by copy/pasting them into the shell
# After having downloaded the data, try to create multiple dfs and merge/concat them, add columns and/or fill in missing values, group and aggregate them
# It may be necessary to either create environmental variables or change connection parameters to properly connect to data sources

# Here are some examples of things to try

# EXAMPLE 1

# td = connect_db("td")
# td_query_str = '''
# SELECT *
# FROM acct.blizzard_login_daily bld
# JOIN acct.d_bnet_account dba
# ON dba.bnet_account_key = bld.bnet_account_key
# WHERE bld.login_date = '2018-10-23'
# SAMPLE 10
# '''
# td_df = query_db(td, td_query_str)

# EXAMPLE 2

# from roland_toolbox import connect_db, query_db, write_table_from_query_batch
# td = connect_db("td")
# hive = connect_db("hive")
# hive_query_str = "SELECT * FROM telem_pro.pro_lobby_endorsementlevelchange LIMIT 10"
# write_table_from_query_batch(
# hive,
# td,
# hive_query_str,
# 'dlab_rheinze.new_table',
# ['col_name1', 'col_name2', ...],
# ['integer', 'varchar(30)', 'col_name3 dtype', ...],
# 10000
# )
# query_db(td, 'dlab_rheinze.new_table')

#################
### APPENDIX  ###
#################

# FULL PYTHON INSTALLATION

# Install the latest version of Python from https://www.python.org/downloads/ and make sure to check the option "Install to System Environment Path"
# After installation, open the command prompt by typing "cmd" into your Start menu
# Next install Python libraries -- pandas, numpy, pyodbc, ipython -- by typing "pip install pandas" and hitting Enter in the Command Prompt
# iPython will serve as the shell for our Python interpreter; it's easy to copy/paste large blocks of Python code into the iPython shell

''' IMPORTANT: You may encounter some errors when installing Python libraries using Windows...
When that occurs, try using https://www.lfd.uci.edu/~gohlke/pythonlibs/ to find the .whl file associated with your version of Python and Operating System
Once downloaded, navigate to your Python directory's Lib folder (similar to C:\Users\rheinze\AppData\Local\Programs\Python\Python36\Lib)
Move the .whl file into the Lib folder, change the Commmand Prompt's current working directory to the Lib directory, and use pip to install the .whl file
Do this using a sequence of Command Prompt commands: "c:", "cd C:\Users\rheinze\AppData\Local\Programs\Python\Python36\Lib", "pip install filename.whl"

# SECTION 1 ANSWERS

In [23]: def connect_db(x='td'):
    ...:     '''This is the docstring for connect_db'''
    ...:     if x == 'td':
    ...:         con, cur = 'td_con', 'td_cur'
    ...:     if x == 'hive':
    ...:         con, cur = 'hive_con', 'hive_cur'
    ...:     print('Connection to {0} Successful!'.format(x))
    ...:     return (con, cur)

In [34]: def join_str_args(list1, list2):
    ...:     str_list1 = list(map(lambda x: str(x), list1))
    ...:     str_list2 = list(map(lambda x: str(x), list2))
    ...:     str_list = []
    ...:     for i in range(max(len(str_list1), len(str_list2))):
    ...:         try:
    ...:             str_list.append('{0} {1}'.format(str_list1[i], str_list2[i]))
    ...:         except:
    ...:             print('Error due to list length mismatch!')
    ...:     return str_list
