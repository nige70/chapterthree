# odr, chr 




# print(chr(169))
# print(ord('©'))

# print("car"<"cat")

# a = 10
# b = 5

# c = (a + b) < (2 * a) # True

# d = 1 > 5 # False
# print("c", c)
# print("d", d)

# print(c and d) # if c is true and d is true, the entire expression will evaluate to true, else it will evaluate to false
# print(c or d)
# print(c is not d)

# state = "MD"

# result = state in ["MD", "CA", "TX", "NY"]

# print("result", result)





# weather = "Hot"
# humidity = "Warm"

# if not(weather == "Hot") and humidity == "Warm":
#     print("It is hot today!")
# else:
#     print("It is not hot today.")

"""
First take in two numbers from the user
store them in variables
compare the two numbers, find the largest number
print the largest number to the user
"""

"""
begin
number 1 = user input 1
number 2 = user input 2

if number 1 is greater than number 2
    then print out the greater number to the user
if not
    then print the lower of the two numbers

end
"""

# number1 = eval(input("Enter number 1: "))
# number2 = eval(input("Enter number 2: "))

# if number1 > number2:
#     print("Number one is the larger number!")
# else:
#     print("Number two is the larger number!")


"""
First get the gallons from user input and assign it to a variable
check to see if the gallon is between .5 (inclusive) and 1 (inclusive)
if it is true, then print Good It holds about 3/4 of a gallon!
if it is not true, then print No, It holds about 3/4 of a gallon!
"""

"""
begin
gallon = input()
if gallon >= .5 and <=1
then print Good
else print No
end
"""

# gallon = eval(input("How many gallon does a ten gallon hat hold?"))

# if(.5 <= gallon <= 1):
#     print("Good, ", end="")
# else:
#     print("No, ", end="")

# print("It holds about 3/4 of a gallon.")


"""
First take in the three numbers from the user and assign it to variables
Initially set a max variable to first number. Then
check to see if the second number is greater than the max number
If so, set max equal to the second number
if the third number is greater than the third number
then set max to the third number
lastly, print out the max number to the user
"""

"""
num1 = user input
num2 = user input
num3 = user input

max = num1
if num2 is greater than max
    set max to num 2
if num3 is greater than max
    set max to num 3

print max to user
"""

# num1 = eval(input("Enter the first number: "))
# num2 = eval(input("Enter the second number: "))
# num3 = eval(input("Enter the third number: "))
# largest = num1

# if num2 > largest:
#     largest = num2
# if num3 > largest:
#     largest = num3

# print("The largest number is: " + str(largest))

"""
Take in the weather "Steady" or "Flashing" and then take in the color of the sky either "Blue" or "Red"
If the weather is Steady and Blue, then print "Clear view"
If the weather is Flashing and Blue, then print "Clouds due"
If the weather is Steady and Red, then print "Rain ahead"
If the weather is Flashing and Red, then print "Snow instead"
"""

"""
weather = input()
color = input()

if color is Blue
    if weather is Flashing
        Clouds due
    else
        Clear view
else:
    if weather is Flashing
        Snow instead
    else
        Rain ahead

print weather
"""
# mode = input("Enter the mode Steady or Flashing: ")
# color = input("Enter the color Blue or Red: ")
# weather = ""
# if color == "Blue":
#     if mode == "Flashing":
#         weather = "Clouds due"
#     else:
#         weather = "Clear view"
# else:
#     if mode == "Flashing":
#         weather = "Snow instead"
#     else:
#         weather = "Rain ahead"

# print("The weather for today is: " + weather)

"""
Get the cost and revenue from the user and set them in variables
if costs equals revenue then print "Breakeven"
Else if the cost is less than revenue (there is a profit), calculate the profit and display to the user
Subtract cost from revenue to get breakeven
If cost is not less than revenue (there is a loss), calculate the loss and display to the user
"""

"""
cost = input()
revenue = input()

if cost is equal revenue
  print "breakeven"
else
  if cost is less than revenue
    profit = revenue - cost
    print out the profit
  else
  loss = cost - revenue
  print loss to the user
"""

