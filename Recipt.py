items=[]
prices=[]
quants=[]
total=[]
for i in range(3):
    sum-0
    item=input("Enter item name")
    items.append(item)
    price=int(input("Enter price"))
    prices.append(price)
    quant=int(input("Enter Quantity"))
    quants.append(quant)
    sum=quant*price
    total.append(sum)
print("\n\n\n****************Reciept*******************\n")
print("items  !  Prices  !  Quant  !  Total")

for i in range(len(items)):
    print(items[i] + '\t ! \t ' , prices[i],"\t ! \t ",quants[i],"\t ! \t ",total[i])
sum1=0
for j in total:
    sum1=sum1+j
print("\nTotal Payable : ",sum1,"/-")     