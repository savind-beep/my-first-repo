'''D=float(input("Enter the distance in km:"))
FA=float(input("Enter the fule efficiency:"))
FP=float(input("Enter the fuel price:"))
HC=float(input("Enter the highway cost:"))
FU=float(D/FA)
TC=FU*FP+HC
print("The total cost of the trip is:",TC)'''

BC=float(input("enter the bacsic salary:"))
OH=float(input("enter the over time hours:"))
OR=float(input("enter the over time rate:"))
B=float(input("enter the bonus:"))
T=float(input("enter the tax:"))
OT=OH*OR
GS=BC+OT+B
TD=GS*(T/100)
NS=GS-TD
print("The net salary is:",NS)
