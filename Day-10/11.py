username = "DefaultUser"
def update_username():
    global username
    username = input("Enter new username: ")

update_username()
print("Updated username:", username)