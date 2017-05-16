#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
  sum = 0
  for i in nums:
      if i%2 == 0:
          sum += 1
  return sum


result = count_evens([2, 1, 2, 3, 4]);
print(result)