original = input ("Enter a string: ")
chkr = original[::-1]
if original == chkr:
  print ('\n{0} is a palindrome'.format(original))
else:
  print('\n Not a palindrome') 
  