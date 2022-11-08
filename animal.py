class Animal():

    def __init__(self, type):
        self.type = type
        self.size = ""
        self.age = 0
        self.name = ""
        if type == "cat" :
            self.name = "Seymour"
        else :
            self.name = "Spot"
        

    def speak(self):
        if self.type == "cat" :
            if self.size == "small" :
                return "meow"
            else :
                return "MEOW!"   
        else :
            if self.size == "small" :
                return "bow wow"
            if self.size == "medium" :
                return "Ruff ruff"
            else :
                return "arf arf"
            

    def describe(self):
        if self.age >= 10 :
            return self.name + " is old"
        else :
            return self.name + " is young"

