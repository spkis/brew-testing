import hashlib

# Path to the local file
file_path = 'hello.sh'  # Replace with the actual file path

# Function to compute SHA-256
def compute_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b''):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "File not found. Please check the file path."

# Compute SHA-256 for the given file
print(compute_sha256(file_path))