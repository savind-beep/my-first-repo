'''D=float(input("Enter the distance in km:"))
FA=float(input("Enter the fule efficiency:"))
FP=float(input("Enter the fuel price:"))
HC=float(input("Enter the highway cost:"))
FU=float(D/FA)
TC=FU*FP+HC
print("The total cost of the trip is:",TC)'''

'''BC=float(input("enter the bacsic salary:"))
OH=float(input("enter the over time hours:"))
OR=float(input("enter the over time rate:"))
B=float(input("enter the bonus:"))
T=float(input("enter the tax:"))
OT=OH*OR
GS=BC+OT+B
TD=GS*(T/100)
NS=GS-TD
print("The net salary is:",NS)
print("The net salary is:",NS)'''

'''A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
C=0
print=(A,B)
C=A
B=A
C=B
print=(A,B)'''

'''A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
if A>B:
    print("The biggest number is:",A)   
else :
    print("The biggest number is:",B)'''

'''Num1=int(input("Enter the first number:"))
if Num1>=0:
    print("The number is positive.")
else:
    print("The number is negative.")'''

''''SM=int(input("Enter the marks:"))
if SM>=50:
    print("Passed")
else:   
     print("Failed")'''

'''AGE=int(input("Enter the age:"))
if AGE>=18:
    print("You are eligible to vote.")  
else:    print("You are not eligible to vote.")'''

'''Num1=int(input("Enter the first number:"))
if Num1%2==0:
    print("The number is even.")        
else:    print("The number is odd.") '''
'''NUM1=int(input("Enter the first number:"))
if NUM1>0:
    print("The number is positive.")        
elif NUM1<0:    print("The number is negative.") 
else:    print("The number is zero.")'''

'''SM=int(input("Enter the marks:"))
if 90<=SM<=100:      
    print("Grade A")
elif 88<=SM<=89:
    print("Grade B")
elif 70<=SM<=79:
    print("Grade C")
elif 60<=SM<=69:
    print("Grade D")        
elif 50<=SM<=59:
    print("Grade E") 
else:    print("Grade F")'''

'''FN=int(input("Enter the first number:"))
SN=int(input("Enter the second number:"))
OP=input("Enter the operator (+, -, *, /):")    
if OP=='+':
    result=FN+SN
    print("The result is:",result)
elif OP=='-':
    result=FN-SN
    print("The result is:",result)
elif OP=='*':
    result=FN*SN
    print("The result is:",result)
elif OP=='/':
    result=FN/SN
    print("The result is:",result)
else:
    print("Invalid operator")'''  
#calori count 
'''ED=int(input("enter the exercise duration in minutes:"))
CBC=float(input("enter the calories burned per minute:"))
TC=ED*CBC            
print("The total calories burned is:",TC)')'''

''''SA=int(input("Enter the Attendance: "))
if SA>=80:
    AM=int(input("Enter the Average Mark: "))
    if AM>75:
        print("scholarship granted")
    else:        print("scholarship not granted")
else:   
    print("insufficient attendance, scholarship not granted")'''

'''PM=str(input("premium member (yes/no):" ))
if PM=="yes": 
       print("discount applied")
       BA=float(input("Enter the bill amount:"))
       if BA>=10000:
              TBM=BA*(20/100)
              print("The total bill amount is:",TBM)
            
         else:              
            TBM=BA*(10/100)
            print("The total bill amount is:",TBM)  
else:
    print("no discount applied")
    BA=float(input("Enter the bill amount:"))
    print("The total bill amount is:",BA)'''


'''PS=int(input("Enter the performance score:"))
if PS>=85:
    SY=int(input("Enter the years of service:"))
    if SY>3:
        print("Promotion approved")
    else:        print("more experience required")
else:  
     print("Promotion not approved") '''

'''UC=int(input("Enter the units consumed:"))
if 0<=UC<=30:
    TBL=UC*20
    print("The total bill amount is:",TBL)
elif 31<=UC<=60:
    TBL=30*20+(UC-30)*40
    print("The total bill amount is:",TBL)
elif 60<UC: 
    TBL=30*20+(30*40)+(UC-60)*60
    print("The total bill amount is:",TBL)'''

'''EA=int(input("Enter your Age"))
CIT=str(input("Are you Citzen in sri lanka "))
if EA  >=18:
 if CIT=="yes":
  print("your Eligible to vote ")
 else :
  print("you are not eligible to vote ")
else:
 print("you are not eligible to vote ")'''


'''PIN=int(input("Enter the pin number:")) 
AB=20000
if PIN==1234:
    print("Access granted") 
    WB=float(input("Enter the withdrawal amount:"))
    if WB<=AB:
        AB=AB-WB
        print("Withdrawal successful. Remaining balance:",AB)
    else:
        print("Insufficient balance. Withdrawal denied.")   
else:  
     print("Access denied. Incorrect pin number.")'''

'''SM=int(input("Enter the marks:"))
FI=float(input("enter the family income:"))
if SM>=75:
    if FI<50000:
        print("Scholarship granted")
    else:        print("Scholarship not granted due to high family income")
else:  
        print("Scholarship not granted due to low marks")'''   

'''RE=str(input("are you registered:"))
EF=str(input("DID you pay the exam fee:"))
if RE=="yes" and EF=="yes":
    print("you are eligible to sit for the exam")
else:   
      print("you are not eligible to sit for the exam")'''



      


