class Postit:
    
    def __init__(self):
        self._postitpages = []
        self._current_postitpage = None
        
    def add_postitpage(self, postitpage):
        self._postitpages.append(postitpage)
        if self._current_postitpage == None:
            self._current_postitpage = postitpage

    def get_page(self, name):
        for page in self._postitpages:
            if name == page.name:
                return page

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
