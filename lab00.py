from testcases import test_cases_q1, test_cases_q2, test_cases_q3

''' Strings Practice 
Fill in the '' to complete the code
'''


# QUESTION 1
def hello_world():
    """Below save a variable (message) as the string 'hello world'
       and return that variable

    >>> hello_world()
    hello world
    """
    #START CODE HERE
    message = ''
    #END OF CODE
    return message

test_cases_q1(hello_world()) 
print('')
print('')



# QUESTION 2
def add_strings():
  """Create a string variable ('balloon') return the sum of the string to itself
  >>> add_strings()
  balloonballoon
  """
  #START CODE HERE
  message = ''
  return ''
  #END OF CODE

test_cases_q2(add_strings())
print('')
print('')



# QUESTION 3 CHALLENGE
def count_and_replace():
  print('    Question 3')
  """Count the index of the string 
  ('12121212121212121212')
  
  Then replace that value in the string with the variable ('2')

  Hint 1: Try using .count and .replace  
  Hint 2: What index is '12121212121212121212'?

  >>> count_and_replace()
  22222222222222222222
  """
  original = '12121212121212121212'
  new = '2'
  #START CODE HERE
  count = ''
  new_message = original.replace(str(count), '') 
  #END OF CODE
  print(new_message)

test_cases_q3(count_and_replace())
