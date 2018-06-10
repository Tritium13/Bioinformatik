# Implement the Distance between a pattern and strings (Rosalind BA2H)

with open("TEST.txt") as f:
    Dna = f.read().split()
    pattern = str(input("Input pattern: "))

    def hamming_dist(str_one, str_two):
        if len(str_one) != len(str_two):
            raise ValueError("Strings have different lengths.")

        mismatches = 0
        for i in range(len(str_one)):
            if str_one[i] != str_two[i]:
                mismatches += 1

        return mismatches


    def min_dist_in_str(dna, pattern):
        d_list = list()
        start = 0
        k = len(pattern)
        while start + k <= len(dna):
            sub_str = dna[start:start + k]
            d_list.append(hamming_dist(sub_str, pattern))
            start += 1

        return min(d_list)


    def dist_in_str_set(Dna, pattern):
        distances = list()
        for dna in Dna:
            distances.append(min_dist_in_str(dna, pattern))

        return sum(distances)


if __name__ == "__main__":
    print(dist_in_str_set(Dna, pattern))
