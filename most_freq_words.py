seq = str(input("Input sequence: "))
k = int(input("Input lenght of pattern: "))


def pattern_count(seq, pattern):
    count = 0
    for i in range(0, (len(seq) - len(pattern) + 1)):
        if seq[i:i + len(pattern)] == pattern:
            count += 1
    return count


def frequent_words(seq, k):
    max_count = 0
    pattern_length = int(k)
    max_pattern = []
    for i in range(0, (len(seq) - k + 1)):
        if pattern_count(seq, seq[i:i + pattern_length]) > max_count:
            max_count = pattern_count(seq, seq[i:i + pattern_length])
            max_pattern.append(seq[i:i + pattern_length])
        elif pattern_count(seq, seq[i:i + pattern_length]) == max_count and seq[i:i + pattern_length] not in max_pattern:
            max_pattern.append(seq[i:i + pattern_length])
    print(max_count)
    return max_pattern


print(frequent_words(seq, k))
