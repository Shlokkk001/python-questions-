
seconds=int(input("Enter the number of seconds:"))
hours = seconds//3600
remaining = seconds%3600
minutes= remaining//60
seconds= remaining%60
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds) 