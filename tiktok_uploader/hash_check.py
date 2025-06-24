import hashlib

def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def is_file_unchanged(file_path, expected_hash):
    current_hash = get_file_hash(file_path)
    return current_hash == expected_hash

