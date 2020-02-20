#crear archivo fasta con las secuencias de interes para la subfamilia X
import pandas as pd
import sys
from Bio import SeqIO

idSequences = pd.read_csv(sys.argv[1])
fastaFile = sys.argv[2]

sequence = []
idElement = []


#hacemos la lectura del multifasta, en un array guardo el ID y la secuencia y luego los exporto...
for record in SeqIO.parse(fastaFile, "fasta"):
    for sequenceData in idSequences['id_sequence']:
        if record.id == sequenceData:
            sequence.append(record.seq)
            idElement.append(record.id)

fileWrite = open(sys.argv[3], 'w')

for i in range(len(sequence)):
    line = ">%s" % (idElement[i])
    fileWrite.write(line+"\n")
    seq = ""
    for res in sequence[i]:
        seq +=res
    fileWrite.write(seq+"\n")

fileWrite.close()
