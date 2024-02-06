n = int(input("enter the number"))
temp = n
r = 0
while(temp > 0):
    q = temp %10
    r = (r *10) +q
    temp = temp//10
if(n==r):
    print("the number is palindrome")
else:
    print("the number is not palindrome")
    
