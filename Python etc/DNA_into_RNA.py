# transcribing DNA into RNA

DNA_seq = str(input("Input DNA-sequence: "))
DNA_seq = str.upper(DNA_seq)


RNA_complement = ""
n = len(DNA_seq) - 1
while n >= 0:
    if DNA_seq[n] == "A":
        RNA_complement += "A"
        n = n - 1
    elif DNA_seq[n] == "T":
        RNA_complement += "U"
        n = n - 1
    elif DNA_seq[n] == "C":
        RNA_complement += "C"
        n = n - 1
    elif DNA_seq[n] == "G":
        RNA_complement += "G"
        n = n - 1
    else:
        print("Abbruch! Fehlerhafte Eingabe")
        break

print("output:   " + RNA_complement[::-1])  # [::-1] for reverse output
