class Item:
    'this shit aint poop'
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def getName(self):
        return self.name
    def getDesc(self):
        return self.desc

                
shoe = Item("shoe", "it's a shoe")
print(shoe.getDesc())
