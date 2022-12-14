# Exercise 3-5

guest_list = ["Leonardo da Vinci", "Barack Obama", "Trevor Noah"]
print(guest_list)
# if message1 is defined here, ed catmull never gets printed (10:54am) (5/22/22)
flaker = guest_list.pop(0)

message4 = flaker.title() + " can't make it"
print(message4)
new_guy  = "Ed Catmull"
guest_list.insert(0, new_guy)
message5 = "New guest is: " + new_guy.title()
print(message5)

message1 = "Formally asking " + guest_list[0].title()+" to dinner"
message2 = "Formally asking " + guest_list[1].title()+" to dinner"
message3 = "Formally asking " + guest_list[2].title()+" to dinner"

print(message1)
print(message2)
print(message3)
