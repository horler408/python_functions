#Control Flow
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

#The Big If
# Complete the if and elif statements!
def grade_converter(grade):
    if (grade >= 90):
        return "A"
    elif (grade >= 80 and grade < 90):
        return "B"
    elif (grade >= 70 and grade < 80):
        return "C"
    elif (grade >= 65 and grade < 70):
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)

#Input
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word: ")
if(len(original) > 0):
  print original
else:
  print "empty"

#PIG LATIN
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
#THe second parameter is optional below
  new_word = new_word[1:len(new_word)]
  print new_word
  
else:
  print 'empty'

#Tip Calculator
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print "With tax: %f" % bill
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print "With tip: %f" % bill
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#Function
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared

def cube(number):
  return number * number * number

def by_three(number):
  if(number % 3 == 0):
    return cube(number)
  else:
    return False

#Imports
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

#Review
def distance_from_zero(c):
  if(type(c) == int or type(c) == float):
    return abs(c)
  else:
    return "Nope"
  
print distance_from_zero(-2)

#Function Exercise
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if(city == "Charlotte"):
    return 183
  elif(city == "Tampa"):
    return 220
  elif(city == "Pittsburgh"):
    return 222
  else:
    return 475
  
def rental_car_cost(days):
  cost = days * 40
  if(days >= 7):
    cost -= 50
  elif(days >= 3):
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + (plane_ride_cost(city)) + spending_money

print trip_cost("Los Angeles", 5, 600)

#List
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')
print backpack

#For Loop
for variable in list_name:
  # Do stuff!
#More For Loop
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()

print square_list

#DICTIONARY
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Atlantic Ocean'

print zoo_animals

#List and Dictionary Review
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['backpack'].sort()
# Your code here
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print inventory

#LOOP and KEY
# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
  print d[key]  # prints "bar" 

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for value in webster:
  print webster[value]

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for value in a:
  if(value % 2 == 0):
    print value

def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print small

def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

print fizz_count(['fizz', 'fox', 'cat', 'fizz', 'rabbit', 'fizz'])

#String Looping
for letter in "Codecademy":
  print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter

#Special Code
>>> text1 = {
'1' : ['The banana is','The tomatoes are','Too much'],
'2' : ['a','b','c']
}
>>> text2 = {
'a' : ["Yellow","Red","Rice"],
'b' : [1,2,3]
}
>>> paired_values = list(zip(text1['1'], text2['a']))
>>> for x in paired_values:
    print ("{object} {adjective}".format(object = x[0], adjective = x[1]))

  
The banana is Yellow
The tomatoes are Red
Too much Rice
>>> 

#Dictionary Project
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  print
  
total = 0
for value in prices:
  product = prices[value] * stock[value]
  print product
  total += product
  
print total

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

#Project
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total) / len(numbers)
  return total

def get_average(student):
  homework = student['homework']
  quizzes = student['quizzes']
  tests = student['tests']
  return 0.1 * average(homework) + 0.3 * average(quizzes) + 0.6 * average(tests)
  
def get_letter_grade(score):
  if(score >= 90):
    return 'A'
  elif(score >= 80):
    return 'B'
  elif(score >= 70):
    return 'C'
  elif(score >= 60):
    return 'D'
  else:
    return 'F'
print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
  results = []
  for student in class_list:
    get_average(student)
    results.append(get_average(student))
  return average(results)


students = [alice, lloyd, tyler]
print get_class_average(students)

print get_letter_grade(get_class_average(students))

#REVIEW
#To Modify Element of a list in a function
def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)

#Printing a list item by item in a function
n = [3, 5, 7]

def print_list(x):
  for i in range(0, len(x)):
    print x[i]
    
print_list(n)

#Modifying each element of a list in a function
n = [3, 5, 7]

for i in range(0, len(n)):
  n[i] = n[i] * 2
# Don't forget to return your new list!
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
  
print double_list(n)

