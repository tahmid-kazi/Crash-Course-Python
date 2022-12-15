# Exercise 5-10

current_users = ["asp","aes","rope","bit","weeds"]
new_users = ["asp","seo","rope","lights","sharpie"]

for i in new_users:
    if (i.lower() in current_users):
        print ("\n")
    else:
        print(i + " is available")
