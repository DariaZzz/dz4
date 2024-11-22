import json
import sys

COMMANDS = {
    "LOAD_CONST": 30,
    "READ_MEM": 14,
    "WRITE_MEM": 7,
    "NOT": 36,
}

def assemble(input_file, binary_file, log_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    binary_data = bytearray()
    log_data = []

    for line in lines:
        parts = line.strip().split()
        command = parts[0]
        args = list(map(int, parts[1:]))
        opcode = COMMANDS[command]

        if command == "LOAD_CONST":
            packed =  (opcode & 0b111111) | (args[0] << 6) | (args[1] << 34)
            binary_data.extend(packed.to_bytes(6, byteorder='big'))
        else:
            packed = (opcode & 0b111111) | (args[0] << 6) | (args[1] << 17)
            binary_data.extend(packed.to_bytes(4, byteorder='big'))

        log_data.append({
            "command": command,
            "opcode": opcode,
            "args": args,
            "packed": list(binary_data[-(6 if command == "LOAD_CONST" else 4):])
        })

    with open(binary_file, 'wb') as f:
        f.write(binary_data)

    with open(log_file, 'w') as f:
        json.dump(log_data, f, indent=4)

if __name__ == "__main__":
    assemble(sys.argv[1], sys.argv[2], sys.argv[3])

# if __name__ == "__main__":
#     assemble('program1.asm', 'program.bin', 'log.json')
