import csv
from utility import string_operation
import math
import random
from datetime import datetime
import time
import os 
import json

# # age = int(input("Please enter your age: "))
# # can_enter_free = age < 12 or age >= 65
# # if can_enter_free:
# #     print("You can enter for free!")
# # else:
# #     print("You need to pay for entry.")

# # # concatenation example 
# # list1 = ["nathan" , "is" , "a" , "developer"]
# # sentence = ",".join(list1)
# # print(sentence)

# #type conversion
# # prist_list = []
# # original_price = int(input("enter wholesale price: "))
# # profit_margin = 1.5
# # final_price = round(original_price * profit_margin)
# # print(final_price)
# # prist_list.append(final_price)
# # print(prist_list)

# # a list is a collection of mutable data of different types 
# # element_list = [2,3 ,4 , "nathan", "goat"]
# # # use append to add a element at the end 
# # element_list.append("apple")
# # print(element_list)
# # # we use extend to add a list of items
# # element_list.extend([6, 8])
# # print(element_list)
# # # we use insert to add an item at a particular index 
# # element_list.insert(3, "smoke")
# # print(element_list)
# # # we use remove to remove any element in the list 
# # element_list.remove("apple")
# # print(element_list)

# # A tupple is an ordered collection of data, which is not mutabl, it has methods like count which returns the number of times. a vaulue occures in the tuple and index() which searches for a particular value and returns the position where it is found 

# first_tuple = ("nathan", "john", 4, 5, "nathan" )
# second_tuple = (2,3,6,7)
# third_tuple = first_tuple + second_tuple
# print(len(first_tuple))
# (a, b, c, d,e) = first_tuple
# print(a)

# print(first_tuple.count("nathan"))
# print(first_tuple.index("john"))
# print(third_tuple)

# # list is a collection of data which can mutated and can support repeating values
# list_one = [a, b , c, 5, "nathan", "goat", "slice"]
# print(list_one)
# for x in range(len(list_one)):
#     print(list_one[x])
# list_one.append("newItem")
# print(list_one)
# list_one.insert(4, "inserted")
# print(list_one)
# list_one.extend("1399")
# print(list_one)

# # sets are a collection of data that is un ordered and thus do not accept repeated values 

# set1 = { "nathan", "boss", "nelly"}
# set2 = { 1,2,3}
# print(set1.update(set2))


# new_list = [1,2,3,4,5]
# for y in range(len(new_list)):
#     print(new_list[y])
# new_list.append(6)
# print(new_list)
# new_list.pop(2)
# print(new_list)
# new_list.remove(4)
# print(new_list)

# customer_name = input("Please enter your name: ")
# names_customer = ["nathan", "john", "nelly"]
# names_customer.append(customer_name)
# print(names_customer)

# attendance_tracker = {
#   "Nathan": ["2026-02-20", "2026-02-21"],
#   "Lisa": ["2026-02-20"]
# }
# print("-----")
# for key, val in attendance_tracker.items():
#     print(key,val)


# # lamda is an anonymous function that can take any number of arguments but can only have one expression. it is often used for short, simple functions that are not worth defining with a full function definition.
# # the map method allows us to transform each item in a iterabe based on a certain rule 

# class_marks = [34, 45, 25, 67, 89]
# new_marks = map(lambda y: y + 7, class_marks)
# print(list(new_marks))
# print(new_marks)

# list_strings = ["nathan", "john", "nelly"]
# transformed_strings = map(lambda x: x.upper(), list_strings)
# print(list(transformed_strings))

# file handlin in python referst to the operations that can be performed on files.
# file = open("example.txt", "r")
# content = file.read()
# file.close()
# print(content)

# try:
#     file = open("example2.txt", "x")
#     file.write("This is an example of file handling in Python.")
#     file.close()
# except FileExistsError:
#     print("The file already exists.")

# file = open("example2.txt", "a")
# file.write("\nThis line is added to the existing file.")
# file.close()

# file = open("example2.txt", "r")
# content = file.read()
# file.close()
# print(content)

# file = open("example2.txt", "a+")
# file.write("\n My name is nathan and i am a level four hundred student at the university of buea.")
# file.seek(0)
# content = file.read()
# print(content)
# file.close()

# reading and writing to a file using the r+ mode 
# file = open("example.txt", "r+")
# file.seek(0)
# content = file.read()
# print(content)
# file.write(" \nhere is the rewritten file ")
# file.close

#reading a file using the with statement 

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "w") as file:
#     file.write(" this is the content using with statement")
# #writinng to a csv file using the csv module

# data = [
#     ["name", "age", "city"],

#     ["Nathan", 25, "Buea"],
    
#     ["Lisa", 30, "Douala"]
# ]

# with open("new_file.csv", "w") as file:
#     content = csv.writer(file)
#     content.writerows(data)

# making use of module( python files), and packages which are a folder containing modules and the __init__.py

name = "nathan"
upper_name = string_operation.toUppercase(name)
print(upper_name)

print(random.randint(1, 100))

now = datetime.now()
print("Current date and time:", now)

# the time module allows us to wait a period of time before executing the next line of code
print("Waiting for 3 seconds...")
time.sleep(3)
print("Done waiting!")

# the os module provides a way of using operating system dependent functionality like creating directories, listing files in a directory, etc.
current_directory = os.getcwd()
print("Current directory:", current_directory)

# data serialization converst your data into a json format
data = {
    "name": "Nathan",
    "age": 25,
    "city": "Buea"
}

json_data = json.dumps(data)
print(json_data)


    