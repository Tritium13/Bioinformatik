# Implement Randomized Motif Search (Rosalind BA2F)

from random import randint

file_name = str(input("Input file: "))
n = int(input("Anzahl Durchläufe: "))


# Randomized selection of motifs in every DNA-string
def Random_Select_Motifs(Dna, k, t):
    Motifs = []

    for seq in Dna:
        index = randint(0, len(seq) - k)
        Motifs.append(seq[index:index+k])
    return Motifs


# Creation of a profile from random-picked motifs
def Profile(Motifs, k):
    profile = []

    for i in range(k):
        for j in range(len(Motifs)):
            if j == 0:
                profile.append({'A': 1, 'T': 1, 'C': 1, 'G': 1})
            profile[i][Motifs[j][i]] += 1
    return profile


# Determination of the Consensus-motif from motifs in profile
def Motif(profile, Dna):
    Motifs = []

    for Seq in Dna:
        k = len(profile)
        max_probs = -1
        kmer = ''
        for i in range(len(Seq) - k + 1):
            Sum = 1
            for j in range(k):
                Sum *= (profile[j][Seq[i+j]])
                if Sum > max_probs:
                    max_probs = Sum
                    kmer = Seq[i:i+k]
        Motifs.append(kmer)
    return Motifs


# Calculating of the score for motifs in relation to Consensus-sequence
def Score(Motifs, k, t):
    profile = Profile(Motifs, k)
    score = 0

    for a in range(len(profile)):
        score += (4 + t - profile[a][max(profile[a], key=profile[a].get)])
    return score


# Searching for best motifs with random searching and checks for score of motif
def Randomized_Motif_Search(Dna, k, t):
    Motifs = Random_Select_Motifs(Dna, k, t)
    BestMotifs = list(Motifs)

    while True:
        profile = Profile(Motifs, k)
        Motifs = Motif(profile, Dna)
        if Score(Motifs, k, t) < Score(BestMotifs, k, t):
            BestMotifs = list(Motifs)
        else:
            return BestMotifs


# Open, read and processing input data from text-file
with open(file_name, 'r') as f:

    k, t = [int(x) for x in f.readline().strip().split(' ')]
    Dna = [x.strip() for x in f.readlines()]

    BestMotifs = Randomized_Motif_Search(Dna, k, t)

    for i in range(0, n):
        Motifs = Randomized_Motif_Search(Dna, k, t)
        if Score(Motifs, k, t) < Score(BestMotifs, k, t):
            BestMotifs = Motifs
            print(BestMotifs, Score(BestMotifs, k, t))

# Saving output data in text-file
with open('output_BA2F.txt', 'w') as out:
    for motif in BestMotifs:
        out.write(motif + '\n')
