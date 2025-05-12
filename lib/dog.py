#!/usr/bin/env python3

class Dog:
    def __init__(self, name,breed="Mutt"):
        self.breed = breed
        self.name = name

    # dog.__init__(name, breed = "Mutt")
    #     self.breed = breed
    #     self.name = name

    def bark(self):
        print("Woof!")

fido = Dog("Fido")
fido.name
# Fido

snoopy = Dog("Snoopy")
snoopy.name
# Snoopy



