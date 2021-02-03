print("Welcome to the Python Demo!")
print("All the text you see generated was created in Python")
print("We are using Python 3 running natively on your machine.")

######################################################################
####################### Part 1 #######################################
######################################################################

print("Part 1: Strings")
my_text = "This is a String named my_text."
print(my_text)
print(f"Format strings let you to put variables _inside_ other strings: {my_text}")
print("Strings can also be concatenated (added): " + my_text)
print("There are many useful functions that work with strings")
my_test_length = len(my_text)
print(f"my_text is {my_test_length} characters long.")

######################################################################
####################### Part 2 #######################################
######################################################################

print("Part 2: Functions")
print("Functions can be defined with the 'def' keyword")

def my_function():
    print("Hello from inside a function!")

my_function()

print("Functions can have arguments passed to them")

def my_custom_function(name):
    print(f"Hello {name}")

my_custom_function("Charles")

print("Lastly functions can return a value")

def my_returning_function():
    return "This is a string I returned!"

print(my_returning_function())

######################################################################
####################### Part 3 #######################################
######################################################################

print("Part 3: Lists")
print("Lists can be used to keep track of multiple things...")
my_list = ["thing 1", "thing 2", "thing 3"]
print(f"This is a list of strings named my_list: {my_list}")
print("You can reference parts of a list by their index:")
print(my_list[0])
print(my_list[1])
print(my_list[2])
print("A great way to go through a list is with a for loop:")
for item in my_list:
    print(item)

######################################################################
####################### Part 4 #######################################
######################################################################

print("Part 4: Loops")
print("As you saw above, for loops are very useful.")
print("Python also supports while loops which does something while a condition is met:")
item_number = 0
while item_number < 3:
    print(my_list[item_number])
    item_number = item_number + 1

######################################################################
####################### Part 5 #######################################
######################################################################

print("Part 5: Dictionaries")
print("Python has a native type for key value stores called a dictionary")
print("You store a value and reference it based on a key:")
dict_example = { "example_key": "example_value",
                 "name": "Ryan",
                 "fav_num": 12 }
print("As you can see dictionary values can have different types")
print("Django uses dictionaries to pass variables to templates")
print("You reference a dictionary by putting using the key as an index")
print(dict_example["example_key"])
print(dict_example["name"])
print(dict_example["fav_num"])
print("It can also be handy to go through all items (key value pairs) in a dictionary")
for key, value in dict_example.items():
    print(f"{key}: {value}")

######################################################################
####################### Exercises ####################################
######################################################################

print("LEVEL 0 Exercise:")
print("Open your text editor an write a Python script that prints your name")
print("Save it as name.py in your home directory")
print("Run your script from the terminal with either the py or python3 command")
print()
print("LEVEL 1 Exercise:")
print("Try writing a Python script that prints out the lyrics to 99 Bottles of Beer on the Wall")
print("You can see my example in beer.py, but try to do it yourself first!")
print()
print("LEVEL 2 Exercise:")
print("Try writing a Python script that prints out the lyrics to the 12 Days of Christmas")
print("You can see my example in 12days.py, but try to do it yourself first!")
print()
print("LEVEL 3 Exercise:")
print("Uses lists and dictionaries to represent the following invoice data:")
print("    Service                              Cost")
print("    -----------------------------------------")
print("    Current site survey               $100.00")
print("    Needs Assessment                  $200.00")
print("    New site development              $300.00")
print("    TOTAL                             $600.00")
print("Calculate the total")
print("Use pprint to print out the dictionary: https://docs.python.org/3/library/pprint.html")
print()
print("SUBMISSION:")
print("Take a screenshot of the output of your exercise and turn that in for your submission")
