def counter(filename):
    with open(filename,"r") as file:
        lines=file.readlines()
        return len(lines)
    
filename="file.txt"
result=counter(filename)
print(result)