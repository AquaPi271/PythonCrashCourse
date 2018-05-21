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
# and       -- logical Boolean function
# as        -- can be used as an alias
#             Example:   f = open(file)
#                        f.read()
#                        f.close()
#             Equivalent:    with open(file) as f:
#                                f.read()
#             Example:   import SomeBigModuleName as sbmn
#                        sbmn.method()
# assert    -- similar to a assert function in C, can be enabled / disabled for checking debug conditions
# break     -- just as in C, exits closest enclosing while or foor loop
# class     -- declares a new class from which objects can be made
# continue  -- just as in C, goes to the next iterator of the closest enclosing while or for loop
# def       -- use to start the defintion of a function
# del       -- remove variable from scope and contents of a dictionary
# elif      -- conditional if following after the original if
# else      -- last leg of if statement
# except    -- exception handler for specific type of exception in try: except: blocks
# exec      -- executes a dynamically created program from a string or code object
# finally   -- code that's guaranteed to run even if an exception occurs
# for       -- for loops
# from      -- used to indicate which package an import will come from; gets specific part of module
# global    -- modifier to variable to show that a global variable is being referenced
# if        -- has a Boolean expression if evaluate as True will execute the body of statements associated with it
# import    -- gets a specific module coupled with from keyword
# in        -- iterates over a list of elements pointed to by in and returns matching arguments
#              Example:    webframeworks = [['flask','django','pylons','pyramid','brubeck']
#              'flask' in python_webframeworks  # Returns true
# is        -- sees if one variable is at the same memory address as another (sees if one object is alias of another)
# lambda    -- shortcut for providing small anonymous functions
# not       -- logical Boolean function
# or        -- logical Boolean function
# pass      -- is a NOP that can be used as a code stub.  Effectively does nothing.
# print     -- send output as strings to a stream
# raise     -- causes an exception to occur
# return    -- used to return values from a function;  multiple values can be returned via a comma separated list
# try       -- code to execute that may generate an exception to be handled by a matching exception handler
# while     -- loop controlled by a Boolean expression
# with      -- a way of getting resource, doing something with it, and releasing it in a convenient form (see 'as' keyword)
# yield     -- used to return a generator (fairly advanced subject which will need examples, but is powerful)
#  
# Operators:
#
#     +
#     -
#     *
#     **   -- exponentation
#     /
#     //   -- floor division
#     %
#     <
#     >
#     <=
#     >=
#     ==
#     !=
#     ()
#     []
#     {}
#     @
#     ,
#     :
#     .
#     =
#     ;
#     +=
#     -=
#     *=
#     /=
#     //=
#     %=
#     **=
#
# Data types:
#
# True
# False
# None
# bytes   -- x = b"hello"
# strings
# numbers
# floats
# lists
# dicts

# List operations:
#
# len() -- length of list
# split(<string>) -- for string, create a list of elements separated by ' ' (or any character you want)
# append(<item>)  -- add item to end of list
# pop() -- remove last item in list and return it
# <char>.join(<list>) -- creates a string by inserting <char> between elements 
#                     -- alternatively, join('<char>', <list>) does the same thing
#
# Dict operations:
#
# -- is just a hash
# -- stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
#    stuff['name'] => 'Zed'
#    stuff[1] = 3    # will make stuff look like:  {'name': 'Zed', 'age':36, 'height':74, 1:3}
# -- use del to remove a hash element
# -- Example:
# --     states = { 'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI' }
# --     for state, abbrev in states.items():
# --         print "%s is abbreviated %s" % (state, abbrev)
# -- get(<hash_index>,<value_if_not_found>)
#
# Classes examples:
#    class Song(object):
#
#        def __init__(self, lyrics):
#            self.lyrics = lyrics
#
#        def sing_me_a_song(self):
#            for line in self.lyrics:
#                print(line)
#
#   happy_bday = Song(["Happy birthday to you",
#                      "I don't want to get sued",
#                      "So I'll stop right there"])
#
#   bulls_on_parade = Song(["They rally around the family",
#                           "With pockets full of shells"])
#
#   happy_bday.sing_me_a_song()
#
#   bulls_on_parade.sing_me_a_song()
#
#
#   import random
#   from urllib import urlopen
#   import sys
#
#   WORD_URL = "http://learncodethehardway.org/words.txt"
#   WORDS = []
#
#   PHRASES = {
#       "class %%%(%%%):":
#         "Make a class named %%% that is-a %%%.",
#       "class %%%(object):\n\tdef __init__(self, ***)":
#         "class %%% has-a __init__ that takes self and *** parameters.",
#       "class %%%(object):\n\tdef ***(self, @@@)":
#         "class %%% has-a function named *** that takes self and @@@ parameters.",
#       "*** = %%%()":
#         "Set *** to an instance of class %%%.",
#       "***.***(@@@)":
#         "From *** get the *** function, and call it with parameters self, @@@.",
#       "***.*** = '***'":
#         "From *** get the *** attribute and set it to '***'."
#   }
#
#   # do they want to drill phrases first
#   PHRASE_FIRST = False
#   if len(sys.argv) == 2 and sys.argv[1] == "english":
#       PHRASE_FIRST = True
#
#   # load up the words from the website
#   for word in urlopen(WORD_URL).readlines():
#       WORDS.append(word.strip())
#
#
#   def convert(snippet, phrase):
#       class_names = [w.capitalize() for w in
#                      random.sample(WORDS, snippet.count("%%%"))]
#       other_names = random.sample(WORDS, snippet.count("***"))
#       results = []
#       param_names = []
#
#       for i in range(0, snippet.count("@@@")):
#           param_count = random.randint(1,3)
#           param_names.append(', '.join(random.sample(WORDS, param_count)))
#
#       for sentence in snippet, phrase:
#           result = sentence[:]
#
#           # fake class names
#           for word in class_names:
#               result = result.replace("%%%", word, 1)
#
#           # fake other names
#           for word in other_names:
#               result = result.replace("***", word, 1)
#
#           # fake parameter lists
#           for word in param_names:
#               result = result.replace("@@@", word, 1)
#
#           results.append(result)
#
#       return results
#
#
#   # keep going until they hit CTRL-D
#   try:
#       while True:
#           snippets = PHRASES.keys()
#           random.shuffle(snippets)
#
#           for snippet in snippets:
#               phrase = PHRASES[snippet]
#               question, answer = convert(snippet, phrase)
#               if PHRASE_FIRST:
#                   question, answer = answer, question
#
#               print question
#
#               raw_input("> ")
#               print "ANSWER:  %s\n\n" % answer
#   except EOFError:
#       print "\nBye"
#
# Inheritence:
#
# class Parent(object):
#
#     def implicit(self):
#         print("PARENT implicit()")
#
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
## This will print "PARENT implicit()" twice.
#
# 
# class Parent(object):
#
#     def override(self):
#         print("PARENT override()")
#
# class Child(Parent):
#
#     def override(self):
#         print("CHILD override()")
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()
#
## This will print "PARENT override()" followed by "CHILD override()"
#
# How to explicitly call the super class.
#
# class Parent(object):
#
#     def altered(self):
#         print("PARENT altered()")
#
# class Child(Parent):
#
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()
#
## PARENT altered()
## CHILD, BEFORE PARENT altered()
## PARENT altered()
## CHILD, AFTER PARENT altered()