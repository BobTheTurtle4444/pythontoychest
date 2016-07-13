# 23.py - This program demonstrates the use of tuples in Python. 
def sweet(candy):
	length = len(candy)
	vowels = set(['a', 'e', 'i', 'o', 'u'])
	hasVowels = bool(vowels.intersection(candy))
	tuple = (length,hasVowels)
	return(tuple)
ret = sweet("chocolate")
print(ret)
