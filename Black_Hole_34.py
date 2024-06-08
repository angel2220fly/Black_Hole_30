def read_numbers_from_file(file_path):
    with open(file_path, 'rb') as file:  # Reading in binary mode
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def compress_option1(numbers):
    compressed = sum(numbers)
    return [compressed]

def compress_option2(numbers):
    if not numbers:
        return []
    compressed = [numbers[0]]
    for i in range(1, len(numbers)):
        compressed.append(numbers[i] - numbers[i-1])
    return compressed

def extract_option1(compressed, original_length):
    raise NotImplementedError("Extraction from summation compression is not feasible.")

def extract_option2(compressed):
    if not compressed:
        return []
    extracted = [compressed[0]]
    for i in range(1, len(compressed)):
        extracted.append(extracted[-1] + compressed[i])
    return extracted

def to_base256(numbers):
    base256_encoded = bytes(numbers)
    return base256_encoded

def from_base256(base256_encoded):
    numbers = list(base256_encoded)
    return numbers

def main():
    # Asking user for input and output file names
    input_file = input("Enter the name of the input file: ")
    compressed_output_file = input("Enter the name of the compressed output file: ")
    extracted_output_file = input("Enter the name of the extracted output file: ")
    
    # Reading input data from file
    numbers = read_numbers_from_file(input_file)
    print(f"Input Data: {numbers}")
    
    # Choosing compression option
    compress_option = int(input("Choose compression option (1 or 2): "))
    extract_option = int(input("Choose extraction option (1 or 2): "))
    
    # Compression
    if compress_option == 1:
        compressed_data = compress_option1(numbers)
        print(f"Compressed Option 1: {compressed_data}")
    elif compress_option == 2:
        compressed_data = compress_option2(numbers)
        print(f"Compressed Option 2: {compressed_data}")
    else:
        print("Invalid compression option selected.")
        return
    
    # Encoding compressed data
    base256_encoded = to_base256(compressed_data)
    
    # Writing encoded data to file
    write_to_file(compressed_output_file, base256_encoded)
    print(f"Base256 Encoded data written to {compressed_output_file}")
    
    # Reading encoded data from file
    encoded_data = read_numbers_from_file(compressed_output_file)
    
    # Decoding the encoded data
    decoded_numbers = from_base256(encoded_data)
    print(f"Decoded Numbers: {decoded_numbers}")
    
    # Extraction
    if extract_option == 1:
        try:
            extracted_data = extract_option1(compressed_data, len(numbers))
            print(f"Extracted Data Option 1: {extracted_data}")
        except NotImplementedError as e:
            print(e)
    elif extract_option == 2:
        extracted_data = extract_option2(decoded_numbers)
        print(f"Extracted Data Option 2: {extracted_data}")
    else:
        print("Invalid extraction option selected.")
        return
    
    # Writing extracted data to file
    write_to_file(extracted_output_file, bytes(extracted_data))
    print(f"Extracted data written to {extracted_output_file}")

if __name__ == "__main__":
    main()