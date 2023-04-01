#Often we will need to zip two or more iterables together. The
#zip function transforms multiple iterables into a single iterable of tuples of corresponding function:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

#zip is lazy, so you have to do something like the following
[pair for pair in zip(list1, list2)] #is [('a', 1), ('b', 2), ('c', 3)]

#if the lists are different lengths, zip stops as soon as the first list ends.

#You can 'unzip' a list using a strange trick:

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

#The asterisk (*) performs argument unpacking, which uses the elements of
#pairs as individual arguments to zip. It ends up the same as if you'd called;

letters, numbers = zip(('a', 1), ('b', 2), ('c', 3))

#you can use argument unpacking with any function:

def add(a, b): return a + b
add(1, 2) #returns 3
try:
    add([1, 2])
except TypeError:
    print("add expects two inputs")
add(*[1, 2]) # returns 3