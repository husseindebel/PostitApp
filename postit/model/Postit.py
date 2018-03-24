from PostitPage import PostitPage
class Postit:
    
    def __init__(self):
        self._postitpages = []
        self._current_postitpage = None
        
    def add_postitpage(self, postitpage):
        self._postitpages.append(postitpage)
        if self._current_postitpage == None:
            self._current_postitpage = postitpage
    
    @property
    def postitpages(self):
        return self._postitpages
    
    @property
    def current_postitpage(self):
        return self._current_postitpage

    @current_postitpage.setter
    def current_postitpage(self, postitpage):
        if postitpage in self._postitpages:
            self._current_postitpage = postitpage


if __name__ == "__main__":
    something = Postit()
    new_postitpage = PostitPage("hussein", "me")
    something.add_postitpage(new_postitpage)
    print(something.current_postitpage)
