# Write a Python program which accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.

# num = input("Enter some numbers: ")
# lst = num.split(",")
# tpl = tuple(lst)
# print("List: ", lst)
# print("Tuple: ", tpl)

# Write a Python program to display the first and last colours from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print("First Color: ", color_list[0])
# print("Last Color: ", color_list[3])


# Write a Python program to print the calendar of a given month and year.(Using calender module)
import calendar

year = int(input("Enter Year: "))
mon = int(input("Enter Month: "))
print(calendar.month(year,mon))
