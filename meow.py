import random
cases = []
test_cases = input('Number of cases?: ')
for i in range(int(test_cases)):
    cases.append(input('Number of distinct cells: '))
king_x = random.randint(1, 8)
king_y = random.randint(1, 8)
king = (king_x, king_y)
print(king)