import os

file_root = "/var/www/html"

def get_file(file_path):
    """Returns /var/www/file_patha s string."""
    file_str = str()
    with open(os.path.join(file_root, file_path)) as f:
            file_str = "\n".join(f)
    return file_str
