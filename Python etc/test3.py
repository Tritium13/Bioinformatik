
with open("BA2H.txt") as f:
    input_text = f.read().splitlines()
    pattern = input_text[1:2]
    data = input_text[2:]

def HAMMINGDISTANCE(data1,data2):
    total = abs(len(data1)-len(data2))
    counter = min(len(data1),len(data2))
    for i in range (counter):
        total += (data1[i] != data2[i])
    return total


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    distance = 0
    k = len(Pattern)
    for dna in Dna:
        #global hamming distance
        ghd = float("inf")
        for i in range(len(dna)-k+1):
            #local hamming distance
            lhd = HAMMINGDISTANCE(Pattern, dna[i:i+k])
            if lhd<ghd:
                ghd=lhd
        distance+=ghd
    return distance


print(DistanceBetweenPatternAndStrings(pattern, data))
