n=int(input("Enter a number: "))
a=[]
while(n>0):
    fun=n%2
    a.append(fun)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
