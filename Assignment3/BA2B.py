# Implement find a median string (Rosalind BA2B)

import itertools

with open("BA2B.txt") as f:
    Dna = f.read().split()
    k = int(input("Input lenght kmer: "))


    def generate_all_substrings(k):
        variants = map(''.join, itertools.product('ACTG', repeat=k))
        answers = dict()
        for item in variants:
            answers[item] = 0

        return sorted(answers)


    def hamming_distance(str_one, str_two):
        if len(str_one) != len(str_two):
            raise ValueError("Strings have different lengths.")

        mismatches = 0
        for i in range(len(str_one)):
            if str_one[i] != str_two[i]:
                mismatches += 1

        return mismatches


    def min_distance_in_string(dna, pattern):
        d_list = list()
        start = 0
        k = len(pattern)
        while start + k <= len(dna):
            sub_str = dna[start:start + k]
            d_list.append(hamming_distance(sub_str, pattern))
            start += 1

        return min(d_list)


    def distance_between_pattern_and_string(Dna, pattern):
        distances = list()
        for dna in Dna:
            distances.append(min_distance_in_string(dna, pattern))

        return sum(distances)


    def find_median_string(Dna, k):
        all_variants = generate_all_substrings(k)
        answers = dict()
        for kmer in all_variants:
            answers[kmer] = distance_between_pattern_and_string(Dna, kmer)

        print(min(answers, key=answers.get))

if __name__ == "__main__":
    print(find_median_string(Dna, k))
