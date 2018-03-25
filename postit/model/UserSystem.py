
class UserSystem:
    def __init__(self):
        self._users = []

    
    @property
    def users(self):
        return self._users

    def add_users(self, user):
        self._users.append(user)

    def get_user(self, name):
        for user in self._users:
            if user.name == name:
                return user