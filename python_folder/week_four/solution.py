word_count = 0

try:
    with open("input.txt", "r") as f, open("output.txt", "w") as out:
        for line in f:
            words = line.split()
            word_count += len(words)

            processed_line = line.upper()
            out.write(processed_line)

    print(f"Done! Created 'output.txt' in the current directory.")
except Exception as e:
    print(f"Unexpected error {e}")
