#Inheritance
class shape():
	def __init__(self):
		self.length=int(input("enter length :"))
		self.breadth=int(input("enter breadth:"))
	def show_dimension(self):
		print("Length of the shape :",self.length)
		print("Breadth of the shape :",self.breadth)


class shape_3D (shape):

	def __init__(self):
		super(). __init__()
		self.height = int(input("Enter Height :"))

	def show_dimension_3 (self) :
		super(). show_dimension()
		print ("Height of the shape : ", self.height)

print("====================")
s1=shape()
s1.show_dimension()
print("====================")

print("====================")
s2=shape_3D()
s2.show_dimension_3()
print("====================")
print("====================")