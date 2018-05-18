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
# Example of new syntax in if statement:   if "0" in next or "1" in next:
#
# Lists:
#   -- [1,2,3,4]  
#      ['brown', 'blond', 'red']
#   -- range function, range(0,6) -> [0,1,2,3,4,5,6]
#   -- append(<element>), adds element to end of the list
#   -- Example:  animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'playtpus']
#                animals[0] refers to 'bear'
#
#
# For loop:
#   -- for <variable> in <list>:
#          <body>
#
#   -- while <boolean_expression>:
#          <body>
#
#
# 
# Symbols in the language:
# and      -- logical Boolean function
# del      -- remove variable from scope and contents of variable
# from     -- used to indicate which package an import will come from
# not      -- logical Boolean function
# while    -- loop controlled by a Boolean expression
# as       -- can be used as an alias
#             Example:   f = open(file)
#                        f.read()
#                        f.close()
#             Equivalent:    with open(file) as f:
#                                f.read()
#             Example:   import SomeBigModuleName as sbmn
#                        sbmn.method()
# elif      -- confiditional if following after the original if
# global    -- modifier to variable to show that a global variable is being referenced
# or        -- logical Boolean function
# with      -- a way of getting resource, doing something with it, and releasing it in a convenient form (see 'as' keyword)
# assert    -- similar to a assert function in C, can be enabled / disabled for checking debug conditions
# else      -- last leg of if statement
# if        -- has a Boolean expression if evaluate as True will execute the body of statements associated with it
# pass      -- is a NOP that can be used as a code stub.  Effectively does nothing.
# yield     -- used to return a generator (fairly advanced subject which will need examples, but is powerful)
# break     -- just as in C, exits closest enclosing while or foor loop
# except    -- exception handler for specific type of exception in try: except: blocks
# import    -- gets a specific module coupled with from keyword
# print     -- send output as strings to a stream
# class     -- declares a new class from which objects can be made
# exec      -- executes a dynamically created program from a string or code object
# in        -- iterates over a list of elements pointed to by in and returns matching arguments
#              Example:    webframeworks = [['flask','django','pylons','pyramid','brubeck']
#              'flask' in python_webframeworks  # Returns true
# raise     -- causes an exception to occur
# continue  -- just as in C, goes to the next iterator of the closest enclosing while or for loop
# finally   -- code that's guaranteed to run even if an exception occurs
# is        -- sees if one variable is at the same memory address as another (sees if one object is alias of another)
# return    -- used to return values from a function;  multiple values can be returned via a comma separated list
# def       -- use to start the defintion of a function
# for       -- for loops
# lambda    -- shortcut for providing small anonymous functions
# try       -- code to execute that may generate an exception to be handled by a matching exception handler
#  