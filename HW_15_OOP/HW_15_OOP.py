class Cat:

    cat_info = 'Always Hungry'
    cat_weight = 12

    def __init__(self, cat_name, cat_status, cat_skills):
         self.cat_name = cat_name
         self.cat_status = cat_status
         self.cat_skills = cat_skills

    def cat_inf(self, cat_skills):
        return f"Your cat's name is {self} and your cat can good {cat_skills}"

    @classmethod
    def Location(cls, location):
        if location == 'At home':
            return f"Your cat at home!"
        else:
            return f"Your cat isn't at home!"


    @staticmethod
    def cat_characteristic(color):
            return f"Your cat is {color}"



print(Cat.Location('At home'))
print(Cat.cat_inf('Rita', 'jumping'))
print(Cat.cat_characteristic('White'))
