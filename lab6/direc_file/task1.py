import os
def list_all():
    path=os.getcwd()
    print(f"Listing contents of: {path}\n")
    
    for item in os.listdir(path):
        print(item)

list_all()