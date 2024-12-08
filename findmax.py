with open ("C:/Users/FlySaurus/Documents/new-BMSTU/2024-2025/practice/homework2/numbers.txt") as file:
    list = [int (i) for i in file]
print("Максимальное число:", max(list))