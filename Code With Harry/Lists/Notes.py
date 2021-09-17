1). “arithmetic with lists is also possible, like adding two lists together or repeating the contents of a list.

>>> [1,2] + [3,4]
[1, 2, 3, 4]
>>> [1,2] * 2
[1, 2, 1, 2]

2). Slicing of elements from any parent list returns a "New List"

3). clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters

4) '\' can be used as Escape Quotes in line
>>> "\"Yes,\" he said."
>>> '"Yes," he said.'

5) If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
>>> print(r'C:\some\name')  # note the r before the quote
>>> C:\some\name

6) Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated but This only works with two literals though, not with variables or expressions.
>>> 'Py' 'thon'
>>> 'Python'

7) While slicing string like list[1:3] from list "Python"
>>> yt  #Here only "yt" is printed bcz python excludes last index and includes first index only.

8) For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.

