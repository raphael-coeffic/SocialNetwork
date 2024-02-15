from user import User

"""
here we use design pattern Singleton because we don't want to create more than one instance of network 
"""
class SocialNetwork:
    _instance = None
    users = {}
    # init like Singleton
    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls.name = name
            print(f"The social network {name} was created!")
        return cls._instance

    # print the info of all the users
    def __str__(self):
        result_str = f"{self.name} social network:"
        for user in self.users.values():
            result_str += f"\n{user.display()}"
        result_str += "\n"
        return result_str

    def sign_up(self, user_name, password):
        if user_name not in self.users:                        # check that we don't have an user with the same name
            if len(password) >= 4 and len(password) <= 8:      # check that the length of the password is ok
                self.users[user_name] = User(user_name, password)
                return self.users[user_name]
            else: print("the password is too short or too long")
        else: print("User already exists!")

    def log_in(self, user_name, password):
        if self.users[user_name].password == password:         # check the password for log in
            self.users[user_name].connected = True
            print(f"{user_name} connected")

    def log_out(self, user_name):
        self.users[user_name].connected = False
        print(f"{user_name} disconnected")


