file = open("animals.txt", "r")

raw_data = file.readlines()
animals = [element.replace("\n", "") for element in raw_data]
file.close()

new_file = open("animals_new.txt", "w")

new_file.write(" ".join(animals))

new_file.close()
