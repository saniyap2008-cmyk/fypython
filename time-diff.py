m1 = int(input("Enter minutes of timestamp 1: "))
s1 = int(input("Enter seconds of timestamp 1: "))
m2 = int(input("Enter minutes of timestamp 2: "))
s2 = int(input("Enter seconds of timestamp 2: "))

min_to_sec = m1 * 60 
x = s1 + min_to_sec
min_to_sec02 = m2 * 60
y = s2 + min_to_sec02
diff = y - x
if diff>0:
 print(f"The difference between two timestamps in seconds is: {diff} ")
else:
 print("Input the higher timetstamp second")


if m1>60 or m2>60:
  print("Minutes should be less than 60")
elif s1>60 or s2>60:
 print("Seconds should be less than 60")
else:
 print("Correct Timestamps")
