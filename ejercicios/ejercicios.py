sequence = [1,2,5,1,2]
bsequence = [1,3,4,2,1,5]

def bsolution(sequence):
    
    num = -(10**6)

    for indice, n in enumerate(sequence):

        indice_sig = sequence[indice + 1]
        if n >= num:
            num = n
            print(sequence[indice],sequence[indice_sig])

a = bsolution(sequence)
print(a)


