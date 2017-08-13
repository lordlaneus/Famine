class Noun:
    def __init__(self):
        self.aliases = []
    def addAliases(self,alias):
        self.aliases.append(alias)
    def look(self):
        raise NotImplementedError( "Should have implemented this")
    def named(self, name):
       return name in self.aliases
