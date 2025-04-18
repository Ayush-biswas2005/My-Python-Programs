#**Palindrome Checker**: Create a function that checks whether a given string is a palindrome (reads the same forward and backward).
# Ignore spaces and capitalization.
# str=input("Enter a string:")
# str1=str[::-1]
# print(str1)
# if (str1==str):
#     print(str+" is a Palindrome")
# else:
#     print(str+" is not a Palindrome")
#**Palindrome Checker**: Create a function that checks whether a given string is a palindrome (reads the same forward and backward).
# Ignore spaces and capitalization
def is_palindrome(s):
   s = s.replace(" ", "").lower()
   length = len(s)

   for i in range(length // 2):
      if s[i] != s[length - i - 1]:
         return False
   return True
word = input("Enter a string:")
if is_palindrome(word):
   print("It is a Palindrome!")
else:
   print("It is not a Palindrome.")
