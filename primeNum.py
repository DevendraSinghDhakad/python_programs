num = int(input("enter a num:"))

if(num>1):
    for i in range(2,int(num/2)+1):
        if(num%i)==0:
            print(num,"is not a prime num")

            break
    else:
            print(num,"is  a prime num")

else:
    print(num,"is not a prime num")           





