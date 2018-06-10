# Generate permutations of kmers

import itertools

k = int(input("Input kmer lenght: "))
nt = "ACGT"
# Use this order of nt to get correct order later without sorting
permutations = itertools.product(nt, repeat=k)

kmers = []
for i, j in enumerate(list(permutations)):
    kmer = ""
    for item in j:
        kmer += str(item)
    kmers.append(kmer)
print(kmers)