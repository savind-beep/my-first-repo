''']
C=1
ET=0
while C<=4:
    ET=int(input("enter the engine ",C,"temp"))
    L.append(ET)
    C=C+1
for i in range(len(L)):
    if 200 < L[i] < 850:
        SC=SC+1
        print("Engine", i+1, "Safe")0
    else:
        DC=DC+1
        print("Engine", i+1, "Meintenance required")

print("Safe engines",SC)
print("Meintenance required",DC)'''

N=int(input("enter the number:"))
TN=1
while N!=0:
    TN=N*TN
    N=N-1
print("the factorial of the number is:",TN)

