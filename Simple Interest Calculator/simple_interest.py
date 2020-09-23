#simple interest calculator
prt = input("Enter principal amt., rate of interest(decimal) and time period: ").split(" ")
si = lambda data: int(data[0])*float(data[1])*float(data[2])
print(f"Simple Interest is {si(prt)}; total is {int(prt[0])+si(prt)}")


