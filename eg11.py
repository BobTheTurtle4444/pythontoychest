# 11.py - This program is about tuples. Tuples are immutable, but they can be combined to create a third tuple. 
# One good use of a tuple is in a function which returns more than one value.
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print(tup1)
print(tup2)
print(tup3)
