# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass

class GroundVehicle(Vehicle):
    """Parent is Vehicle"""
    pass

class Car(GroundVehicle):
    """Parent is GroundVehicle"""
    pass

class Motorcycle(GroundVehicle):
    """Parent is GroundVehicle"""
    pass

class FlightVehicle(Vehicle):
    """Parent is Vehicle"""
    pass

class Airplane(FlightVehicle):
    """ Parent is FlightVehicle"""
    pass

class Starship(FlightVehicle):
    """Parent is Vehicle"""
    pass
    