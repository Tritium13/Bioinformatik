# Creating reverse complement of a DNA sequence

input_sequence = str(input("Input sequence: "))
input_sequence = str.upper(input_sequence)


reverse_complement = ""
n = len(input_sequence) - 1
while n >= 0:
    if input_sequence[n] == "A":
        reverse_complement += "T"
        n = n - 1
    elif input_sequence[n] == "T":
        reverse_complement += "A"
        n = n - 1
    elif input_sequence[n] == "C":
        reverse_complement += "G"
        n = n - 1
    elif input_sequence[n] == "G":
        reverse_complement += "C"
        n = n - 1
    else:
        print("Abbruch! Fehlerhafte Eingabe")
        break

# print("input :   " + input_sequence)
print("reverse complement:   " + reverse_complement)
