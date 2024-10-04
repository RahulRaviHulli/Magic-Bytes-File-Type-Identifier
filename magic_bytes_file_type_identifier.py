import argparse
import difflib

def load_magic_bytes(file_path):
    magic_bytes_dict = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() and not line.startswith('#'):  # Ignore comments and empty lines
                    parts = line.split()
                    if len(parts) >= 2:
                        magic_bytes = parts[0].strip()
                        file_type = " ".join(parts[1:]).strip()
                        magic_bytes_dict[file_type.lower()] = magic_bytes  # Store file type in lowercase
    except FileNotFoundError:
        print("The magic bytes file was not found.")
        exit(1)
    return magic_bytes_dict

def suggest_similar_file_type(magic_bytes_dict, file_type_input):
    file_types = list(magic_bytes_dict.keys())
    suggestions = difflib.get_close_matches(file_type_input, file_types, n=3, cutoff=0.6)
    if suggestions:
        print(f"Did you mean: {', '.join(suggestions)}?")
    else:
        print("No similar file types found.")

def find_file_type(magic_bytes_dict, magic_input):
    magic_input = magic_input.replace(" ", "").lower()  # Clean input
    matches = {k: v for k, v in magic_bytes_dict.items() if k.startswith(magic_input)}

    if matches:
        if len(matches) == 1:
            for file_type, magic in matches.items():
                print(f"The magic bytes '{magic_input}' correspond to the file type: {file_type}")
        else:
            print(f"The magic bytes '{magic_input}' partially match the following file types:")
            for file_type in matches.keys():
                print(f"- {file_type}")
    else:
        print(f"Magic bytes '{magic_input}' not recognized.")

def find_magic_bytes(magic_bytes_dict, file_type_input):
    file_type_input = file_type_input.lower()  # Clean input
    magic_bytes = magic_bytes_dict.get(file_type_input)

    if magic_bytes:
        print(f"The file type '{file_type_input}' corresponds to the magic bytes: {magic_bytes}")
    else:
        print(f"File type '{file_type_input}' not recognized.")
        suggest_similar_file_type(magic_bytes_dict, file_type_input)

def main():
    parser = argparse.ArgumentParser(description='Identify file type based on magic bytes or get magic bytes for a file type.')
    parser.add_argument('-m', '--magic', type=str, help='Pass magic bytes to get file type.')
    parser.add_argument('-x', '--filetype', type=str, help='Pass file type to get magic bytes.')

    args = parser.parse_args()

    magic_bytes_dict = load_magic_bytes('magic_bytes.txt')  # Load magic bytes from the text file

    if args.magic:
        find_file_type(magic_bytes_dict, args.magic)
    elif args.filetype:
        find_magic_bytes(magic_bytes_dict, args.filetype)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

