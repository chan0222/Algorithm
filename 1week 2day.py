import sys
dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)

for i in range(9):
    for j in range(i+1,9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            result = [dwarfs[k] for k in range(9) if k != i and k !=j]
            result.sort()
            for dwarf in result:
                print(dwarf)
            sys.exit()