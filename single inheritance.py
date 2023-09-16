# class A:#This is the parent class
#     def display(self):
#         print("Hello")
# class B(A):#This is the child class in which child B is taking inheritance of A
#     def display1(self):
#         print("welcome")
# b=B()#Creating an object
# b.display()
# b.display1()

# class A:#This is the parent class
#     def display(self):
#         print("Hai")
# class B:#This is 2nd parent child
#     def display1(self):
#         print("Hello")
# class C(A,B):#here A and B is inherited here
#     def display2(self):
#         print("Welcome")
# D=C() #object creating
# D.display()
# D.display1()
# D.display2()

# class A:
#     def display(self):
#         print("hi")
# class B(A):#B is inheriting A
#     def display1(self):
#         print("Hello")
# class C(B): #C is inheriting B and B also contains A so C contains A and B
#     def display2(self):
#         print("welcome to")
# class D(C):#D is inheriting C
#     def display3(self):
#         print("softronics")
# E=D()#creating object
# E.display()

# E.display1()
# E.display2()
# E.display3()
# class A:
#     def display(self):
#         print("hi")
# class B(A):
#     def display1(self):
#         print("hello")
# class C(A):
#     def display2(self):
#         print("welcome")
# D=C()
# D.display()
# D.display2()#in C B is not inherited so we are creating B as another object
# E=B()
# E.display()
# E.display1()

# class A:
#     def display(self):
#         print("1")
# class B(A):
#     def display1(self):
#         print("2")
# class C(A):
#     def display2(self):
#         print("3")
# class D(B,C):
#     def display3(self):
#         print("4")
# class E(C):
#     def display4(self):
#         print("5")
# class F(D,E):
#     def display5(self):
#         print("6")
# g=F()#creating object
# g.display()
# g.display1()
# g.display2()
# g.display3()
# g.display4()
# g.display5()
class student:
    def __init__(self):
        self.x="Hello"
class teacher(student):
    def __init__(self):
        super().__init__()
        self.y="welcome"
    def display(self):
        print(self.x)
        print(self.y)
t=teacher()
t.display()
