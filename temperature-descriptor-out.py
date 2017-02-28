__metaclass__ = type
class CFt(property):
    pass

class Temperature():
    def __init__(self):
        self.ctemp = None
        self.ftemp = None

    def csetTemp(self, value):
        self.ctemp = value
        self.ftemp = value*1.8+32.0

    def fsetTemp(self, value):
        self.ftemp = value
        self.ctemp = (value-32.0)/1.8

    def cgetTemp(self):
        return self.ctemp
    def fgetTemp(self):
        return self.ftemp

    ct = CFt(fget=cgetTemp,fset=csetTemp)
    ft = CFt(fget=fgetTemp,fset=fsetTemp)
