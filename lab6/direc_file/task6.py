import os
import string

def create_text_files(directory="letters"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for letter in string.ascii_uppercase: 
        filename = os.path.join(directory, f"{letter}.txt")
        with open(filename, "w") as file:
            file.write(f"This is file {letter}.txt\n")  

    print(f"26 text files created successfully in '{directory}' folder!")

create_text_files()
