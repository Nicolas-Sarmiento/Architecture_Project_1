import sys
import re
import argparse

def rom2text(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            lines = f_in.readlines()
            for line in lines:
                if "v3.0" in line:
                    continue

                if ":" in line:
                    content = line.split(':')[1].strip()
                                        
                    words = content.split()
                    print(words)
                    for word in words:
                        f_out.write(f"{word}\n")
        
        print(f"File created: {output_file}")

    except FileNotFoundError:
        print("Error: No input file")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract Hex data from Logisim v3.0 files to a clean text column.")
    
    parser.add_argument("input", help="Input Logisim .hex file path")
    parser.add_argument("-o", "--output", default="columna_out.txt", help="Output text file path (default: columna_out.txt)")

    args = parser.parse_args()
    
    rom2text(args.input, args.output)
