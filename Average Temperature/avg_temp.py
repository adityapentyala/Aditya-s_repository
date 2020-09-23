#calculates avg temperature of a week
temps = input("Enter temperatures of the 7 days: ").split(" ")
temps = [float(i) for i in temps]
print("Average temperature of the week is {:.1f}".format(sum(temps)/len(temps)))


