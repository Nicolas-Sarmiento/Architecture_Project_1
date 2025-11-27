import sys
import argparse

def convert_obj_to_logisim(input_file, output_file):
    memory = [0] * 65536
    try:
        with open(input_file, 'rb') as f_in:
            origin_bytes = f_in.read(2)
            if not origin_bytes:
                print("Error: Empty input file.")
                return

            current_addr = int.from_bytes(origin_bytes, byteorder='big')
            print(f"Origin address found: x{current_addr:04X}")

            while True:
                word_bytes = f_in.read(2)
                if not word_bytes:
                    break 
                
                val = int.from_bytes(word_bytes, byteorder='big')
                
                if current_addr < 65536:
                    memory[current_addr] = val
                    current_addr += 1

        with open(output_file, 'w') as f_out:
            f_out.write("v3.0 hex words addressed\n")
            
            for i in range(0, 65536, 16):
                line_start = f"{i:04x}:"
                data_block = ""
                for j in range(16):
                    data_block += f" {memory[i + j]:04x}"
                
                f_out.write(line_start + data_block + "\n")

        print(f"Converted '{input_file}' to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert LC-3 .obj binary files to Logisim .hex format")
    parser.add_argument("-i","--input", help="Path to the .obj input file")
    parser.add_argument("-o", "--output", default="memory.hex", help="Path to the .hex output file")
    args = parser.parse_args()
    convert_obj_to_logisim(args.input, args.output)
