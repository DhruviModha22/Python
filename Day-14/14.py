class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username, privileges):
        super().__init__(username)
        self.privileges = privileges

admin = Admin("admin_user", ["add", "delete", "modify"])
print(admin.username, admin.privileges)
