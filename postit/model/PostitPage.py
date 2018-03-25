
class PostitPage:
    
    def __init__(self, name, owner):
        self._name = name
        self._owner = owner
        self._posts = []

    
    def add_posts(self, post):
        print("hussein", post.title)
        self._posts.append(post)

    @property
    def posts(self):
        return self._posts

    @property
    def owner(self):
        return self._owner.name
    
    @owner.setter
    def owner(self, name):
        self._owner.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self):
        return self._name
    
    def __str__(self):
        return "Name: " + self._name + " Owner: " + self._owner.name