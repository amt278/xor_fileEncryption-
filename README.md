# File Encryptor/Decryptor

A simple Python script to encrypt and decrypt files using a XOR-based method. This tool processes files byte by byte, allowing secure and reversible transformations.

---

## Features

- **Encryption**: Transforms the file into an encoded format with a specified key.
- **Decryption**: Reverts the encoded file back to its original form using the same key.
- Simple, efficient, and works with any file format.

---

## How It Works

- The script uses a **key** (an integer between 1 and 255) to perform a XOR operation on each byte of the file.
- The same key is required to decrypt the file.

---

## Usage

1. Clone or download the script.
2. Run the script using Python:
   ```bash
    python3 encryptor.py
   ```
