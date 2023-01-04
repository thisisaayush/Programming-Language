class Kettle(object):
    power_source = 'electricity'
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

#kenwood is object here of class Kettle.
kenwood = Kettle('Kenwood',8.99)
print("Model: {}, Price: {}".format(kenwood.make, kenwood.price))
print('Switch 1: ',kenwood.on)
kenwood.switch_on()
print('Switch 2: ',kenwood.on)

#hamilton object
hamilton = Kettle('Hamilton', 9.99)

kenwood.power = 1.5
print(kenwood.power)

print("*" * 10)
print("Kettle Power Source: ",Kettle.power_source)
print("Kenwood Power Source: ",kenwood.power_source)
print("Hamilton Power Source: ",hamilton.power_source)

print("Change the power source of Kettle:")
Kettle.power_source = 'atomic'

print('*' * 10)
print("Kenwood power source: ", kenwood.power_source)
print("But change the power source of Hamilton separately: ")
hamilton.power_source = 'Gas'
print("Hamilton power source: ", hamilton.power_source)