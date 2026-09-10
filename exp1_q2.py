import math
ta= int(input("enter 1st side"))
tb= int(input("enter 2nd side"))
tc= int(input("enter 3rd side"))
s= (ta+tb+tc)/2
area = math.sqrt (s*(s-ta)*(s-tb)*(s-tc))
print ("Area of triangle = ",area) 
