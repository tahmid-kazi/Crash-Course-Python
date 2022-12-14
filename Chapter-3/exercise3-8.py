# Exercise 3-8

world = ["Greece", "Rome", "Japan", "Turkey"]
#print(sorted(world)) #shows temporary sorting 
#print(world)
#print(sorted(world, reverse=True)) #prints in reverse sorted order temporarily

world.reverse() #this is permanent
#print(world)
world.reverse() #back to its original order
#print(world)

world.sort() #permanent alphabetical sorting
print(world)
world.sort(reverse=True)
print(world)
