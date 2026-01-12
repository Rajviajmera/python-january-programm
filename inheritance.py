#Inheritance
class shape():
	def __init__(self):
		self.length=int(input("enter length :"))
		self.breadth=int(input("enter breadth:"))
	def show_dimension(self):
		print("Length of the shape :",self.length)
		print("Breadth of the shape :",self.breadth)
s1=shape()
s1.show_dimension()

s2=shape()
s2.show_dimension()