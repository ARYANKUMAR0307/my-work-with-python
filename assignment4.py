marks = int(input("Enter your marks"))     

if marks<25:
    print("F")                            
elif marks>=25 and marks<45:
    print("E")                            
elif marks>=45 and marks<50:
    print("D")                            
elif marks>=50 and marks<60:
    print("C")                             
elif marks>=60 and marks<80:
    print("B")                             
else :
    print("A")                             

#QUESTION2

year = int(input("Enter your year"))            

if year%4==0 :                                 
    if year%100!=0 or year%400==0 :            
       print (year,"is a leap year")           
    else :
        print(year,"is not a leap year")       
else :
    print (year, "is not a leap year")        
    
#QUESTION3
from random import randint                     
n=0 
while n<10:                                    
    x=randint(0,9)
    y=randint(0,9)

    print("What is ",x,"times",y)
    guess=int(input("Enter your answer:"))    

    if guess==x*y:                            
        print("Correct")
    else:
        print("That is incorrect"," The correct answer is :",x*y) 
    n=n+1
else :
    print("Thank you for playing")            

#QUESTION4

for candies in range(200) :
    if candies%5 == 2 and candies%6 == 3 and candies%7 ==2 :  
      print("Number of candy are :",candies)                  
