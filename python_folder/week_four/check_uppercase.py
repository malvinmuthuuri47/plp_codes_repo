import sys

# get output filename from command line, default to 'output.txt'
if len(sys.argv) > 1:
    output_file = sys.argv[1]
else:
    output_file = "output.txt"

try:
    with open("output.txt", "r") as f:
	    text = f.read()
	
	    if text.isupper():
		    print(f"The file {output_file}'s content is uppercase")
	    else:
		    print("The file {output_file}'s content is lowercase")
except Exception as e:
    print(f"Unexpected error: {e}")
