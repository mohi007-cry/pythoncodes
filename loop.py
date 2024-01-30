st = int(input("enter the starting number : "))
ed = int(input("enter the ending number : "))
ud = int(input("enter the upadating number : "))
rv= int(input("enter the value for row"))
if(rv==1):
    for i in range(st,ed,ud):
        print(i,end=' ')
elif(rv==2):
    for i in range(st,ed,ud):
        print(i)
else:
    print("invalid")