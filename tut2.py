answer_one = input("would you like a glass of water? ")
answer_one = answer_one.lower()
if answer_one == 'yes' : 
    print("Your water is chilled and includes ice")
elif answer_one == 'no' :
    print("You can ask for water any time")
else: 
    print("The answer needed to be yes or no")