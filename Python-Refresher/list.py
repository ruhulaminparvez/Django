# List

dog_names = ["tom", "sean", "sally", "mark"]

print(type(dog_names))
print(dog_names)

# Adding Item On Last Position
dog_names.append("sam")

print(dog_names)

# Adding Item On First Position
dog_names.insert(0, "bruz")

print(dog_names)

# Delete Items 
del(dog_names[0])

print(dog_names)

# Length Of List
print('Length Of List: ',len(dog_names))