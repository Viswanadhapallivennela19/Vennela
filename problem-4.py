# Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#   (examples)
#   input: [1,2,8,9,12,46,76,82,15,20,30]
#   Output: 
#     {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

 def listed_multiples(arr):
    obj={}
    for i in range(1,10):
        for j in range(len(arr)):
            if(arr[j]%i==0):
                obj[i]=obj.get(i,0)+1
        if i not in obj:
            obj[i]=0
    return obj
a=list(map(int,input("Enter list values : ").split(',')))
print("Result : ",listed_multiples(a))
