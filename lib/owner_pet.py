class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        from owner_pet import Pet  # avoid circular import if needed
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        from owner_pet import Pet
        if not isinstance(pet, Pet):
            raise Exception("Must be an instance of Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        from owner_pet import Owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")

        self.name = name
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")

        self.owner = owner
        Pet.all.append(self)
