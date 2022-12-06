with open('Day1.txt', "r") as f:
    all_elves_meals = sorted(map(sum,[map(int,elves_meals.split('\n')) for elves_meals in f.read().split('\n\n')]))

print(all_elves_meals[-1], sum(all_elves_meals[-3:] ))
