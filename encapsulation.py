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

comp1 = Company("apple", "20000000000", 5)
comp1.set_origin("Indonesia")
print(comp1.get_data())
comp1.__origin = "Pakistan"
print(comp1.get_data())