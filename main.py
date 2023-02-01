print("Input lengths of each of the three sides: ")
x = int(input("First Side or X: "))
y = int(input("Second Side or Y: "))
z = int(input("Third Side or Z: "))

if x == y == z:
	print("The Triangle is Equilateral triangle")
elif x==y or y==z or z==x:
	print("The Triangle is not equilateral")
else:
	print("The Triangle is not equilateral")
