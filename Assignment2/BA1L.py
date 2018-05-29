# Implement Pattern to Number (Rosalind BA1L)

dna_seq = str(input("Input sequence: "))
dna_seq = str.upper(dna_seq)


sym_to_num = {"A": 0, "C": 1, "G": 2, "T": 3}


def pattern_to_number(pattern):

    if not pattern:
        return 0

    return 4 * pattern_to_number(pattern[:-1]) + sym_to_num[pattern[-1]]


if __name__ == "__main__":
    print(pattern_to_number(dna_seq))
