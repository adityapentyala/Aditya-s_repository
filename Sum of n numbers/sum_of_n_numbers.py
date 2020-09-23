#prints sum of n numbers
numbers = input("Enter the numbers: ").split(" ")
numbers = [int(i) for i in numbers]
print(f"The sum is {sum(numbers)}")


