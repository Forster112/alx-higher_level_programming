class Human:
    
    def __init__(self, name="", age=0, complesion=""):
        self.name = name
        self.age = age
        self.complesion = complesion
        
    @property
    def name(self):
        print("Getting the name")
        
        return self.__name
        
    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            print("name cant be empty or a number")
            
    @property
    def age(self):
        print("Getting the age")
        
        return self.__age

    @age.setter
    def age(self, value):
        if value.isdigit():
            self.__age = value
        else:
            print("age cant be empty or a string")
            
    @property
    def complesion(self):
        print("Getting the complesion")
        
        return self.__complesion

    @complesion.setter
    def complesion(self, value):
        if value:
            self.__complesion = value
        else:
            print("complesion cant be empty or a number")
            
            
    def getTheHuman(self):
        me = print("my name is {}, i am {} years old, and i am {} in complesion".format(self.__name, self.__age, self.__complesion))
        
        return me
    
def main():
    anonymous = Human()
    
    name = input("What is your name: ")
    age = input("What is your age: ")
    complesion = input("What is your complesion: ")
    
    anonymous.name = name
    anonymous.age = age
    anonymous.complesion = complesion
    
    print("Name: ", anonymous.name)
    print("age: ", anonymous.age)
    print("complesion: ", anonymous.complesion)
    
    print(anonymous.getTheHuman())
    
main()