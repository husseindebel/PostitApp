class PostitPage:
    
    def __init__(self, name, owner):
        self._name = name
        self._owner = owner
        self._posts = []

    
    def add_posts(self, post):
        self._posts.append(post)

    @property
    def posts(self):
        return self._posts

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self):
        return self._owner
    
    def __str__(self):
        return "Name: " + self.name + " Owner: " + self.owner
