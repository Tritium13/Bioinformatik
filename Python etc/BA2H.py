#input_data = input("Input data name: ")

with open("BA2H.txt") as f:
    input_text = f.read().splitlines()
    pattern = input_text[1:2]
    text = input_text[2:]


def distance_between_pattern_strings(pattern, text):
    k = len(pattern)
    distance = 0
    for string in text:
        hamming = float("inf")
        for i in range(0, len(string) - k + 1):
            if hamming > hamming_distance(pattern, string[i:i + k]):
                hamming = hamming_distance(pattern, string[i:i + k])
        distance += hamming
    return distance


def hamming_distance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count


print(distance_between_pattern_strings(pattern, text))
#print(pattern)
#print(text)
