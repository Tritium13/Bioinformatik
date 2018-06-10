# finding a most frequent pattern in DNA sequence

text = str(input("Input sequence: "))
k = int(input("Input lenght of pattern: "))


def pattern_count(text, pattern):
    count = 0
    for i in range(0, (len(text) - len(pattern) + 1)):
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count


def frequent_words(text, k):
    frequent_patterns = []
    count = [0] * len(text)
    for i in range(0, (len(text) - k + 1)):
        pattern = text[i: i + k]
        count[i] = pattern_count(text, pattern)
    max_count = max(count)
    for i in range(0, (len(text) - k + 1)):
        if count[i] == max_count:
            if text[i: i + k] not in frequent_patterns:
                    frequent_patterns.append(text[i: i + k])
    print(max_count)
    return frequent_patterns


print(*frequent_words(text, k), sep=" ")
