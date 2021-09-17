#FrozenSet is a new class that has the characteristics of set but its elements cannot be changed once assigned.
#Like Tuple are immutable lists, Frozensets are immutable sets.


set1 = frozenset({1, 2, 3, 4, 5})
set2 = frozenset({4, 5, 6, 7, 8})
print(set1)
print(set1.intersection(set2)) #We can do intersection, union, symmetric_difference, difference operation in Frozenset but we cant add, remove, etc operation in frozenset because it is immutable.