print("Choose 2 numbers!")
count_numbers1 = int(input('Number one: '))
count_numbers2 = int(input('and number two: '))

count_numbers1 = count_numbers1 + 1
 
while count_numbers1 < count_numbers2:
    print(count_numbers1, end= ", ")
    count_numbers1 = count_numbers1 + 1
print(' All done')