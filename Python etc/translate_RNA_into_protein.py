# translation of RNA sequence into protein (aminoacid-sequence)

RNA_seq = str(input("Input sequence: "))
RNA_seq = str.upper(RNA_seq)

prot_seq = ""
n = len(RNA_seq) - 1
while n >= 0:
    if RNA_seq[n:n+3] == "UUU" or "UUC":
        prot_seq += "F"
        n = n - 3
    elif RNA_seq[n:n+3] == "UUA" or "UUG":
        prot_seq += "L"
        n = n - 3
    elif RNA_seq[n:n+3] == "UCC" or "UCU" or "UCA" or "UCG":
        prot_seq += "S"
        n = n - 3
    elif RNA_seq[n:n+3] == "UAU" or "UAC":
        prot_seq += "Y"
        n = n - 3
    elif RNA_seq[n:n+3] == "UGU" or "UGC":
        prot_seq += "C"
        n = n - 3
    elif RNA_seq[n:n+3] == "UGG":
        prot_seq += "W"
        n = n - 3
    elif RNA_seq[n:n+3] == "CUU" or "CUC" or "CUA" or "CUG":
        prot_seq += "L"
        n = n - 3
    elif RNA_seq[n:n+3] == "CCU" or "CCC" or "CCA" or "CCG":
        prot_seq += "P"
        n = n - 3
    elif RNA_seq[n:n+3] == "CAU" or "CAC":
        prot_seq += "H"
        n = n - 3
    elif RNA_seq[n:n+3] == "CAA" or "CAG":
        prot_seq += "Q"
        n = n - 3
    elif RNA_seq[n:n+3] == "CGU" or "CGC":
        prot_seq += "R"
        n = n - 3
    elif RNA_seq[n:n+3] == "AUU" or "AUC" or "AUA":
        prot_seq += "I"
        n = n - 3
    elif RNA_seq[n:n+3] == "AUG":
        prot_seq += "M"
        n = n - 3
    elif RNA_seq[n:n+3] == "ACU" or "ACC" or "ACA" or "ACG":
        prot_seq += "T"
        n = n - 3
    elif RNA_seq[n:n+3] == "AAU" or "AAC":
        prot_seq += "N"
        n = n - 3
    elif RNA_seq[n:n+3] == "AAA" or "AAG":
        prot_seq += "K"
        n = n - 3
    elif RNA_seq[n:n+3] == "AGU" or "AGC":
        prot_seq += "S"
        n = n - 3
    elif RNA_seq[n:n+3] == "AGA" or "AGG":
        prot_seq += "R"
        n = n - 3
    elif RNA_seq[n:n+3] == "GUU" or "GUC" or "GUA" or "GUG":
        prot_seq += "V"
        n = n - 3
    elif RNA_seq[n:n+3] == "GCU" or "GCC" or "GCA":
        prot_seq += "A"
        n = n - 3
    elif RNA_seq[n:n+3] == "GAU" or "GAC":
        prot_seq += "D"
        n = n - 3
    elif RNA_seq[n:n+3] == "GAA" or "GAG":
        prot_seq += "E"
        n = n - 3
    elif RNA_seq[n:n+3] == "GGU" or "GGC" or "GGA" or "GGG":
        prot_seq += "G"
        n = n - 3
    elif RNA_seq[n:n+3] == "UAA" or "UAG" or "UGA":
        prot_seq += ""
        break

print("protein-sequence:   " + prot_seq)  # [::-1] for reverse output
