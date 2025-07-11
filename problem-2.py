def odd_series(val):
    result=[]
    for i in range(val*2+1):
        if(i%2==1):
            result.append(i)
    return result
a=int(input("Please Enter number :"))
print("Result :",odd_series(a))
