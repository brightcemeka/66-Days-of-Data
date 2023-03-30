#Often all we need is to iterate over the collection using for and in. In this case we can create
#generators, which can be iterated over just like lists but generate their values lazily on demand.

#One way to create generators is with functions and the yield operator:
def generate_range(n):
    i = 0
    while i < n:
        yield i # every call to yield produces a value of the generator
        i += 1

#The following loop will consume the yielded values one at a time until none are left:

for i in generate_range(10):
    print(f"i: {i}")

#With a generator, you can even create an infinite sequence:

def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

#A second way to create generators is by using for comprehensions wrapped in parentheses:

evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

#Such a "generator comprehension" doesn't do any work until you iterate over it (using for or next).
#We can use this to build up elaborate data processing pipelines:

#None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

#When we are iterating over a list or a generator we'll want not just the values but also their indices.
#For this common case Python provides an 'enumerate' function, which turns values into pairs (index, value):

names = ["Alice", "Bob", "Charlie", "Debbie"]

#not pythonic * Not a best practice
for i in range(len(names)):
    print(f"name {i} is name {names[i]}")

#also not pythonic
i = 0
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1

#PYTHONIC
for i, name in enumerate(names):
    print(f"name {i} is {name}")