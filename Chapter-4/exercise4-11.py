# Exercise 4-11

pizzas = ["barbeque", "cheese", "hawaiian"]
friend_pizza = pizzas[:]
pizzas.append("Mayo")
friend_pizza.append("turkey")

print("My pizzas")
for i in pizzas:
    print(i)

print("\ndummy's pizza")
for j in friend_pizza:
    print(j)
