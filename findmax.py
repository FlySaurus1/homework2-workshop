file = open("C:/Users/FlySaurus/Documents/new-BMSTU/2024-2025/practice/homework2/numbers.txt", "a")

file2 = open("C:/Users/FlySaurus/Documents/new-BMSTU/2024-2025/practice/homework2/numbers.txt", "r")
filelen = len(file2.readlines())

num = 0
list = []
print("Если введёте пробел, программа остановится и выведет максимальное число.")
while num != "":
    try:
        num = int(input("Введите число: "))
        list.append(num)
    except ValueError:
        print(f'Максимальное число: {max(list)}')
        stroka = ("Max number #" + str(filelen+1) + " - " + str(max(list)) + '\n')
        file.writelines(stroka)
        break
