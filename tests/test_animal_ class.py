import unittest
import animal

class test_animal_class(unittest.TestCase):

    def test_animal_cat():
        pass

    def teset_animal_name():

        if animal.type == "cat":
         if animal.name == "":
            animal.name = "Seymour"
        
        if animal.type == "dog":
         if animal.name == "":
            animal.name = "Spot"
        return animal.name

    def test_animal_speak():

        if animal.type == "cat":
           if animal.size == "small":
             return "meow"
           else:
              return "MEOW!"
        
        if animal.type == "dog":
            if animal.size == "small":
                return "bow wow"
            else:
                return "Ruff ruff"

    def test_animal_describe(slf):
        if animal.age < 10:
            return animal.name + " is young"
        else:
            return animal.name + " is old"




        