# cost = eval(input("Enter the cost for the company: "))
# revenue = eval(input("Enter the revenue for the company: "))

# if (cost == revenue):
#   print("Break Even!")
# else:
#     # if cost is less than revenue
#   if cost < revenue:
#     # calculate profit
#     profit = revenue - cost
#     print("The profit for the period is ${0:,.2f}".format(profit))
#   else:
#     # calculate the loss because loss is greater than revenue
#     loss = cost - revenue
#     print("The loss for the period is {0:,.2f}".format(loss, 0.34))

# cond1 = True
# cond2 = False
# cond3 = True

# if cond1 == True:
#   print("cond1 is true") # execute
# elif cond2 == True:
#   print("cond2 is true") # execute
# elif cond3 == True:
#   print("cond3 is true") # execute
# else:
#   print("None is true") # execute

"""
The program finds out which number is larger.
We must obtain from the user two inputs, they are number1 and number2
Once we have two numbers, then we evaluate the inputs
if number1 is greater than number2
print the larger value
if it is not true then see if number2 is larger than number1
print the larger value
if both conditions are false, then that means the numbers are equal
print "Number is equal"
"""

"""
number1 = input()
number2 = input()

if number1 > number2
  print number1 is greater
else if number2 > number1
  print number2 is greater
else
  print they are equal
"""

# number1 = eval(input("Enter the first number: "))
# number2 = eval(input("Enter the second number: "))

# if number1 > number2:
#   print("number1 is greater!")
# elif number2 > number1:
#   print("number2 is greater!")
# else:
#   (print("number1 and number2 are equal"))

"""
The program calculates the FICA tax for a single employee. The program first captures the user's input
for the ytd_earnings and the current_earnings. Once we have the two inputs, we calculate the total earnings
by adding them up. We then initially set ssi_benefit_tax = 0 and then based on the total _earnings
if the total_earnings is <= 117,000, ssi_benefit_tax will equal to .062 * current_earnings
otherwise ytd_earnings is <= 117,000, ssi_benefit_tax will equal to .062 * (117,000 - ytd_earnings)

We then calculate the medicare_tax equal to .0145 * current_earnings

if ytd_earnings is >= to 200,000, then we add .009 * current_earnings to medicare
otherwise if total_earnings > 200,000, then we add .009 * (total_earnings - 200,000) to medicare_tax

Once we have all the data, we calculate the FICA. To calculate the FICA, we add ssi_benefit_tax + medicare_tax)
Print out the FICA information to the user
"""

"""
ytd_earnings = input()
current_earnings = input()
total_earnings = ytd_earnings + current_earnings

#calculate ssi benefit tax
ssi_benefit_tax = 0
if the total_earnings is <= 117,000
  ssi_benefit_tax = .062 * current_earnings
elif
  ytd_earnings is < 117,000
    ssi_benefit_tax = .062 * (117,000 - ytd_earnings)

# calculate medicare tax
medicare_tax = .0145 + current_earnings
if ytd_earnings is >= to 200,000
  medicare_tax += .009 * (total_earnings - 200,000) to medicare_tax

# calculate FICA
fica = ssi_benefit_tax + medicare_tax

print result to user
"""

# ytd_earnings = eval(input("Enter YTD earnings for employee: "))
# current_earnings = eval(input("Enter Current Earnings for employee: "))
# total_earnings = ytd_earnings + current_earnings

# #calculate ssi benefit tax
# ssi_benefit_tax = 0
# if total_earnings <= 117000:
#   ssi_benefit_tax = .062 * current_earnings
# elif ytd_earnings < 117000:
#     ssi_benefit_tax = .062 * (117000 - ytd_earnings)

# # calculate medicare tax
# medicare_tax = .0145 * current_earnings
# if ytd_earnings >= 200000:
#   medicare_tax += .009 * current_earnings
# elif total_earnings > 200000:
#   medicare_tax += .009 * (total_earnings - 200000)

