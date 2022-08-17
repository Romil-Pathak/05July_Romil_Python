from math import pi
def surface_area_cyl(r,h):
    sur_area = 2*pi*r*(r+h)
    volume = pi*(r**2)*h
    print("surface area is: %0.2f" %sur_area) #print upto 2 decimal places
    print('Volume is: %0.2f' %volume) #print upto 2 decimal places
x=int(input("Enter the radius of cylinder:"))
y=int(input("Enter the height of the cylinder:"))
surface_area_cyl(x,y)

