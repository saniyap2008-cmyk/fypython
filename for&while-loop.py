print("Countdown")
count = 5
while count > 0:
    print(count)
    count -= 1 
print("Blast off!\n")



print("Sum numbers 1 to 5")
total = 0
for num in range(1, 6):  # range(1, 6) generates numbers 1, 2, 3, 4, 5
    total += num
    print(f"Added {num}, running total: {total}")

print(f"Final sum: {total}")