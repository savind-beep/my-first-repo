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
'''RA=str(input("are ther eny rooms avelble "))
if RA=="yes":
    ID=str(input("DO you have id :"))
    if ID=="yes":
        HF=int(input("did they pay the Advance:"))
        if HF=="yes":
         SD=int(input("how many days do you want to stay:"))
          if SD>=1:
            print("room booked successfully")   
          else:
            print("invalid number of days")
        else:
            print("advance payment required to book the room")
    else:     
       print("ID required to book the room")  
else:   
   print("no rooms available")'''            


'''YN=str(input("enter your name:"))
C=0
while C<5:
    print("my name is ",YN)
    C=C+1'''

'''N=int(input("enter the number:"))
C=0
while C<=5:
    print(N)
    N=N+1
    C=C+1'''

'''N=int(input("enter the number:"))
while N!=20:
    print(N)
    N=N+2'''
    

'''N=int(input("enter the number:"))
while N!=0:
    print(N)
    N=N-6'''

'''N=int(input("enter the number:"))
while N!=11:
    MV=N*N
    print(MV)
    N=N+1'''#
'''C=0
while C<=10:
    T=int(input("enter the number:"))
    FT=FT+T
    C=C+1
    print("the total sum is:",FT)


BW=int(input("enter the beggege weight:"))
if BW<=20:
    print("no extra charge")    
elif 20<BW<=30:
    EC=(BW-20)*200
    print("the extra charge is:",EC)
elif BW>30:
    print("this baggege is not allowed")

MS=int(input("enter the salary:"))
if 50000<=MS<=99999:
    IT=MS*(10/100)
    print("your bonus is:",IT)
elif MS>=100000:
    IT=MS*(15/100)
    print("your bonus is:",IT)
else: MS<50000    
IT=MS*(5/100)
print("your bonus is:",IT)


C=0
while C<=10:
    M=int(input("enter the marks:"))
    TM=TM+M
    C=C+1
AV=TM/10
if AV>=50:
    print("passed") 
else:  
    print("failed")



while N!=(-1):
    N=int(input("enter the number:"))
    TN=TN+N
print("the total sum is:",TN)


W=str(input("enter the word:"))
W=W.lower()
C=0
for i in range(len(W)):
    if W[i] in {'a','e','i','o','u'}:
        C=C+1
print("the number of vowels in the word is:",C)'''

'''N=int(input("enter the number:"))
TN=1
while N!=0:
    TN=N*TN
    N=N-1
print("the factorial of the number is:",TN)


while N!=(-1):
  Age=int(input("enter the age:"))
  if Age>=18:
        print("eligible to vote")
        else:  
        print("not eligible to vote")
print("program ended")'''


'''I=0
while I>= 5:
    J=5
    while J>=0:
        print("*",end="")
        J=J-1
print ("\n")
I=I+1'''


'''C=1
TC=0
while C<=5:
    TC=TC+C
    C=C+1
print(TC)'''

'''TC=0
C=1
while C<=5:
    A=int(input("enter the number"))
    TC=TC+A
    C=C+1
print("youer totle is",TC)'''

'''O=E=0
C=1
while C<=5:
    NUM=int(input("enter your number "))
    if NUM%2==0:
        E=E+1
    else:
        O=O+1
    C=C+1
print("even num",E) 
print("odd num",O)'''

'''C=1
while C<=3:
    B=1
    while B<=3:
      print(B,end=" ")
      B=B+1
      
    C=C+1
    print()'''

'''C=1
while C<=5:
    B=1
    while B<=4:
      print("*",end=" ")
      B=B+1
      
    C=C+1
    print()'''

'''for i  in range(1,5):
    for J in range (i):
        print("*",end= " ")
    print()'''

'''TC=1
N=int(input ("enteryou number "))
while N!=1:
    TC=TC*N
    N=N-1
print(TC)'''

'''TC=1
I=int(input("enter youer num"))
for I in range (0+1,I):
    TC=TC*I
print(TC)'''

'''N = int(input("Enter the number: "))

if N <= 1:
    print("This number is not prime")
elif N == 2:
    print("This number is prime")
elif N % 2 == 0:
    print("This number is not prime")
else:
    print("This number is prime")'''


'''TS=C=0
D_sales=[]
while C<=7:
    S=int(input("enter the daily sales"))
    D_sales.append(S)
    C=C+1
print(D_sales)'''

M_N=[]
T_P=[]
S_N=[]
x=int(input("enter the key:"))
while x!=0:
    M_N.append(str(input("enter the movie name:")))
    T_P.append(float(input("enter the Ticket price :")))
    S_N.append(float(input("enter the booked seats number:")))
    x=int(input("enter the key:"))
    
print(f"{'MOVIE NAME':<15}{'TICKET PRICE':<15}{'BOOKED SEATS':<15}")
print ("-"*50)
for i in range(len(M_N)):
    print(f"{M_N[i]:<15}{T_P[i]:<15}{S_N[i]:<15}")
