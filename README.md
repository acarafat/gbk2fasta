# gbk2fasta
Convert a GenBank file to fasta. 

# Conversion options
There are three options: `fna`, `ffn`, and `faa`. 
`fna` extracts all GenBank sequence records.
`ffn` extracts only CDS records.
`fna` extracts CDS and translate it into amino acid sequences.

# Usage
This is a Python script to be used in command line/shell/terminal. Use the following prompt to convert .gbk file to .fasta:
`python gbk2fasta.py input.gbk option`

# Output
`input.gbk.fasta` file will be created in the same directory of `input.gbk` file

# Dependency
It requires Biopython.
