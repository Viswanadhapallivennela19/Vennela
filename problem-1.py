class calculator:
    def __init__(self,a,b,type):
        self.val1=a
        self.val2=b
        self.operation=type
    def calculate(self):
        match self.operation.lower():
            case "div" :
                return self.val1/self.val2
            case "mul" :
                return self.val1*self.val2
            case "add" :
                return self.val1+self.val2
            case "sub":
                return self.val1-self.val2
            case _:
                return  "You Entered Wrong operation"
a=int(input('Enter first number : '))
b=int(input('Enter another number : '))
operation=input('Enter the Operation (div,mul,add,sub) : ')
obj=calculator(a,b,operation)
print("Result : ",obj.calculate())
