import os

def rename_file():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\OOP\prank") #r:raw path
    print(file_list)
    saved_path = os.getcwd() #check current wdir
    print ("Current Working Dir is "+saved_path)
    os.chdir(r"C:\OOP\prank")
    
    #(2) for each file, rename filename
    for file_name in file_list:
        os.rename(filename, file_name.translate(None, "0123456789"))
    os.chdir(saved_path) #why happens on C:\OOP?
    
rename_file()
