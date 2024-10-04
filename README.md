# Magic Bytes and File Types Identifier

## Overview

The **Magic Bytes and File Types Identifier** is a Python script that allows users to identify file types based on their magic bytes and retrieve magic bytes for known file types. It supports partial matches and suggests similar file types for unrecognized inputs.

## Features

- **Identify File Types**: Input magic bytes to determine the corresponding file type.
- **Retrieve Magic Bytes**: Provide a file type to get its associated magic bytes.
- **Partial Matches**: Handle inputs with incomplete magic bytes and provide possible matches.
- **Suggestions**: Suggest similar file types for unrecognized inputs.

## Installation

**Clone the Repository**:
```bash
git clone https://github.com/RahulRaviHulli/Magic-Bytes-File-Type-Identifier.git

cd magic-bytes-file-type-identifier
```
## Usage:
**Run the script using Python 3.x**:

Identify File Type Using Magic Bytes:
```bash
python3 magic_bytes_file_type_identifier.py -m "FFD8FF"
```

Retrieve Magic Bytes for a File Type:

```bash
python3 magic_bytes_file_type_identifier.py -x "JPEG"
```

## Command Line Options:
```bash
-h, --help: Show help message and exit.
-m MAGIC, --magic MAGIC: Pass magic bytes to get the corresponding file type.
-x FILETYPE, --filetype FILETYPE: Pass a file type to get the associated magic bytes.
```

## Examples

Identify File Type by Magic Bytes:
```bash
python3 magic_bytes_file_type_identifier.py -m "FFD8FF"

Output:
The magic bytes 'FFD8FF' correspond to the file type: jpeg
```

Get Magic Bytes for a File Type:
```bash
python3 magic_bytes_file_type_identifier.py -x "JPEG"
Output:
The file type 'jpeg' corresponds to the magic bytes: FFD8FF
```

Handle Unrecognized File Type:
```bash
python3 magic_bytes_file_type_identifier.py -x "JPG"
Output:
File type 'jpg' not recognized.
Did you mean: jpeg?
```

## License
This project is not licensed under any specific license. Feel free to use and modify it as needed.

## Contributions
Contributions are welcome! Please feel free to open issues or submit pull requests for improvements or additional file types.


