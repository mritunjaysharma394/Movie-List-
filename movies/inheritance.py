class Parent():
    def __init__(self,last_name,eye_color):
        print("Parnet Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child():
    
    print("Child constructor called")
    def __init__(self,last_name,eye_color,number_of_toys):
        
        
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

miley_cuyrus = Child("Cuyrus","Blue",5)
print(miley_cuyrus.last_name)
print(miley_cuyrus.number_of_toys)
