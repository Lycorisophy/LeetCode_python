class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            return False
        if carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            return False
        if carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            return False

if __name__ == '__main__':
    obj1 = ParkingSystem(1, 1, 0)
    print(obj1.addCar(1))
    print(obj1.addCar(2))
    print(obj1.addCar(3))
    print(obj1.addCar(1))
