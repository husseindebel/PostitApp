from flask_login import UserMixin
class User(UserMixin):
    
    def __init__(self, name, password):
        self._name = name 
        self._password = password 
        self._authenticated = False
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name 
    
    @property
    def password(self):
        return self._password 

    @password.setter
    def password(self, password):
        self._password = password

    
    def __str__(self):
        return "Name: " + self._name + " Password: " + self._password

    def __eq__(self, other):
        try:
            return self._name == other._name
        except AttributeError:
            return False    # There is no 'container' attribute, so can't be equal

    def get_id(self):
        return self._name

    @property
    def is_authenticated(self):
        return self._authenticated

    @is_authenticated.setter
    def authenticated(self, value):
        self._authenticated = value