# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class calculator:
    def __init__(self,a,b,type):
        self.val1=a
        self.val2=b
        self.operation=type
    def calculate(self):
        match self.operation.lower():
            case "div" :
                if self.val2!=0:
                    return self.val1/self.val2
                else:
                    return "Infinity"
            case "mul" :
                return self.val1*self.val2
            case "add" :
                return self.val1+self.val2
            case "sub":
                return self.val1-self.val2
            case _:
                return  "You Entered Wrong operation"
a=float(input('Enter first number : '))
b=float(input('Enter another number : '))
operation=input('Enter the Operation (div,mul,add,sub) : ')
obj=calculator(a,b,operation)
print("Result : ",obj.calculate())
