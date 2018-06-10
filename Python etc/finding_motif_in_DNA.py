# finding a motif in DNA sequence

seq = str(input("Input sequence: "))
seq = str.upper(seq)
motif = str(input("Input motif: "))
motif = str.upper(motif)


def finding_motif(seq, motif):
    result = []
    len_seq = len(seq)
    len_motif = len(motif)
    for i in range(0, len_seq - len_motif + 1):
        if seq[i:i + len_motif] == motif:
            result.append(i + 1)
    return result


print(finding_motif(seq, motif))
