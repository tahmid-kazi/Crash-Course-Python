# Exercise 3-6

guest_list = ["Leonardo da Vinci", "Barack Obama", "Trevor Noah"]
print(guest_list)

flaker = guest_list.pop(0)
message4 = flaker.title() + " can't make it"
print(message4)
new_guy  = "Ed Catmull"
guest_list.insert(0, new_guy)
message5 = "New guest is: " + new_guy.title()
print(message5)

print("Found a bigger table!")

guest_list.insert(0, "Ian Goodfellow")
guest_list.insert(2, "Steve Wozniak")
guest_list.append("Avi Tevanian")

for i in guest_list:
    print("Formally asking " + i.title()+" to dinner")
