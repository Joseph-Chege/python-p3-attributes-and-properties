#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None, approved_breeds=None):
        self.approved_breeds = APPROVED_BREEDS or []
        self._name = None
        self._breed = None
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed


    def get_name(self):
        return self._name


    def set_name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value