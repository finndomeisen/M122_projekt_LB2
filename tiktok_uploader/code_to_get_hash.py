import hashlib

def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

print(get_file_hash("config.cfg"))
