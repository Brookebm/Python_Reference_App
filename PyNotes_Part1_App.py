# Use the pound sign (#) for notes on single line; 
# These notes are ignored in execution.

# Print Function to output the text in parenthesis:
# Python3 uses () but Python2 doesn't.
print ("Hello World!")

# Single and double quotes are good for one line strings: 
print ('The Interpreter and Compiler are separate processes.')
print ("Python uses an Interpreter.")
print ("Double quotes are best practice.")

# For a string on multiple lines (useful for longer text), use triple quotes:
print ('''The Text Editor(write script), python interpreter (execution), 
and terminal (run script) are all separate distinct entities.''')

# String concatenation -> concatenate (i.e. merge) two strings into one string:
print ("This is a" + " string which is a data type.")
print ("A string can hold text(abc), numbers (123) and symbols (@).")
# Spaces in a string matter:
print ("No" + "Space" + "Added.")
print ("Space" + " Added!")

# A variable can be assigned an value, and that value can be changed, allowing for flexiblity:
my_variable = 5
print (my_variable)

my_variable = 6
print (my_variable)

# In mathematical operations, the order of operations is followed.
print ("Mathematical Operators are  *, /, +, and -.")
order_of_operations = ('''From left to right: Parenthesis (), Exponents **,
 Multication *, Division /, Addition +, and subtraction -.''')
print (order_of_operations)

math1 = (3**2 - 1) * 2 / 2 + 5
print (math1)

# Python3 will print the Float if do 4/3, but python2 will round down the answer to an Integer.
# In Python2, to get float answer, can do: 4./3, 4/3., or 4./3. or float(4)/3
# In variable naming, best practice is first letter lowercase or if start with number put underscore first.
_2math = 4/3
print (_2math)

# Modulo Operator returns the remainder after division is performed.
# This operator is used for odd/even tests
print (4%3)

# Integer, Float and String are data types.
# The print function can use + and * operations, also called String Operators.
# The * will copy the string statement by integer number of times.
# Cannot multiply string statement by string.
print ("text " * 3)
print ("3" * 3)

# Variables are not objects, but a symbolic name that is reference to an object.
# Objects, Variables and Attributes will be explored and explained later.
# The symbol (=) is an assignment operator. 
# Variables are reusable. Print function will print value in variable:
variable_name = "This value is defined. It can be string, integer and float."
print (variable_name)
