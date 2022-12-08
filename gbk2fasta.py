from Bio import SeqIO
import sys


def gbk2fasta(gbkFile):
    '''
    INPUT: A GenBank file containing one or multiple seq-record
    OUTPUT: It writes a single fasta file containing all seq-records
    '''
    allSeq = []
    for seq in SeqIO.parse(gbkFile, 'genbank'):
        allSeq.append(seq)
    SeqIO.write(allSeq, gbkFile+'.fasta', 'fasta')
    pass


if __name__ == "__main__":
    inputFile = sys.argv[1]
    gbk2fasta(inputFile)
    print('Done.')
