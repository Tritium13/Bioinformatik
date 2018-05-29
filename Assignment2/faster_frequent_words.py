# finding a most frequent pattern in DNA sequence faster than frequent words

text = str(input("Input sequence: "))
k = int(input("Input lenght of pattern: "))


def faster_most_frequent_words(text, k, frequency=-1):
    frequency_array = dict()
    frequent_patterns = []
    for i in range(0, len(text) - k):
        try:
            frequency_array[text[i:i+k]] += 1
        except KeyError as a:
            frequency_array[text[i:i+k]] = 1

    frequency = max(frequency_array.values()) if frequency < 0 else frequency

    for key in frequency_array.keys():
        if frequency_array[key] >= frequency:
            frequent_patterns.append(key)
    print(frequency)
    return frequent_patterns


print(*faster_most_frequent_words(text, k), sep=" ")
