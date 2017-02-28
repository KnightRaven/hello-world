__metaclass__ = type
class Ct():

    def __get__(self, instance, owner):
        return instance.ctemp
    def __set__(self, instance, value):
        instance.ctemp = value
        instance.ftemp = value *1.8+32.0

class Ft():

    def __get__(self, instance, owner):
        return instance.ftemp
    def __set__(self, instance, value):
        instance.ftemp = value
        instance.ctemp = (value-32.0)/1.8

class Temperature():

    ct = Ct()
    ft = Ft()
