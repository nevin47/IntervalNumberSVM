import numpy as np

class InterVal:
    ##Initialise the interval number
    def __init__(self,Lower,Upper):
        self.Upper = float(Upper)
        self.Lower = float(Lower)
        print "Init a new interval number :[",self.Lower,",",self.Upper,"]"
    
    ##Set the method of plus
    def IntervalNumPlus(self,b):
        newUpper = self.Upper + b.Upper
        newLower = self.Lower + b.Lower
        newInterNum = InterVal(newLower,newUpper)
        return newInterNum
    
    ##Set the method of minus
    def IntervalNumMinus(self,b):
        newUpper = self.Upper - b.Upper
        newLower = self.Lower - b.Lower
        newInterNum = [newLower,newUpper]
        return newInterNum
    
    ##Set the method of multiply
    def IntervalNumMulti(self,b):
        testArray = [self.Upper*b.Upper,self.Lower*b.Lower,self.Upper*b.Lower,self.Lower*b.Upper]
        newUpper = max(testArray)
        newLower = min(testArray)
        newInterNum = [newLower,newUpper]
        return newInterNum
    
    ##Set the method of devide
    def IntervalNumDevide(a,b):
        testArray = [a[0]/b[0],a[1]/b[0],a[1]/b[1],a[0]/b[1]]
        newUpper = max(testArray)
        newLower = min(testArray)
        newInterNum = [newLower,newUpper]
        return newInterNum
