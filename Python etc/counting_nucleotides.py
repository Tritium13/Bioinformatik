# counting nucleotides in DNA sequence

seq = str(input("DNA-sequence: "))

n = len(seq) - 1
count_A = 0
count_T = 0
count_C = 0
count_G = 0

while n >= 0:
        if seq[n] == 'A':
            count_A += 1
            n = n - 1
        elif seq[n] == 'T':
            count_T += 1
            n = n - 1
        elif seq[n] == 'C':
            count_C += 1
            n = n - 1
        elif seq[n] == 'G':
            count_G += 1
            n = n - 1
        else:
            print("Abbruch! Fehlerhafte Eingabe")
            break

print(count_A, count_C, count_G, count_T)