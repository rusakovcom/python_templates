# delete n symbols in the begining of every file line

def remove_n_symbols_from_lines(input_file, output_file, n):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(line[n:])
    except Exception as e:
        print(f"An error occurred: {e}")

input_file=input("Please give file: ")
output_file=input("What will be the name of output file: ")
n=int(input("How many lines delete: "))

remove_n_symbols_from_lines(input_file, output_file, n)