#Passing a range into a function
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print my_function([0, 1, 2, 3, 4,5]) # Add your range between the parentheses!

#Iterating over a list in function
n = [3, 5, 7]

def total(numbers):
  result = 0
  for item in numbers:
    result += item
  return result
        #OR
def totals(numbers):
  result = 0
  for i in range(len(numbers)):
    print i
    result += numbers[i]
  return result

#Using String in List in Function
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for item in words:
    result += item
  return result
      # OR
def join_strings(words):
  result = ""
  for i in range(len(words)):
    result += words[i]
  return result

#Concatenating a List in a function
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
  return x + y

print join_lists(m, n)

#Using a List of Lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for lst in numbers:
      results.append(lst)
  return results

#BATTLESHIP GAME
board = []
for i in range(5):
  board.append(['O'] * 5)
  
def print_board(board_in):
  for row in board:
    print " ".join(row)
print_board(board)

#BATTLESHIP GAME
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"  
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)


#While LOOP
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False

choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

count = 0

while count < 10: # Add a colon
  print count
  # Increment count
  count += 1

count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

#Guessing Game
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print random_number
guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input('Your guess: '))
  print guess
  if guess == random_number:
    print 'You Win!'
    break
  guesses_left -= 1
else:
    print 'You Lose.'


hobbies = []

# Add your code below!
for i in range(3):
  hobby = raw_input('Enter your hobby: ')
  hobbies.append(hobby)
print hobbies

thing = "spam!"

for c in thing:
  print c

word = "eggs!"

# Your code here!
for g in word:
  print g


phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == 'A' or char == 'a':
    print 'X',
  else:
    print char,

print

#Count as you go
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item
  #Print 1 pizza 2 pasta 3 salad 4 nachos

#Multiple List
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  print max(a, b)

#For/Else
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'

#CHALLENGE EXERCISE
def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)

def digit_sum(n):
  n = str(n)
  total = 0
  for num in n:
    total += int(num)
  return total

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print factorial(4)

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print scrabble_score("pizza")

def purify(lst):
  even = []
  for i in lst:
    if i % 2 == 0:
      even.append(i)
  return even

print purify([1,2,3,4,5,6,7,8,9]) #It removes odd numbers and only print out even numbers

def product(multiple):
  total = 1
  for num in multiple:
    total *= num
  return total

print product([2,5,3,4,8]) #It multiplies the numbers in the list and output total product

def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
  
print remove_duplicates([1, 1, 2, 2])

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])
        

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print censor("this hack is wack hack", "hack")

def counter(sequence, item):
  count = 0
  for char in sequence:
    if char == item:
      count += 1
  return count

print counter([2,3,1,2,4,2,5], 2) #It print 3 to the screen coz 2 appears 3 times

#STATISTICS
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    diff = (average - score) ** 2
    variance += diff
    result = variance / float(len(scores))
  return result


def grades_std_deviation(variance):
  return variance ** 0.5
variance = grades_variance(grades)


print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)

#ADVANCED TOPICS IN PYTHON
my_dict = {
  'name': 'Expert',
  'age': 30,
  'height': '6ft',
  'weight': '65kg',
  'sex': 'female',
  'coding skill': True
}


print my_dict.keys()
print
print my_dict.values()
print
for item in my_dict:
  print item, my_dict[item]

#List Iteration
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]

print cubes_by_four

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 ==0]

print threes_and_fives
#Anonymous Function
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != 'X', garbled)
print message

#BITWISE OPERATORS
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int('0b11001001', 2)

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

def check_bit4(input):
  mask = 0b1000
  if input & mask:
    return 'on'
  else:
    return 'off'

a = 0b10111011
mask = 0b100
print bin(a | mask)


def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

#INTRODUCTION TO CLASSES
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

#MORE ON __INIT__
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = 'good'
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def description(self):
    print self.name,
    print self.age

sloth = Animal('Lampard', 3)
ocelot = Animal('Ronaldo', 4)
hippo = Animal('Hazard', 5)    
zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

