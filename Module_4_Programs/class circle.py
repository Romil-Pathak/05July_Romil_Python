from math import pi

class Circle():
    def areacircle(self,radius):
        area=pi*radius*radius
        print(area)

    def perimetercircle(self,radius):
        perimeter=2*pi*radius
        print(perimeter)

a=Circle()
a.areacircle(10)
a.perimetercircle(10)
