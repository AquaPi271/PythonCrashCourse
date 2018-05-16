# <- This is a comment character.
# print("") is used to output to STDOUT.
#   -- ',' will delimit string inputs:  print("Hello", var1, " Have a ", var2 );
#   -- print(f"{variable}") -- The f indicates a variable will be placed inside the curly braces.  f can be used on standalone string variables.
#   -- .format(variable) will place contents at corresponding {}.  
#        formatter = "{} {}" 
#        print(formatter.format(1,2))
#      # This also works:
#        print("{} {}".format(1,2))
#   -- print has other arguments:  print(string, end=' ') --> indicates to use space rather than newline to terminate output.
#   -- \n is traditional newline
# "" or '' delimits a string.
# """ or ''' delimits a multi-line string.
# Math:  + - * / % < > <= >= += -= *= /= (usual meanings).  Numbers are typed first as int then move to float.  Division creates float.
# True and False are Boolean types
# Typical variable naming conventions.
# The \ operator in strings is the escape character.  
#   -- Examples:  \\, \t, \n, \", \a (bell), \b (backspace), \f (formfeed), \n (linefeed), \N{name} (Unicode), \r (carriage return)
#   --            \t (tab), \uxxxx (character with 16-bit hex value), \Uxxxxxxxx (character with 32-bit hex value), \v (vertical tab),
#   --            \ooo (octal value), \xhh (hex)
# The + operator concatenates strings.
# The * operator replicates strings:  print("." * 10) --> ".........."
# input() takes characters from STDIN until newline is input.  Eg.  age = input()
#   -- Prompt can be added:  y = input("Name? ")
# int() converts string to integer
# Features:
#   -- from <name> import <name>             # way to import features
#   -- from sys import argv                  # gets command line -->  script, first, second, third = argv
#   -- from os.path import exists            # operate on file system and check for existence of file
# File I/O:  
#   -- txt = open(filename)           # opens a file named filename
#   -- txt.read()                     # reads the whole file
#   -- txt.close()                    # closes the file
#   -- txt.readline()                 # read just one line of a file
#   -- txt.truncate()                 # empties the file
#   -- txt.write('stuff')             # writes stuff to the file
#   -- txt.seek(0)                    # moves read/write location to the beginning of a file
# Functions:
#   -- def <function_name>(<arguments>):
#          <next_line>
#          <next_line>
#      <blank>
#
#   Examples:   
#   def print_two(*args):
#      arg1, arg2 = args
#      print(f"arg1: {arg1}, arg2: {arg2}")
#
#   def print_two_again(arg1, arg2):
#      print(f"arg1: {arg1}, arg2: {arg2}")
#
#   -- return <expression>            # returns a value from the function, or several expressions separated by commas
#   --   Example:  return 1, 2, 3
#
# Boolean Logic:
#   -- and, or, not, !=, ==, >=, <=, True, False
#
# If expression:
#   -- if <boolean expression>:
#           <body>
#      elif <boolean expression>:
#           <body>
#      else:
#           <body>
#
# Lists:
#   -- [1,2,3,4]  
#      ['brown', 'blond', 'red']
#   -- range function, range(0,6) -> [0,1,2,3,4,5,6]
#   -- append(<element>), adds element to end of the list
#
#
# For loop:
#   -- for <variable> in <list>:
#          <body>
#
#  