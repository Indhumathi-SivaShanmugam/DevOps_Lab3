# login.py

users = {
    "Indhuthi": "1234",
    "Jonna": "abcd",
    "Harnee": "pass123",
    "Jyo": "bob@123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")