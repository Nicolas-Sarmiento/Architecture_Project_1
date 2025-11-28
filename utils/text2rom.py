import argparse
def pack_rom(archivo_txt_entrada, archivo_hex_salida):
    """
    Lee una lista de valores hex (uno por línea) y genera
    el formato 'v3.0 hex words addressed' de Logisim.
    """
    print("Generando archivo de memoria Logisim...")
    
    memoria = []
    try:
        with open(archivo_txt_entrada, 'r') as f:
            lineas = f.readlines()
            for l in lineas:
                limpio = l.strip()
                if limpio:
                    memoria.append(limpio)
        
        while len(memoria) < 64:
            memoria.append("0") 

        with open(archivo_hex_salida, 'w') as f:
            #f.write("v2.0 raw\n") # Usamos v2.0 raw porque es MAS FACIL y Logisim lo lee igual de bien
            
            # Escribir los valores separados por espacios/nuevas lineas
            # Logisim v2.0 raw es simplemente una lista de hex
            #f.write("\n".join(memoria))
            
            # Si REALMENTE necesitas el formato v3.0 (el largo con ceros):
            # Descomenta esto y comenta lo de arriba:
            
            f.write("v3.0 hex words addressed\n")
            for i in range(0, len(memoria), 8):
                linea = f"{i:02x}:"
                chunk = memoria[i:i+8]
                datos = " ".join(chunk)
                f.write(f"{linea} {datos}\n")
            

        print(f"File '{archivo_hex_salida}' generated.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text to ROM hex v3")
    
    parser.add_argument("input", help="Input Logisim .hex file path")
    parser.add_argument("-o", "--output", default="columna_out.txt", help="Output text file path (default: columna_out.txt)")

    args = parser.parse_args()
    pack_rom(args.input, args.output)
    
