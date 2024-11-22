import json
import sys

def interpret(binary_file, result_file, memory_range):
    with open(binary_file, 'rb') as f:
        binary_data = f.read()

    memory = [0] * 1024  # Простая модель памяти
    pc = 3 # Счётчик команд

    while pc < len(binary_data) + 1:
        if pc == 5:
            op = binary_data[pc]
            op1 = binary_data[pc - 1]
            op2 = binary_data[pc - 2]
            op3 = binary_data[pc - 3]
            op4 = binary_data[pc - 4]
            op5 = binary_data[pc - 5]
        opcode = binary_data[pc] & 0b111111

        if opcode == 30:  # LOAD_CONST
            data = binary_data[pc - 5:pc + 1]
            bytes_array = int.from_bytes(data, 'big')
            bytes_array >>= 6

            const_value = bytes_array & 0b1111111111111111111111111111
            addr = (bytes_array >> 28) & 0b11111111111

            memory[addr] = const_value
            pc += 4
        elif opcode == 14:  # READ_MEM
            data = binary_data[pc - 3:pc + 1]
            bytes_array = int.from_bytes(data, 'big')

            addr_src = (bytes_array >> 6) & 0b11111111111
            addr_dst = (bytes_array >> 17) & 0b11111111111

            memory[addr_dst] = memory[memory[addr_src]]
            pc += 4
        elif opcode == 7:  # WRITE_MEM
            data = binary_data[pc - 3:pc + 1]
            bytes_array = int.from_bytes(data, 'big')

            addr_src = (bytes_array >> 6) & 0b11111111111
            addr_dst = (bytes_array >> 17) & 0b11111111111

            memory[memory[addr_dst]] = memory[addr_src]
            pc += 4
        elif opcode == 36:  # NOT
            data = binary_data[pc - 3:pc + 1]
            bytes_array = int.from_bytes(data, 'big')

            addr_src = (bytes_array >> 6) & 0b11111111111
            addr_dst = (bytes_array >> 17) & 0b11111111111

            memory[addr_src] = ~memory[memory[addr_dst]]
            pc += 4
        else:
            pc += 2

    start, end = map(int, memory_range.split(":"))
    result = memory[start:end]

    with open(result_file, 'w') as f:
        json.dump(result, f, indent=4)


if __name__ == "__main__":
    interpret(sys.argv[1], sys.argv[2], sys.argv[3])
# if __name__ == "__main__":
#     interpret("program.bin", "result.json", "0:100")



