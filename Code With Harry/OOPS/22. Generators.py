#Iterables : objects that can be placed inside a loop and are capable of returning one variable at a time. In simple terms, we can say that iterables are objects capable of iteration. Examples of iterable include list, string, tuple, etc. 

#Iteration : Object that does iterations on iterable. Meaning that it will move from character to character doing iteration.

# Every iterable, either it is a string or tuple has a built-in method __iter__() that creates an object when called. The object moves from character to character of iterable using the __next__() method. The __next__() method is, what's really behind the working of the loop. 

# Generators : Generators concept is also very similar as it is used to make an iterator. The only difference comes in the return statement. The generator does not use a return statement. Instead, it uses a yield keyword. Yield functionality is very similar to return as it returns a value to the caller, but the difference is that it also saves the state of the iterator. Meaning that when we use the function again, the yield will resume it is the value from the place it left off. 
# Generators in Python are created just like the normal functions using the ‘def’ keyword. Generator functions do not run by their name, and they are run when the __next__() function is called.Generator is very helpful in projects relating to memory issue because like a simple iterator, it does not return all the values at a time instead it produces, series of values overtime. So a generator is generally used when we want to iterate over a series of values but do not want to store them completely in memory. 


#Advantages of using Generators.
# -> Producing iterables is extremely difficult and lengthy without Generators in Python.
# -> Generators automatically implement __iter__(), __next__() and StopIteration which otherwise, need to be explicitly specified.
# -> The most significant advantage of generators is that the memory is saved as the items are produced when required.
# -> Generators are also used to pipeline a series of operations, for example, Generate Fibonacci Series.

#Example : 

"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)











# Notes :
# 1) We can Generate Object only at once means if we have generated 1 to 1000 numbers then we can generate them only at once. 
# 2) We should check that Object is Iterable or Not because Only Iterable Objects can be Generated. for example str is iterable but int, range() is not Iterable.