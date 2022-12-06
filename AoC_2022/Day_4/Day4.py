import time
start = time.perf_counter()
with open('Day4.txt', "r") as f:
    assignements_per_pair = [[{section for section in range(int(elf_assign.split('-')[0]), int(elf_assign.split('-')[-1]) + 1)} for elf_assign in assignement.split(',')] for assignement in f.read().splitlines()]
print(sum([1 for assignement in assignements_per_pair if assignement[0].issubset(assignement[1]) or assignement[0].issuperset(assignement[1])])) # Part 1
print(sum([1 for assignement in assignements_per_pair if len(assignement[0] & assignement[1]) != 0])) # Part 2
print((time.perf_counter() - start)*1000)

start = time.perf_counter()
with open('Day4.txt', "r") as f:
    total_part1 = 0
    total_part2 = 0
    for pair, assignement in enumerate(f.read().splitlines()):
        assignements_per_pair=[]
        for elf_assign in assignement.split(','):
            sections_delimiter = elf_assign.split('-')
            elf_section = set()
            for section in range(int(sections_delimiter[0]), int(sections_delimiter[-1]) + 1):
                elf_section.add(section)
            assignements_per_pair.append(elf_section)
        if assignements_per_pair[0].issubset(assignements_per_pair[1]) or assignements_per_pair[0].issuperset(assignements_per_pair[1]):
            total_part1 += 1
        if len(assignements_per_pair[0] & assignements_per_pair[1]) != 0:
             total_part2 += 1       
print(total_part1, total_part2)
print((time.perf_counter() - start)*1000)
