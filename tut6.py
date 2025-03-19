# # Exercise 1
# list = ['rose','tulip','daisy']
# print(list)
# print(f"")




# exercise 3
# filling_list = []
# loop_count = int(1)
# print("You can have 3 fillings in your toasted sandwich")

# while loop_count < 4:
#     filling_name = input(f"What is filling {loop_count} for you toasty? ")
#     filling_list.append(filling_name)
#     loop_count = loop_count + 1

# print(f"The order is {filling_list[0]}, {filling_list[1]}, {filling_list[2]}")



# # Exercise 4
# rainbow_colours = "  "
# rainbow_list = []
# loop_count = 0

# while rainbow_colours != "":
#     rainbow_colours = input("Name a colour of the rainbow: ")
#     if rainbow_colours == "":
#         break
#     rainbow_list.append(rainbow_colours)

# print("Thank you for your input")

# # while loop_count < len(rainbow_list):
# #     print(rainbow_list[loop_count])
# #     loop_count += 1


# print("Colours entered:", end=" ")
# for colour in rainbow_list:
#     print(colour, end=" ")


# Exercise 6
topping_list = ['bread', 'butter', 'cheese', 'onions', 'tomato sauce']
print(topping_list)

remove_item = input("What do you want to get rid of? ")
topping_list.remove(remove_item)

list_count = 0
while list_count < len(topping_list):
    print(list_count + 1, topping_list[list_count])
    list_count += 1

remove_item = int(input("What NUMBER item do you want to get rid of? "))
topping_list.pop(remove_item - 1)

print(topping_list)
