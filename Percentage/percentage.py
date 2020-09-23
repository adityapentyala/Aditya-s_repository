#marks, percent
name = input("Enter name: ")
marks = input("Enter marks: ").split(" ")
marks = [int(i) for i in marks]
total = sum(marks)
print(f"{name} scored {total} at a percentage of {total/3}")


