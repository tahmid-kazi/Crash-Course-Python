# Exercise 5-9

users = ["admin", "pewdiepie", "oats", "reston", "Foobar"]
user=[]
if not user: #check if list is empty
    print("List is empty")
else:
    for e in users:
        if (e == "admin"):
            print("Hello " + e + ". Would you like to see a status report.")
        else:
            print("Hello " + e + ". Thank you for logging in.")
