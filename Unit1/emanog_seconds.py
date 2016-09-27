# 100 seconds is 0 hours, 1 minute, and 40 seconds
# 60 secs = 1 min
# 60 min = 1 hour
s = int(input("How many seconds?: "))
x = s % 60
m = s / 60 % x
h = m / 60
print(str(int(s)) + " seconds is " + str(int(h)) + " hours, " + str(int(m)) + " minutes, and " + str(int(x)) + " seconds")