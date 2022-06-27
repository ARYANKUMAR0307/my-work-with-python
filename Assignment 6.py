# Program to check whether a number is perfect or not_1

n=int(input("Enter a number: "))
sum = 0
for i in range(1,n):
      if n%i == 0:
         sum += i
if sum == n:
      print("Entered number is a perfect number")
else :
      print("Entered number is not a perfect number")
    
    
# Program for checking whether a string is palindrome or not_2

a=input("Enter a string: ")
a=a.replace(" ","")
a=a.lower()
a_reverse=a[::-1]
if a==a_reverse :
    print("String is palindrome")
else :
    print("String is not palindrome")
    
    
#Program for printing pascal's triangle _3
import math
from math import factorial
n=int(input("Enter a nunmber: "))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")                                                 #for spacing
        
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")    #by the definition of nCr
 
    print()
  
  
#Program for checking whether a string is pangram or not
string=input("Enter a string: ")
alphabets="abcdefghijklmnopqrstuvwxyz"
string=string.lower()
string=string.replace(" ","")
for i in alphabets:
    if i not in string:
        print("Given string is not a pangram")
    else:
        print("Given string is a pangram")
        
