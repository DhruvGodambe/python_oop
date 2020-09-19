 # creating a class with a private variable 'origin'
class Company:
    def __init__(self, name, net_worth, rating):
        self.name = name
        self.net_worth = net_worth
        self.rating = rating
        self.__origin = "India" # adding __ makes it a private variable
        print(" __origin from init function : {}".format(self.__origin))

    def get_data(self):
        return {
            "name": self.name,
            "net_worth": self.net_worth,
            "rating": self.rating,
            "origin": self.__origin
        }

    def set_origin(self, val):
        self.__origin = val

#creating a company object
comp1 = Company("Apple", "20000000000", 5)

# changing origin from the class function
comp1.set_origin("Indonesia")
print(comp1.get_data())

#changing private variable from outside of the class
comp1.__origin = "Pakistan"
print(comp1.get_data())

#changing other variables from outside of the class
comp1.name = "Microsoft"
print(comp1.get_data())