class Calculator:
    
    def __init__(self, x):
        self.x = x
        
    def __add__(self, other):
        result_add = self.x + other.x
        return result_add
    
    def __sub__(self, other):
        result_sub = self.x - other.x
        return result_sub
    
    def __mul__(self, other):
        result_mul = self.x * other.x
        return result_mul
    
    def __truediv__(self, other):
        result_div = self.x / other.x
        return result_div

x, y = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(x)),Calculator(int(y))
print(x+y, x-y, x*y, x/y, sep="\n")