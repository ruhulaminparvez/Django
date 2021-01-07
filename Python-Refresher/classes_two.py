class Dog:
 
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor
    

    def bark(self, str):
        print("BARK! " + str)

mydog = Dog("Fido", 12, "Brown")
print(mydog.name)
mydog.bark("Bow, Bow")