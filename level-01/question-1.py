#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    for x in range(len(nums)-2):
       if nums[x] == 1 and nums[x+1] == 2 and nums[x+2]==3:
           return True
    return False
        
result = arrayCheck([1, 1, 2, 4, 1])
print(result)