hippo.description()
print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive
print hippo.health
print sloth.health
print ocelot.health

#SHOPPING CART CLASS
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

my_cart = ShoppingCart('Obama')
my_cart.add_item('Spagetti', 50)

#INHERITANCE
class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print "Hello, %s" % other.name

class CEO(Employee):
  def greet(self, other):
    print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00
  
  # A method to Redo override
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)
  
milton = PartTimeEmployee('Milton')
staff_one = Employee('Gabriel')
staff_two = PartTimeEmployee('Abdullah')

print milton.full_time_wage(10)
print staff_one.calculate_wage(5)
print staff_two.calculate_wage(10)

class Triangle(object):
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
  number_of_sides = 3
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3 == 180):
      return True
    else:
      return False

class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle
    
my_new_triangle = Equilateral()

#Class Exercise
class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"
    
class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
    
  def drive_car(self):
    self.condition = 'like new'

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition

#Building Useful Classes
class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    return '(%d, %d, %d)' % (self.x, self.y, self.z)
  
my_point = Point3D(1, 2, 3)
print my_point

my_triangle = Triangle(35, 55, 90)
print my_triangle.check_angles()
print my_triangle.number_of_sides
print my_new_triangle.check_angles()

#FILE INPUT/OUTPUT
my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

#To Write into output.txt file
my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for value in my_list:
  my_file.write(str(value) + "\n")
  
my_file.close()

#To Read from output.txt
my_file = open('output.txt', 'r')

print my_file.read()

my_file.close()

#Reading between Lines
my_file = open('text.txt', 'r')

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

#With and as keyword
with open("text.txt", "w") as textfile:
  textfile.write("Success!")

with open('text.txt', 'w') as my_file:
  my_file.write('You are as good as you are!')

#Case Closed
with open('text.txt', 'w') as my_file:
  my_file.write('You are as good as you are!')
if(my_file.closed == False):
  my_file.close()
print my_file.closed


# Nested Functon
def talf(phrase):
  def say(word):
    print(word)
  words = phrase.split(' ')
  for word in words:
    say(word)

talk("I am going to buy the milk")

def count():
  count = 0
  def increament():
    nonlocal count
    count = count + 1
    print(count)

  increament()

count()

# Lambda Function (Anonymous Function
lambda <arguments> : <expression>

lambda a, b : a * b #Lambda function cannot be called directl;y

multiply = lambda a, b : a * b 
print(multiply(2, 2))

# Loops
items = [1, 2, 3, 4]
for item in items:
  print(item)

for item in range(4):
  print(item)

for index, item in enumerate(items):
  print(index, item)


# Annotation
def increament(n: int) -> int:
  return n+1

# Files and Folder in a dir
import os

dirname = '/users/AB/dev'
dirfiles = os.listdir(dirname)
print(files)

  # To get the full path to a file
temp = map(lambda name:
  os.path.join(dirname, name), dirfiles)

print(list(temp))

  # To list only the files
dirs = []
files = []

for file in temp:
  if os.path.isdir(file):
    dirs.append(file)
  if os.path.isfile(file):
    files.append(file)

print(list(dirs))
print(list(files))

# To chech even or odd
numbers = [1, 2, 3, 4, 5]

even = filter(lambda n: n % 2 == 0, numbers)
odd = filter(lambda n: n % 2 == 1, numbers)

print(list(even))
print(list(odd))


# To get the details of a file
# os.path.getsize, os.path.getmtime, os.path.getctime
import os

filename = '/users/AB/test.txt'

print(os.path.getsize(filename))
print(os.path.getmtime(filename)) #last modified
print(os.path.getctime(filename)) #created time
print(os.stat(filename)) #full details of file

stats = os.stat(filename)
print(stats.st_size)
print(stats.sy_mtime)

#To chech if a file of dir exists
exits = os.path.exists(filename)
print(exists)





