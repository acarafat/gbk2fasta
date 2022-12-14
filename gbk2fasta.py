import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


def gbk2fasta(gbkFile):
    '''
    INPUT: A GenBank file containing one or multiple seq-record
    OUTPUT: It writes a single fasta file containing all seq-records
    '''
    allSeq = []
    for seq in SeqIO.parse(gbkFile, 'genbank'):
        allSeq.append(seq)

    return allSeq


def gbk2ffn(gbkPath):
    '''
    Iterate through GenBank features and look for CDS, update seq id and seq description, and finally convert into fasta file containing all the CDS sequence
    INPUT example: database/gbk/inoc131.gbk
    '''
    
    seq_record_list = []

    for gb_record in SeqIO.parse(gbkPath, 'genbank'):
        for gb_feature in gb_record.features:
            if gb_feature.type == 'CDS':
                locus = gb_feature.qualifiers['locus_tag']
                product = gb_feature.qualifiers['product']
                seq_record = gb_feature.extract(gb_record)
                seq_record.id = locus[0]
                seq_record.name = ''
                seq_record.description = product[0]
                seq_record_list.append(seq_record)
    print(f'Total {len(seq_record_list)} CDS extracted')            
                
    return seq_record_list    


def gbk2faa(gbkPath):
    '''Iterate through GenBank feature and look for CDS, extract amino acid sequence convert into fasta file containing all the translated CDS sequence.
    INPUT example: 'database/gbk/inoc131.gbk'
    '''
    aa_seq_list = []

    for gb_record in SeqIO.parse(gbkPath, 'genbank'):
        for gb_feature in gb_record.features:
            if gb_feature.type == 'CDS':
                locus = gb_feature.qualifiers['locus_tag'][0]
                product = gb_feature.qualifiers['product'][0]
                aa_seq = gb_feature.extract(gb_record.seq).translate(table=11, cds=True)
                aa_seqRecord = SeqRecord(aa_seq, id=locus, description=product, name='')
                aa_seq_list.append(aa_seqRecord)
    print(f'Total {len(aa_seq_list)} CDS extracted')
    
    return aa_seq_list


if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputType = sys.argv[2]

    if outputType == "fna":
        allSeq = gbk2fasta(inputFile)
    elif outputType == "ffn":
        allSeq = gbk2ffn(inputFile)
    elfi outputType == "faa":
        allSeq = gbk2faa(inputFile)
        
    SeqIO.write(allSeq, gbkFile+'.fasta', 'fasta'
