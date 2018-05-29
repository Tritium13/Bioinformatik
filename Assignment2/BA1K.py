# Generate the Frequency Array of a String (Rosalind BA1K)

import itertools

text = str(input("Input sequence: "))
text = str.upper(text)
k = int(input("Input lenght kmer: "))

sym_to_num = {"A": 0, "C": 1, "G": 2, "T": 3}

nt = "ACGT"
# Use this order of nucleotides (nt) to get correct order without sorting
permutations = itertools.product(nt, repeat=k)

kmers = []
for i, j in enumerate(list(permutations)):
    kmer = ""
    for item in j:
        kmer += str(item)
    kmers.append(kmer)
print(*kmers, sep=" ")
# len(kmers) is count of permutations

index = list(range(0, 4**k))
print(*index, sep=" ")


def pattern_to_number(pattern):

    if not pattern:
        return 0

    return 4 * pattern_to_number(pattern[:-1]) + sym_to_num[pattern[-1]]


#if __name__ == "__main__":
#    print(pattern_to_number(text))


def frequency_array(text, k):
    array = [0] * 4**k
    for i in range(0, len(text) - k + 1):
        num = pattern_to_number(text[i:i+k])
        array[num] += 1
    return array


print(*frequency_array(text, k), sep=" ")
