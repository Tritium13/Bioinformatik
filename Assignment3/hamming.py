# Hamming distance between two strings

with open("BA2H.txt") as f:
    input_text = f.read().splitlines()
    pattern = input_text[1:2]
    text = input_text[2:]
    str_one = input_text[2]
    str_two = input_text[3]


    def hamming_distance(str_one, str_two):
        if len(str_one) != len(str_two):
            raise ValueError("Strings have different lengths.")

        mismatches = 0

        for i in range(len(str_one)):
            if str_one[i] != str_two[i]:
                mismatches += 1

        return mismatches


print(hamming_distance(str_one, str_two))
