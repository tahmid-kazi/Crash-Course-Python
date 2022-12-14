# Exercise 4-12

foods = ['pizza','falafel','carrot cake']
friend_food = foods[:] #copies the entire list

foods.append("cannoli")
friend_food.append("ice cream")

print("My favorite foods are:")
for i in foods:
    print(i)

print("\nMy friends favorite foods are:")
for j in friend_food:
    print(j)
