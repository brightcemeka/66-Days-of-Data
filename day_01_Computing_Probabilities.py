#Samples Space is the set of all possible outcomes an aciton could produce.
#For a Coin flip action the possible outcomes are Heads or Tails.

sample_space = {'Heads', 'Tails'} #This is a pythong set, it stores unique, unordered elements.

#suppose we choose an element from sample_space at random the probability will be 1/len(sample_space).

#Computing probability of heads.
probability_heads = 1 / len(sample_space)
print(f'Probability of choosing heads is {probability_heads}')

#An Event condition is a simple Boolean (yes-or-no, true-or-false) function whose input is a single sample_space element.

#Defining Event conditions
def is_heads_or_tails(outcome):
    return outcome in {'Heads', 'Tails'}

def is_neither(outcome):
    return not is_heads_or_tails(outcome)

def is_heads(outcome):
    return outcome == 'Heads'
def is_tails(outcome):
    return outcome == 'Tails'

#Defining an event-detection function
def get_matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space
                if event_condition(outcome)])

event_conditions = [is_heads_or_tails, is_heads, is_tails, is_neither]

for event_condition in event_conditions:
    print(f"Event Condition: {event_condition.__name__}")
    event = get_matching_event(event_condition, sample_space)
    print(f'Event: {event}\n')

#The probability we showed earlier was for a single-element outcome for a fair coin which was 1/len(sample_sapce).
#We can generalize this to include multi-element events, to be len(event)/len(sample_space) only if all outcomes are known to occur with equal likelihood

#Computing Event Probabilities.
def compute_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    return len(event) / len(generic_sample_space)

for event_condition in event_conditions:
    prob = compute_probability(event_condition, sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name} is {prob}")


#PLEASE NOTE: - 0.0 and 1.0 are the lower and upper bounds of probabilty; no probability can ever fall below 0.0 or rise above 1.0


#Analyzing a biased coin
#To compute the likelihoods of outcomes that are not weighted in an equal manner, we construct a weighted sample space represented by a Python dictionary.
# each outcome is treated as a key whose value maps to the associated weight. In our example, Heads is weighted four times as heavily as Tails, so we map Tails to 1 and Heads to 4.

#Representing a weighted sample space
weighted_sample_space = {'Heads': 4, 'Tails': 1}

sample_space_size = sum(weighted_sample_space.values())
assert sample_space_size == 5
#Checking the weighted event size
event = get_matching_event(is_heads_or_tails, weighted_sample_space)
event_size = sum(weighted_sample_space[outcome] for outcome in event)
assert event_size == 5

#Defining a generalized event probability function

def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()):
        return len(event) / len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome]
                     for outcome in event)
    return event_size / sum(generic_sample_space.values())

for event_condition in event_conditions:
    prob = compute_event_probability(event_condition, weighted_sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name}' is {prob}")



#PROBLEM 01: Analyzing a family with four children
"""
Suppose a family has four children. What is the probability that exactly two of the children are boys? We'll assume that each child is equally likely to be either a boy or a girl.
Thus we can construct an unweighted sample space where each outcome represents one possible sequence of four children, as shown in figure 1.2
Figure 1.2
[
B, B, B, B
B, B, B, G,
B, B, G, B,
B, G, B, B,
G, B, B, B,
G, G, B, B,
G, B, B, G,
B, B, G, G,
B, G, B, G,
G, B, G, B,
B, G, G, B,
B, G, G, G,
G, G, G, B,
G, B, G, G,
G, G, B, G
G, G, G, G,
]
"""

#copmuting the sample space of children
possible_children = ['Boy', 'Girl']
sample_space = set()
for child1 in possible_children:
    for child2 in possible_children:
        for child3 in possible_children:
            for child4 in possible_children:
                outcome = (child1, child2, child3, child4)
                sample_space.add(outcome)

from itertools import product
all_combinations = product (*(4 * [possible_children]))
assert set(all_combinations) == sample_space

#Passing repeat into product
sample_space_efficient = set(product(possible_children, repeat=4))
assert sample_space == sample_space_efficient

#Let's calc. the fraction of sample_space that is composed of families with two boys.

#Computing the probability of two boys

def has_two_boys(outcome):
    return len([child for child in outcome
                if child == 'Boy']) == 2

prob = compute_event_probability(has_two_boys, sample_space)
print(f"Probability of 2 boys is {prob}")
