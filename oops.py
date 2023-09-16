class calculator():
    def addition(self):
        q=int(input("Enter first number:"))
        r=int(input("Enter second number:"))
        print(q+r)
    def subtraction(self):
        q = int(input("Enter first number:"))
        r = int(input("Enter second number:"))
        print(q-r)
    def multiplication(self):
        q = int(input("Enter first number:"))
        r = int(input("Enter second number:"))
        print(q * r)
    def division(self):
        q = int(input("Enter first number:"))
        r = int(input("Enter second number:"))
        print(q/r)
c=calculator()
while True:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        x=int(input("enter the choice:"))
        if x==5:
            break
        if x==1:
            c.addition()
        if x==2:
            c.subtraction()
        if x==3:
            c.multiplication()
        if x==4:
#             c.division()
class perimeter():
    def circle(self):
        r=int(input("Enter the radius:"))
        j=2*3.14*r
        print("The perimeter of a circle is",j)
    def rectangle(self):
        h=int(input("enter the height:"))
        w=int(input("enter the width:"))
        y=2*(h+w)
        print("The perimeter of a rectangle is",y)
    def square(self):
        s=int(input("enter the side:"))
        o=4*s
        print("The perimeter of a square is",o)
d=perimeter()
while True:
    print("1.circle")
    print("2.Rectangle")
    print("3.Square")
    x=int(input("enter the choice:"))
    if x==4:
        break
    if x==1:
        d.circle()
    if x==2:
        d.rectangle()
    if x==3:
        d.square()
l=[]
class vehicle():
    def __init__(self):
        self.number=0
        self.name=0
        self.price=0
        self.wheel=0
    def add(self):
        self.number=int(input("enter the number:"))
        self.name=input("enter the name:")
        self.price=int(input("enter the priec:"))
        self.wheel=int(input("enter the wheel:"))


    def display(self):
        print("vehicle number",self.number)
        print("vehicle name",self.name)
        print("vehicle price",self.price)
        print("vehicle wheel",self.wheel)

while True:
    print("1.add")
    print("2.Display")
    x=int(input("enter the choice:"))
    if x==3:
        break
    if x==1:
        f = vehicle()
        f.add()
        l.append(f)
        print(l)
    if x==2:
        while True:
            print("1.2 wheeler")
            print("2.3 wheeler")
            print("3.4 wheeler")
            d=int(input("enter the choice:"))
            if d==4:
                break
            if d==1:
                for i in l:
                    if i.wheel==2:
                        i.display()
                        print("2 wheeler is displayed")
            if d==2:
                for i in l:
                    if i.wheel==3:
                        i.display()
                        print("3 wheeler is displayed")
            if d==3:
                for i in l:
                    if i.wheel==4:
                        i.display()
                        print("4 wheeler is displayed")





