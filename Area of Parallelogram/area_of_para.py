#area of parallelogram
dim = input("Enter base, height: ").split(" ")
area = lambda dim: int(dim[0]) * int(dim[1])
print(f"Area is {area(dim)}")


