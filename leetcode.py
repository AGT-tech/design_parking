class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parkingspot = {
            1: big, 
            2: medium,
            3: small    
        }
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.parkingspot[carType] > 0:
            self.parkingspot [carType] -= 1
            return True
        return False
    






