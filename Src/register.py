users = {
    "admin": "1234",
    "john": "abcd",
    "alice": "pass123",
    "bob": "bob@123"
}

username = input("Choose a username: ")

if username in users:
    print("Username already exists!")
else:
    password = input("Choose a password: ")
    users[username] = password
    print("Registration successful!")

print("\nRegistered Users:")
for user in users:
    print(user)