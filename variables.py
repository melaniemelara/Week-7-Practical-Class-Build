# This is a comment
# This is a print method.Print will echo out anything inside the 
# () round brackets to the terminal, when we run the file
print("This is my very first python script!!")

# Variables are placeholders, with dynamic values -> things that can change 
# they get stored in memory and referenced later

name = "Melanie"
age = 19
eyecolor = "brown"
haircolor = "brown"

#Arrays are variables on steriods. They let us store many values in one 
# variable. -> To help us grou data.
# This makes our scripting files easier to understand and work it
# car1 = "Volvo"
# car2 = "Toyota"
# car3 = "Fiesta"
cars = ["Volvo", "Toyota", "Fiesta"]

print("My name is" + name) 

# input is another Python "thing" - it waits with a flashing cursor
# until you type something and hit enter
name = input("What is YOUR name?")

print("My name is now " + name)

print("My age is " + str(age))