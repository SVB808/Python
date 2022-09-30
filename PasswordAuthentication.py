import getpass as gp
db = { "svb": "234567", "svb808": "987654"}
username = input("Enter your Username: ")
password = gp.getpass("Enter your password: ")
for i in db.keys():
  if username == i:
    while password != db.get(i):
      password = gp.getpass("Enter your password again: ")
    break
print("Password Verified!")
