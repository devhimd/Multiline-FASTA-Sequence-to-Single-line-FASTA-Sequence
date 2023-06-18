def multiline_to_singleline_fasta(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        header = ''
        sequence = ''
        
        for line in f_in:
            line = line.strip()
            if line.startswith('>'):
                if header != '':
                    f_out.write(header + '\n')
                    f_out.write(sequence + '\n')
                header = line
                sequence = ''
            else:
                sequence += line
        
        if header != '':
            f_out.write(header + '\n')
            f_out.write(sequence + '\n')

# Usage example
input_file = 'input.fasta'
output_file = 'output.fasta'
multiline_to_singleline_fasta(input_file, output_file)

