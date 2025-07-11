def odd_series(val):
    result=[]
    num=val
    if val%2==0:
        num=val-1
    for i in range(num*2+1):
        if(i%2==1):
            result.append(i)
    return result
a=int(input("Please Enter number : "))
print("Result :",odd_series(a))
