
#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE
      if len(a)>len(b):
          return looping(a,b)
      else:
          return looping(b,a)

def looping(a,b):
    i = 0
    while(i< len(a)):
        i+=1
        if b == a[i:i+3]:
             return True
    return False          

result = end_other('Hiabc', 'abc') 
print(result)
