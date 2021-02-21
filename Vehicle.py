#Parking Lot
class Vehicle:
	def __init__(self,register_number,color):
		self.color =  color
		self.register_number = register_number

class Car(Vehicle):

	def __init__(self,register_number,color):
		Vehicle.__init__(self,register_number,color)

