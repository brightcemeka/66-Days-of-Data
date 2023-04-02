#args and kwargs
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")

#I am so tired and exhausted, I will just use the below code as a playground:

#here is a while statement:
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        print("Blastoff!")


countdown(30)

#Good night, see you tomorrow.

