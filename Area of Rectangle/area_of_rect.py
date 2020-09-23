#area of rectangle
dim = input("Enter length, breadth: ").split(sep=" ")
area = lambda dim: int(dim[0]) * int(dim[1])
print(f"Area is {area(dim)}")


