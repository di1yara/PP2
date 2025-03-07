import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.R_OK) and os.access(file_path, os.W_OK):
            os.remove(file_path) 
            print(f"File '{file_path}' deleted successfully!")
        else:
            print(f"Error: No permission to delete '{file_path}'.")
    else:
        print(f"Error: The file '{file_path}' does not exist.")


delete_file("file.txt")
