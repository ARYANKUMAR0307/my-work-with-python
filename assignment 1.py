"""
1.
Write a Python program to find average of three numbers entered by the user.
"""

a=int(input("Enter first no."))
b=int(input("Enter second no."))
c=int(input("Enter third no."))
d=(a+b+c)/3
print("Average is",d)







"""
2.
Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate
"""

a=float(input("Enter gross income nearest to penny:"))
b=int(input("Enter no. of dependents:"))
c=a-10000-3000*b
e=(c*2)//10
print("Amount of tax is:",e)




"""
3.
Write a python program to store different data type values into a list. (For an
example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5).
"""

a=int(input("Enter your SID:"))
b=str(input("Enter your name:"))
c=str(input("Enter your gender as F,M,U:"))
d=str(input("Enter your course name:"))
e=float(input("Enter you CGPA:"))
l=[a,b,c,d,e]
print(l)


      
      
"""
4.
Write a python program to enter marks of 5 students into a list and display
them in sorted manner.
"""

a=int(input("Enter first no."))
b=int(input("Enter second no."))
c=int(input("Enter Third no."))
d=int(input("Enter fourth no."))
e=int(input("Enter fifth no."))
x=[a,b,c,d,e]
x.sort()
print("Sorted list",x)







"""
5.
List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a. Write a Python program to print a specified list after removing 4th element.
Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
Do that in one line code.
"""


list=['RED','GREEN','WHITE','BLACK','PINK','YELLOW']
list[4] = "PURPLE"
print(list)
list[0]='BLUE'
print(list)
list[2:3] = "purple"
print(list)




