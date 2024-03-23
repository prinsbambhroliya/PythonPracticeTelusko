# 45. Module
# import calc_module as calc
# a = 9
# b = 6
# c = calc.add(a, b)
# d = calc.sub(a, b)
# e = calc.mul(a, b)
# f = calc.div(a, b)
# print(c)
# print(d)
# print(e)
# print(f)

# Special Variable _name
# import calc_module
# def main():
#     print("Hello World!")
#
# print("Demo Says:",__name__)
#
# main()
#
# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#
#     def config(self):
#         print("Config is ", self.cpu, self.ram)
#
# com1 = computer('i5','16')
# com2 = computer('Ryzen 3','8')
#
# com1.config()
# com2.config()

# 51.Constructor
# Size of an object ?
# > Depends on the no. of variables and size of each variable
# Who allocates size to object?
# > Constructor
# class computer:
#     def __init__(self):
#         self.name = "prinsbambhroliya"
#         self.age = 19
#     def compare(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
#     def update(self):
#         self.age +=1
#
# c1 = computer()
# c2 = computer()
#
# if c1.compare(c2):
#     print("They are the same")
# else:
#     print("They are not the same")
#
# c2.name = "mantrabambhroliya"
# c2.age = 15
#
# #obj.update()
# c1.update()
# print(c1.name,c1.age)
# print(c2.name, c2.age)

# 52.Types of variable

# class car:
#     airbag = 4

#     def __init__(self):
#         self.maker = "Mercedes"
#         self.color = 'red'
#         self.mileage = 10

# c1 = car()
# c2 = car()

# c1.mileage = 8 #Change in Only c1
# car.airbag = 5 #Change everywhere

# print(c1.color, c2.airbag, c1.maker, c1.mileage)
# print(c2.color, c2.airbag, c2.maker, c2.mileage)

# Accessor Methods
# Mutator Methods

# class student:

#     college = 'alphapix'

#     def __init__(self,m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3
    
#     @classmethod
#     def getcollege(cls):
#         return cls.college

#     @staticmethod
#     def info():
#         print("this is student class... in abc module")

#     # def get_m1(self):
#     #     return self.m1

#     # def set_m1(self):
#     #     self.m1 = value

        
# s1 = student(67,87,98)
# s2 = student(57,47,68)
    
# # print(s1.avg())
# print(s2.avg())
# print(student.getcollege())
# student.info()


# 54.Inner Class in Python

# class student:

#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno
#         self.lap = self.laptop()

#     def show(self):
#         print(self.name , self.rollno)
#         self.lap.show()

#     class laptop:
#         def __init__(self):
#             self.brand = 'Hp'
#             self.cpu = 'i5'
#             self.ram = 8

#         def show(self):
#             print(self.brand, self.cpu,self.ram)
            
# s1 = student('Prince',2)
# s2 = student('Navin',3)

# s1.show()
# # print(s1.name,s1.rollno)
# lap1 = student.laptop()



# 55.Inheritance in Python
# class A:
#     def feature1(self):
#         print("feature 1 Working")
        
#     def feature2(self):
#         print("feature 2 Working")

# #Inherit All The Feature From A
# class B(A):     #Child Class(Sub Class) Of A
#     def feature3(self):
#         print("feature 3 Working")

#     def feature4(self):
#         print("feature 4 Working")

# class C(B):
#     def feature5(self):
#         print("feature 5 Working")
# print("A .....")
# a1 = A()

# a1.feature1()
# a1.feature2()

# print("B ......")
# b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()

# print("C ........")
# c1 = C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()

#56.Constructors In Inheritance
# > Method Resolution Order(MRO) --> Left To Right
# class A:
    
#     def __init__(self):
#         print("in A Init")

#     def feature1(self):
#         print("feature 1-A Working")
        
#     def feature2(self):
#         print("feature 2 Working")

# #Inherit All The Feature From A
# class B:     #Child Class(Sub Class) Of A
    
#     def __init__(self):
#         super().__init__()
#         print("in B Init")

#     def feature1(self):
#         print("feature 1-B Working")

#     def feature3(self):
#         print("feature 3 Working")

#     def feature4(self):
#         print("feature 4 Working")

# class C(A,B):       #Left to right priority

#     def __init__(self):
#         super().__init__()      #Priority According Left to right
#         print("in C Init")    

# a1 = C()
# a1.feature1()

# 57.Polymorphism in Python Theory
# > Duck Typing
# > Operator Overloading
# > Method Overloading
# > Method Overriding

# A simple Python function to demonstrate 
# len() being used for a string
# print(len("geeks"))

# 58.Duck Typing
# Python program to demonstrate 
# duck typing 


# class Bird: 
# 	def fly(self): 
# 		print("fly with wings") 

# class Airplane: 
# 	def fly(self): 
# 		print("fly with fuel") 

# class Fish: 
# 	def swim(self): 
# 		print("fish swim in sea") 

# # Attributes having same name are 
# # considered as duck typing 
# for obj in Bird(), Airplane(), Fish(): 
# 	obj.fly() 

# 59.Operator Overloading
# Python Program illustrate how 
# to overload an binary + operator
# And how it actually works

# class A:
# 	def __init__(self, a):
# 		self.a = a

# 	# adding two objects 
# 	def __add__(self, o):
# 		return self.a + o.a 
# ob1 = A(1)
# ob2 = A(2)
# ob3 = A("Geeks")
# ob4 = A("For")

# print(ob1 + ob2)
# print(ob3 + ob4)
# # Actual working when Binary Operator is used.
# print(A.__add__(ob1 , ob2)) 
# print(A.__add__(ob3,ob4)) 
# #And can also be Understand as :
# print(ob1.__add__(ob2))
# print(ob3.__add__(ob4))

# 60.Method Overriding And Method Overloading
# Python program to demonstrate 
# method overriding 


# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 






