class Car:
    """A simple attempt to reprsent a car"""
    def __init__(self, make, model, year):
        """init attributes to describe a car"""
        self.make = make 
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        '''return a neatly formated name'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        '''print a statement showing the cars mileage.'''
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("can't roll back odometer")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        

class ElectricCar(Car):
    '''represents aspects of an electric car'''
    def __init__(self, make, model, year):
        '''initialize attributes of the parent class with super then init for the attributes for the child class'''
        super().__init__(make,model,year)
        self.battery_size = 40
        self.battery=Battery()
    
    def fill_gas_tank(self):
        return print("this car doesn't have a gas tank!")
    
class Battery:
    '''a simple attempt to model a battery for an electric car.'''
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """describe the battery"""
        print(f"this car has a {self.battery_size}-kWh battery")
        return
    
    def get_range(self):
        '''print somthing about the range of the vehicle'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        '''increase the battery size and range'''
        self.battery_size = 65
        print('Vehicle battery upgraded.')