# # calculate FICA
# fica = ssi_benefit_tax + medicare_tax

# print("FICA Tax for employee is {0:,.2f}".format(fica))

"""
The program is determining if graduates earned academic honor status based on gpa.
It first needs to capture user input of gpa.
If gpa is >= 3.9, honors = " Magna Cum Laude "
If gpa is >= 3.6, honors = " Summa Cum Laude "
If gpa is >= 3.3, honors = " Cum Laude "
Otherwise, honors = "."
Results will print out ("You graduated" + honors) to user.
"""

"""
gpa = input()

If the gpa is >= 3.9
  honors = " Magna Cum Laude "
elif
  gpa is >= 3.6
    honors = " Summa Cum Laude "
elif
  gpa is >= 3.3
    honors = " Cum Laude "
else
  honors = "."

print ("You graduated" + honors)
"""

# # Bestow graduation honors
# # Request grade point average
# gpa = eval(input("Enter your gpa: "))
# Determine if honors are warranted

# if gpa>= 3.9:
#   honors = " Magna Cum Laude "
# elif gpa >= 3.6:
#   honors = " Summa Cum Laude "
# elif gpa >= 3.3:
#   honors = " Cum Laude "
# else: honors = "."
# # Display conclusion

# print ("You graduated" + honors)

"""
Program uses the method isdigit to guard against improper input.
User input must be captured first. Two numbers need to be entered (num1 and num2) and added up to get the sum.
Sum will be displayed if entries are valid. Otherwise, the user will be informed of the invalid entries.
If both numbers are valid, the program will print "The sum is" , (num1 +  num2 + ".")
If neither are valid, the program will print "Neither entry was a proper number."If the first entry is invalid,
the program will print "The first entry was not a proper number." If the second
entry is invalid, the program will print "The second entry was not a proper number.
End results will print out.
"""

"""
num1 = input()
num2 = input()

if num1.1sdigit and num2.1sdigit:
  print "The sum is" str(eval(num1) + eval(num2)) + ".")
elif not num1.1sdigit:
  if not num2.1sdigit:
    print "Neither was a proper number"
  else:
    print "The first entry was not a proper number."
else:
  print "The second entry was not a proper number."
"""

# # # Request two numbers and find their sum. Validate the input.
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number ")
# # Display sum if entries are valid. Otherwise, inform
# # the user where invalid entries were made.
# if num1.isdigit() and num2.isdigit():
#   print("The sum is" , str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#   if not num2.isdigit():
#     print("Neither was a proper number. ")
#   else:
#     print("The first entry was not a proper number. ")
# else:
#   print("The second entry was not a proper number. ") 

"""
The program illustrates truth values of objects by evaluating numbers and lists as true or false.
No user input needs to be captured.
If 7, it will be evaluated as "A non zero number is true. " Otherwise, the program will print "The number zero is false. "
If [], the program will print "A nonempty list is true. " Otherwise, the program prints "An empty list is false. "
If ["spam"], the program prints "A nonempty list is true. " Otherwise, the program prints "The empty list is false. "
"""

"""
If 7:
  A non zero number is true.
Else:
  The number zero is false.
If []:
  A nonempty list is true.
Else:
  An empty list is false.
If ["spam"]:
  A nonempty list is true.
Else:
  The empty list is false.
"""

# Illustrate Boolean values
# if 7:
#   print("A non zero number is true. ")
# else:
#   print("The number zero is false. ")
# if []:
#   print("A nonempty list is true. ")
# else:
#   print("An empty list is false. ")
# if ["spam"]:
#   print("A nonempty list is true. ")
# else:
#   print("The empty list is false. ")

"""
The program is trying to calculate the number of eyars to reach a million
dollars based on a 4% annual increase.
First initially set numbers_of_years to 0. Then we capture user input to represent
the current_balance. While the current_balance is less than 1 million, we
increment the numbers_of_years by 1.
display the results to the user.
"""

