import math
print("Ax^2 + Bx + C")

a = int(input("Enter A : "))

b = int(input("Enter B : "))

c = int(input("Enter C : "))

delta = (b*b)-(4*a)*(c)
if delta<0:
  print("This equation has no real root")
elif delta==0:
  print("Has one root")
  print(-b/(2*a))
else:
  print("Has 2 root")
  print((-b-math.sqrt(delta))/(2*a))
  print((-b+math.sqrt(delta))/(2*a))