import Vehicle
import argparse
import sys


class ParkingLot:
	def __init__(self):
		self.availability = 0
		self.slot_num = 0
		self.num_of_occupied_slots = 0

	def createParkingLot(self,availability):
		self.slots = [-1] * availability
		self.availability = availability
		return self.availability

	def findSlot(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i

	def park(self,register_number,color):
		if self.num_of_occupied_slots < self.availability: 
			slot_num = self.findSlot()
			self.slots[slot_num] = Vehicle.Car(register_number,color)
			self.slot_num = self.slot_num+1
			self.num_of_occupied_slots = self.num_of_occupied_slots + 1
			return slot_num+1
		else:
			return -1

	def leave(self,slot_num):

		if self.num_of_occupied_slots > 0 and self.slots[slot_num-1] != -1:
			self.slots[slot_num-1] = -1
			self.num_of_occupied_slots = self.num_of_occupied_slots - 1
			return True
		else:
			return False

	def status(self):
		print("Slot No.\tRegistration No.\tColour")
		for i in range(len(self.slots)):
			if self.slots[i] != -1:
				print(str(i+1) + "\t\t" +str(self.slots[i].register_number) + "\t\t" + str(self.slots[i].color))
			else:
				continue

	def find_register_numbers_from_Color(self,color):

		register_numbers = []
		for i in self.slots:

			if i == -1:
				continue
			if i.color == color:
				register_numbers.append(i.register_number)
		return register_numbers
			
	def find_slot_numbers_from_register_numbers(self,register_number):
		
		for i in range(len(self.slots)):
			if self.slots[i].register_number == register_number:
				return i+1
			else:
				continue
		return -1
			

	def find_slot_numbers_from_color(self,color):
		
		slot_numbers = []

		for i in range(len(self.slots)):

			if self.slots[i] == -1:
				continue
			if self.slots[i].color == color:
				slot_numbers.append(str(i+1))
		return slot_numbers

	def display(self,line):
		if line.startswith('create_parking_lot'):
			n = int(line.split(' ')[1])
			res = self.createParkingLot(n)
			print('Created a parking lot with '+str(res)+' slots')

		elif line.startswith('park'):
			register_number = line.split(' ')[1]
			color = line.split(' ')[2]
			res = self.park(register_number,color)
			if res == -1:
				print("Sorry, parking lot is full")
			else:
				print('Allocated slot number: '+str(res))

		elif line.startswith('leave'):
			leave_slot_num = int(line.split(' ')[1])
			status = self.leave(leave_slot_num)
			if status:
				print('Slot number '+str(leave_slot_num)+' is free')

		elif line.startswith('status'):
			self.status()

		elif line.startswith('registration_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			register_numbers = self.find_register_numbers_from_Color(color)
			print(', '.join(register_numbers))

		elif line.startswith('slot_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			slot_numbers = self.find_slot_numbers_from_color(color)
			print(', '.join(slot_numbers))

		elif line.startswith('slot_number_for_registration_number'):
			register_number = line.split(' ')[1]
			slotno = self.find_slot_numbers_from_register_numbers(register_number)
			if slotno == -1:
				print("Not found")
			else:
				print(slotno)
		elif line.startswith('exit'):
			exit(0)

def main():

	parkinglot = ParkingLot()
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
	args = parser.parse_args()
	
	if args.src_file:
		with open(args.src_file) as f:
			for line in f:
				line = line.rstrip('\n')
				parkinglot.display(line)
	else:
			while True:
				line = input("Enter Command: $ ")
				parkinglot.display(line)

if __name__ == '__main__':
	main()