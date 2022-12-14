# Exercise 4-5

mil = []
for i in range(1, 1000000):
    mil.append(i)

print(min(mil))
print(max(mil)) #to verify that you're actually making a list with a million numbers
print(sum(mil)) #to see how quickly python adds up a million
