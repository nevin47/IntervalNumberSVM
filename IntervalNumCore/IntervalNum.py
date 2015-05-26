import numpy as np

class Interval:
    ##Initialise the interval number
    def __init__(self,Lower,Upper):
        if Lower >= Upper:
            print "Illegle!"
        else:
            self.Upper = float(Upper)
            self.Lower = float(Lower)
            print "Init a new interval number :[",self.Lower,",",self.Upper,"]"
        
    ##Set the method of plus
    def IntervalNumPlus(self,b):
        newUpper = self.Upper + b.Upper
        newLower = self.Lower + b.Lower
        newInterNum = Interval(newLower,newUpper)
        return newInterNum
    
    ##Set the method of minus
    def IntervalNumMinus(self,b):
        newUpper = self.Upper - b.Upper
        newLower = self.Lower - b.Lower
        newInterNum = Interval(newLower,newUpper)
        return newInterNum
    
    ##Set the method of multiply
    def IntervalNumMulti(self,b):
        testArray = [self.Upper*b.Upper,self.Lower*b.Lower,self.Upper*b.Lower,self.Lower*b.Upper]
        newUpper = max(testArray)
        newLower = min(testArray)
        newInterNum = Interval(newLower,newUpper)
        return newInterNum
    
    ##Set the method of devide
    def IntervalNumDevide(self,b):
        testArray = [self.Upper/b.Upper,self.Lower/b.Lower,self.Upper/b.Lower,self.Lower/b.Upper]
        newUpper = max(testArray)
        newLower = min(testArray)
        newInterNum = Interval(newLower,newUpper)
        return newInterNum
        
    ##Set the method of output the Interval Number
    def IntervalOutput(self):
        print "This num is: [" , self.Lower , "," , self.Upper , "]"