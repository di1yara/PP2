import os 
dir_path=os.path.join(os.getcwd(),"new_directory")
def deleted_fd(target_dir):
    if os.path.exists(target_dir)and os.path.isdir(target_dir):
        for file_name in os.listdir(target_dir):
            file_path=os.path.join(target_dir,file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File deleted: {file_path}")
        os.rmdir(target_dir)
        print(f" Directory deleted: {target_dir}")
    else:
        print(f'"{target_dir}" undefined ')


deleted_fd(dir_path)

