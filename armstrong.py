n = int(input("enter the number"))
temp = n
r = 0
temp1 = n
c = 0
while(temp1!=0):
    temp1 = temp1//10
    c = c+1
    
while(temp!= 0):
    q = temp %10
    r = r + q**c
    temp = temp//10
if(n==r):
    print("the number is armstrong")
else:
    print("the number is not armstrong")