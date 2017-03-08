## Problem 1 ##
"""
Return true if the sequence of numbers 1,2,3
appears in the list somewhere
"""
def arrayCheck(nums):
    if (1 in nums and 2 in nums and 3 in nums):
        return True
    else:
        return False

print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,1,2,3]))

## Problem 2 ##
def stringBits(my_str):
    i = 0
    my_word = ""
    while i < len(my_str)+1:
        my_word += (my_str[i])
        i += 2
    print(my_word)

stringBits("Hello")
#stringBits("Hi")
stringBits("Heeololeo")
