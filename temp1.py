temp1 = int(input("enter the temp1 : "))
if(temp1<=0):
    print("weather is snowy")
elif(temp1>0 and temp1<=20):
    print("weather is cold")
elif(temp1>=21 and temp1<=40):
    print("weather is hot ")
else:
    print("death")
