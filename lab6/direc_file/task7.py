def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dest:
            dest.write(src.read())  
        print(f"File copied successfully from '{source}' to '{destination}'!")
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


copy_file("source.txt", "destination.txt")
