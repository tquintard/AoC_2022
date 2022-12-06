import string
def common_letter_value(groups):
    common_letter = set(string.ascii_letters)
    for group in groups:
        common_letter = common_letter & {c for c in group}
    return string.ascii_letters.index(list(common_letter)[0]) + 1 

with open('Day3.txt', "r") as f:
    rucksacks = f.read().splitlines()
    rucksacks_compartimented = [[rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]] for rucksack in rucksacks]
    print(sum([common_letter_value(group) for group in rucksacks_compartimented])) #Part 1
    group_of_rucksacks= [rucksacks[i*3:(i+1)*3] for i in range(len(rucksacks)//3)]
    print(sum([common_letter_value(group) for group in group_of_rucksacks])) #Part 2