"""
numbers_of_years = 0
current_balance = input ()
while the current_balance is less than 1000000
  current_balance += current_balance + ().04 * current_balance)
  increment numbers of years by 1
"""
# ## Calculate the number of years to become a millionaire.
# numbers_of_years = 0
# current_balance = eval(input("Enter the initial balance: "))
# # enter the loop
# while current_balance < 1000000:
#   current_balance += .04 * current_balance
#   print("numbers_of_years is : ", numbers_of_years)
#   print("current_balance is: ", current_balance)
#   numbers_of_years += 1
# print("In " + str(numbers_of_years) + " years, you will be rich!")

# list1 = []

# while True:
#   # infinite loop
#   num = eval(input("Enter a non negative number: "))
#   if num == -1:
#     break
#   if num == 11:
#     continue
#   list1.append(num)

# print("List 1 contains: ", list1)

"""
The program will search for a list of values and find the first occurence of a number that is divisible
by 11. If it is found, then print the number to the user.
if it is not found, then print "not found"
"""

"""
list1 = ["one", 23, 17.5, "two", 33, 22.1, 242, "three"]
i = 0
foundFlag = False
while i is < len(list1):
  x = list1(1)
  i +=1
  if not isinstance (x, int):
    continue  # Skip to next item in list.
  if x % 11 == 0:
    foundFlag = True
    print(x, "is the first int that is divisible by 11. ")
    break
  if not foundFlag:
    print("There is no int in the list that is divisible by 11. ")
"""

# # Find integers divisible by 11.
# list1 = ["one", 23, 17.5, "two", 33, 22.1, 242, "three"]
# i = 0
# foundFlag = False
# while i < len(list1):
#   x = list1[i]
#   i += 1
#   if not isinstance (x, int):
#     continue  # Skip to next item in list.
#   if x % 11 == 0:
#     foundFlag = True
#     print(x, "is the first int that is divisible by 11. ")
#     break
#   if not foundFlag:
#     print("There is no int in the list that is divisible by 11. ")

"""
The program is trying to obtain facts about the United States.
It will print 4 statements on the screen relating to the United States.
One of the options for the user will be to quit if 
he or she decides to exit the program. 
"""

"""
print("Enter a number from the menu to obtain a fact")
print("about the United States or to exit the program. \n")
print("1. Capital")
print("2. National Bird")
print("3. National Flower")
print("4. Quit\n")
while True:
  num = input ("Make a selection from the menu: "))
  if num == 1:
    print("Washington, DC is the capital of the United States.")
"""
# # Display facts about the United States.
# print("Enter a number from the menu to obtain a fact")
# print("about the United States or to exit the program. \n")
# print("1. Capital")
# print("2. National Bird")
# print("3. National Flower")
# print("4. Quit\n")
# while True:
#   num = int(input("Make a selection from the menu: "))
#   if num == 1:
#     print("Washington, DC is the capital of the United States.")
#   elif num == 2:
#     print("The American Bald Eagle is the national bird.")
#   elif num == 3:
#     print("The Rose is the national flower.")
#   elif num == 4:
#     break
"""
# for var in range(0, 5): # 0, 1, 2, 3, 4
  # print("var is: ", var, "var * var: ", var * var)
"""

# word = input("Enter a word: ")

# reverse_word = ""

# for ch in word:
#   print("ch", ch)
#   print("reverse_word", reverse_word)
#   reverse_word = ch + reverse_word

# print("The reverse word is: ", reverse_word)

# months = ["January", "February", "March"]
# abbr = []
# for month in range(3):
#   char = months[1] [0:3]
#   print('char', char)
#   abbr.append(char)

# print("abbr", abbr)

# def doSomething(a, b): # parameters
#   print("Doing something")
#   print("a is: ", a)
#   print("b is: ", b)

# doSomething("x", "Y") # arguments

# calculate_interest(.5, 10000000, "2001") # arguments


# def firstName(first_name):
#   # print("The first name is: ", first)
#   first_name = "Mike"

# first = input("Enter a first name: ") # John
# firstName(first)

# print("First after changed: ", first)









