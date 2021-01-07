class Dog:

    doginfo = "Hey, dogs are cool"

    def bark(self, str):
        print("BARK! " + str)

mydog = Dog()
mydog.bark("Bow, Bow")

mydog.name = "FIDO"
mydog.age = 12

print(mydog.name)
print(mydog.age)

print(Dog.doginfo)

