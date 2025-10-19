class ParkingSystem(object):
    """
    A parking system that tracks availavle parking spots of three sizes:
    big, medium, and small. Cars can be added based on their type.

    carType values:
        1 -> bigcar
        2 -> medium car
        3 -> small car
    """
    def __init__(self, big, medium, small):
        """
        Initialize the ParkingSystem with the number of available spots for each car type.

        :param big: int - Number of big parking spots
        :param medium: int - Number of medium parking spots 
        :param small: int - Number of samll parking spots
        """

        # Dictionary to map carType to available parking spots 
        self.parkingspot = {
            1: big,     # Big car
            2: medium,  # Medium car
            3: small    # Small car 
        }
        

    def addCar(self, carType):
        """
        Try to park a car of the given thype. If there is at least one spot available,
        park the car and return True. Otherwise, return False.

        :param carType: int - Type of car (1=big, 2=medium, 3=small)
        :return: bool - True if the car was parked, False otherwise
        """

        # Check if the requested carType has available spots
        if self.parkingspot[carType] > 0:
            # Park the car by decrementing the available spot count
            self.parkingspot [carType] -= 1
            return True
        # No spot available for the given car type
        return False
    
# Test sample 1 (basic functionalty)
# Create a ParkingSystem with 1 big, 1 medium, and 0 small spots
ps = ParkingSystem(1, 1, 0)

print(ps.addCar(1))  # True: One big spot is available
print(ps.addCar(2))  # True: One medium spot is available
print(ps.addCar(3))  # False: No small spots available
print(ps.addCar(1))  # False: No big spots left

# # Test sample 2 (using all spots)
# ps = ParkingSystem(2, 2, 1)

# # Fill all available spots
# print(ps.addCar(1))  # True
# print(ps.addCar(1))  # True
# print(ps.addCar(2))  # True
# print(ps.addCar(2))  # True
# print(ps.addCar(3))  # True

# # Now all are full, next should return False
# print(ps.addCar(1))  # False
# print(ps.addCar(2))  # False
# print(ps.addCar(3))  # False

# # Test 3 (Invalid carType handling)
# ps = ParkingSystem(1, 1, 1)

# print(ps.addCar(4))  # False: Invalid carType (not 1, 2, or 3)
# print(ps.addCar(0))  # False: Invalid carType





