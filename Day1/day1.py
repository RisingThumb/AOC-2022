elves = []
with open("input.txt", "r") as f:
    currentElf = []
    for line in f:
        if line == "\n":
            elves.append(currentElf)
            currentElf = []
        else:
            currentElf.append(int(line.strip('\n')))

def sum_calories_for_elf(elf):
    calories = 0
    for calorie in elf:
        calories += calorie
    return calories

elvesSummedCalories = []
for elf in elves:
    elvesSummedCalories.append(sum_calories_for_elf(elf))

summedCaloriesSorted = sorted(elvesSummedCalories)

print("Part 1 ", summedCaloriesSorted[-1])
print("Part 2 ", summedCaloriesSorted[-1] + summedCaloriesSorted[-2] + summedCaloriesSorted[-3])


