class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def displayinfo(self):
        print(f"My name is {self.name}, a {self.gender} and I am {self.age} years old!")
        
person_attributes = person("Victor", 24, "Male")
    
person_attributes.displayinfo()
    
        