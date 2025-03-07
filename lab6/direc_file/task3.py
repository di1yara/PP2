import os
def check_path(path):
    path = os.getcwd()
    if os.path.exists(path):
        print("The path exists!")
        
        sep = "\\" if "\\" in path else "/"
        
        if sep in path:
            directory, filename = path.rsplit(sep, 1)  
        else:
            directory, filename = "", path  

        print("Directory:", directory if directory else "(No directory, only filename)")
        print("Filename:", filename)
    else:
        print("The path does not exist.")

check_path(os.getcwd())
