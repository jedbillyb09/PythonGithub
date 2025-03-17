# 1
# dog_types = ["pug", "terrier", "alsatian"]
# print(dog_types)
# print(dog_types[0])
# print(f"Why is it I got {(dog_types[0])}, when i expected terrier??")



#2

# colour_list = ["green","Blue","Red"]

# print(f"0 = {(colour_list[0])}, 1 = {(colour_list[1])}, 2 = {(colour_list[2])}")

# first_name = input("What is your name? ")
# tree_colour = int(input("What number colour are leaves? "))
# print(f"{first_name} thinks that the coloour of leaves is {colour_list[tree_colour]}")

# 3
# prize_list = ["Free Ice Cream","A New Car","A Peice of Coal","One Lolipop"]
# first_name = input("What is your name? ")
# prize = int(input("Choose a number between 0 and 3! "))
# print(f"Congratulations {first_name} you have won a {prize_list[prize]}!")

# 4
# rainbow_list = []
# rainbow_colour = input("Name a colour of the rainbow: ")
# rainbow_list.append(rainbow_colour)
# print(rainbow_list)
# print(rainbow_list[0])

# rainbow_list = [ ]
# while rainbow_list != "":
#     print(rainbow_list)
#     rainbow_list = input("Name a colour of the rainbow: ")

# rainbow_list = []
# rainbow_list2 = input("Name a colour of the rainbow: ")
# rainbow_list.append(rainbow_list2)
# print(rainbow_list)
# print(rainbow_list[0])

rainbow_list = []
rainbow_colour = "    "
while rainbow_colour != "":
    rainbow_colour = input("Name a colour of the rainbow ")
    if rainbow_colour == "": break
    rainbow_list.append(rainbow_colour)
    print(f"You choose {rainbow_colour}")
    print(f"The list of the colours in the rainbow now contains: {rainbow_list}")
print("Thank you very much")