# Exercise 3-7

guest_list = ["Leonardo da Vinci", "Barack Obama", "Trevor Noah"]
print(guest_list)

flaker = guest_list.pop(0)
new_guy  = "Ed Catmull"
guest_list.insert(0, new_guy)
print(guest_list)

print("Found a bigger table!")

guest_list.insert(0, "Ian Goodfellow")
guest_list.insert(2, "Steve Wozniak")
guest_list.append("Avi Tevanian")
print(guest_list)

#for i in guest_list:
#    print("Formally asking " + i.title()+" to dinner")

print("Unfortunately the new table won't arrive in time")

print("Sorry I can't invite you to dinner " + guest_list.pop())
print("Sorry I can't invite you to dinner " + guest_list.pop())
print("Sorry I can't invite you to dinner " + guest_list.pop())
print("Sorry I can't invite you to dinner " + guest_list.pop())
print(guest_list)

print("You are still invited " + guest_list[0])
print("You are still invited " + guest_list[1])
del guest_list[0]
del guest_list[0]
print(guest_list)
