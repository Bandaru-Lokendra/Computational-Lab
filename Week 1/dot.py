l1=[]
l2=[]
sum=0
n=int(input("No of orders: "))
for i in range(n):
	a=int(input("Enter number: "))
	b=int(input("Enter number: "))
	l1.append(a)
	l2.append(b)
print("Vector1= ",l1)
print("Vector2= ",l2)
for i in range(len(l1)):
	sum+=l1[i]*l2[i]
print("Dot product: ", sum)	
