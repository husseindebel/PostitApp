class Post:

    def __init__(self, user, title):
        print("anotherthing", title)
        self._user = user
        self._title = title
        self._comments = []
    
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
    
    def add_comments(self, comment):
        self._comments.append(comment)
    
    @property
    def comments(self):
        return self._comments