# Implement Number To Pattern (Rosalind BA1M)

index = int(input("Input index: "))
k = int(input("Input lenght kmer: "))

num_to_sym = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def num_to_pattern(index, k):
    if k == 1:
        return num_to_sym[index]
    elif k > 1:
        pref_ind = index // 4
        r = index % 4
        pref_pattern = num_to_pattern(pref_ind, k - 1)
        return pref_pattern + num_to_sym[r]


print(num_to_pattern(index, k))
