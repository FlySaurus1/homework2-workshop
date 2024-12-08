file = open("C:/Users/FlySaurus/Documents/new-BMSTU/2024-2025/practice/homework2/worklogs.txt", "a")

file2 = open("C:/Users/FlySaurus/Documents/new-BMSTU/2024-2025/practice/homework2/worklogs.txt", "r")
filelen = len(file2.readlines())

num = 0
list = []

k = int(input("Введите число, равное количеству будущим введенным символам: "))
for i in range(k):
    num = int(input("Введите число: "))
    list.append(num)

print(f'Максимальное число: {min(list)}')
stroka = ("Min number #" + str(filelen+1) + " - " + str(min(list)) + '\n')
file.writelines(stroka)
