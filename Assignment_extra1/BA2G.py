# Implement Gibbs Sampler (Rosalind BA2G)

from random import randint, choices

file_name = str(input("Input file: "))
a = int(input("Anzahl Durchläufe: "))


# Randomized selection of motifs in every DNA-string
def Random_Select_Motifs(Dna, k, t):
    Motifs = []

    for seq in Dna:
        index = randint(0, len(seq) - k)
        Motifs.append(seq[index:index + k])
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
def Motif(profile, Seq, k):
    probs = []

    for i in range(len(Seq) - k + 1):
        Sum = 1
        for j in range(k):
            Sum *= (profile[j][Seq[i+j]])
        probs.append(Sum)
    return probs


# Calculating of the score for motifs in relation to Consensus-sequence
def Score(Motifs, k, t):
    profile = Profile(Motifs, k)
    score = 0

    for a in range(len(profile)):
        score += (4 + t - profile[a][max(profile[a], key=profile[a].get)])
    return score


# Random choice and deletion of one motif in profile and insertion of new random selected motif to profile.
# Also searching for best motifs with random searching and checks for score of motif
def Gibbs_Sampler(Dna, k, t, N):
    Motifs = Random_Select_Motifs(Dna, k, t)
    BestMotifs = list(Motifs)

    for j in range(N):
        i = randint(0, t - 1)
        Motifs.pop(i)
        profile = Profile(Motifs, k)

        temp = Motif(profile, Dna[i], k)
        index = choices(list(range(0, len(Dna[i]) - k + 1)), temp)

        Motifs.insert(i, Dna[i][index[0]:index[0] + k])

        if Score(Motifs, k, t) < Score(BestMotifs, k, t):
            BestMotifs = list(Motifs)
    return BestMotifs


# Open, read and processing input data from text-file
with open(file_name, 'r') as f:

    k, t, N = [int(x) for x in f.readline().strip().split(' ')]
    Dna = [x.strip() for x in f.readlines()]

    BestMotifs = Gibbs_Sampler(Dna, k, t, N)

    for i in range(0, a):
        Motifs = Gibbs_Sampler(Dna, k, t, N)
        if Score(Motifs, k, t) < Score(BestMotifs, k, t):
            BestMotifs = Motifs
            print(BestMotifs, Score(BestMotifs, k, t))

# Saving output data in text-file
with open('output_BA2G.txt', 'w') as out:
    for motif in BestMotifs:
        out.write(motif + '\n')
