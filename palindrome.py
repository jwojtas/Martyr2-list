original = input ("Enter a string: ")
chkr = original[::-1] #reverses string
if original == chkr: #checks if reversed string is equal to original
  print ('\n{0} is a palindrome'.format(original))
else:
  print('\n Not a palindrome') 
  