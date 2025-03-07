def writter(filename,datalist):
    with open(filename,"w") as file:
        for item in datalist:
            file.write(str(item)+"\n")

my_list=[1,2,3,4,5,6]
filename="writer.txt"
 
writter(filename,my_list)