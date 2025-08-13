# ask the user for file names
program_input_file = input("Enter the input file name (default: input.txt): ") or "input.txt"
program_output_file = input("Enter the output file name (default: output.txt): ") or "output.txt"

if not program_output_file.lower().endswith(".txt"):
    program_output_file += ".txt"

word_count = 0

try:
    with open(program_input_file, "r") as f, open(program_output_file, "w") as out:
        for line in f:
            words = line.split()
            word_count += len(words)

            processed_line = line.upper()
            out.write(processed_line)

    print(f"Done! Created {program_output_file} in the current directory.")
except Exception as e:
    print(f"Unexpected error: {e}")
