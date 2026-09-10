CN=str(input("enter the cashier name "))#CN=cashier name
CUN=str(input("enter the customer name "))#CUN=customer name
CG=int(input("customer category "))#CG=customer category
CGL=["Adult","Student","Child"]
index=CG-1
CG=CGL[index]
#ticket price VIP=1500
#ticket price Standard=1000
#ticket price Child=500
C=-1
R=int(input("enter the number "))#R=Round
while C!=R:
    SNL=[]
    TTL=[]
    TPL=[]
    SN=str(input("enter the seat number "))#SN=seat number
    TTI=str(input("enter the ticket type "))#TT=ticket type input
    TT=["standard","Premium","VIP"]
    TP=[1500,1000,500]
    if TTI=="standard":
        index=0 
    elif TTI =="Premium":
        index=1
    elif TTI=="VIP":
        index=2
    SNL.append(SN)
    TTL.append(TT[index])   
    TPL.append(TP[index])
SO=str(input("Do you need a snack? (yes/no)"))#Snack order
SL=[]#SL=Snack list
SP=[]#SP=Snack price    
if SO=="yes":    
    S=str(input("enter the snack name:"))#S=Snack name
    SP=int(input("enter the snack price:"))#SP=Snack price
    SL.append(S)
    SP.append(SP)
else:
 print("No snack ordered")
if len(TPL) > 0:
    total_cost = sum(TPL)
    highest_price = max(TPL)
    lowest_price = min(TPL)
    average_price = total_cost / len(TPL)

    print("Total Ticket Cost :", total_cost)
    print("Highest Price     :", highest_price)
    print("Lowest Price      :", lowest_price)
    print("Average Price     :", average_price)
else:
    print("No tickets have been added.")

for i in range(len(TT)):
    SC=0#standard count
    PC=0#premium count
    VC=0#VIP count
    if TT[i] == "standard":
        SC += 1
    elif TT[i] == "Premium":
        PC += 1         
    elif TT[i] == "VIP":
        VC += 1
print("Standard Count:", SC)
print("Premium Count :", PC)
print("VIP Count     :", VC)
        

