#fixnum_pkg.py
import math
class fixNum:
    def __init__(self, a,b):
        self.a=int(a)
        self.b=int(b)
        #Storing the length of b to help with decimal reconstruction
        self.precision=len(str(b)) if b>0 else 2

    def to_float(self):
        '''Converts the internal representation to a float for calculation'''
        return self.a +(self.b/10**self.precision)

    def from_float(value,precision=2):
        #Creates a fixNum object from a float result
        a=int(value)
        ''' (round..., 7) acts as a safety net to clean tiny binary errors at the 7th decimal place(safe choice)'''
        b=int(math.floor(round((value-a)*(10**precision),7)))
        return fixNum(a,b)
        
    def multiply(self,other):
        #Performs the multiplication task, converts both to floats to perform the math
        val1=self.to_float()
        val2=other.to_float()

        raw_result=val1*val2
        #Return as a new fixed-point number
        
        return fixNum.from_float(raw_result,self.precision)

    def __str__(self):
        return f"{self.a}.{self.b:0{self.precision}d}" #The 0 pads the integers to avoid confusion between 12.05 and 12.5 for example. 
        
    