#Dictionaries - a DS that associates values with keys and allows you
#quickly retrieve the value corresponding to a given key:

empty_dict = {}
grades = {"Joel":80, "Tim":95} #dictionary literal

#you can look up the value for a key using square brackets:
joels_grade = grades["Joel"]

#When you as for a key not in a dictionary you get KeyError
#you can confirm the existence of a key using 'in':

joel_has_grade = "Joel" in grades #This returns True
print(joel_has_grade)

#Dictionaries have a get method that returns a default value instead of
#raising an exception

joels_grade_check = grades.get("Joel", 0) #It returns 0 if the key is not there
print(joels_grade_check) #If the key is there, it returns its value

#Dictionaries can represent structured data;

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags":["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

#we can look at all the keys
tweet_keys = tweet.keys()
print(tweet_keys)
#we can also look at all the values
tweet_values = tweet.values()
print(tweet_values)
#iterable for the (key, value) tuples
tweet_items = tweet.items()
print(tweet_items)

#NOTE: Dictionary keys must be 'hashable'; you cannot use lists as keys. If
#If you need a multipart key, you should probably use a tuple or figure
#out a way to turn the key into a string.

#To do word count in a document /usecase for defaultdict

document = {}

#WRONG Way
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#YOU might get keyerror in the above, here's another way

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
#Another approach is to use get

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

#The above is unwieldly which is why defaultdict is useful
#To use defaultdict you have to import them from colections

from collections import defaultdict

word_counts = defaultdict(int) # int() produces 0
for word in document:
    word_counts[word] += 1

#Defaultdict can also be useful with list or dict or functions
dd_list = defaultdict(list)      #list() produces an empty list
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)      #dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"
print(dd_dict)

#COUNTERS - A counter turns a sequence of values into a defaultdict(int)-like
#object mapping keys to counts:

from collections import Counter
c = Counter([0, 1, 2, 0])
print(c)

#Counters have a most_common method that is frequently used


#SETS - A set is a collection of distinct elements; use curly braces to define sets
#To create an empty set use the set()
s = set()
s.add(1) # s is now {1}
s.add(2) # s is now {1, 2}
s.add(2) # s is still {1, 2}
print(len(s))
print(s)

#We use for two main reasons, the first that 'in' is a very fast operation
#on sets. If we have a large collection of items that we want to use for a
#membership test, a set is more appropriate than a list:

#The second reason we use sets is to find the distinct items in a collection

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_items = len(item_set)
distinct_items_list = list(item_set)
print(f"{item_list},\n, {item_set}, \n, {distinct_items_list}")