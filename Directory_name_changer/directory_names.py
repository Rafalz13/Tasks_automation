import os

def get_dir_names(path_to_dirs=""):
    os.chdir(path_to_dirs)
    list_dir_prep = os.listdir()
    list_dir_post = []

    for dir in list_dir_prep:
        if "." not in dir:
            list_dir_post.append(dir)
    return list_dir_post


def change_dirs_name(old="",new_name=""):
    os.rename(old, new_name)

def go_through_dirs(old_name,new_name,list_of_dirs=[]):
    for dir in list_of_dirs:
        os.chdir(dir)
        change_dirs_name(old_name,new_name)
        os.chdir("..")



old_name = input("old name: ")
new_name = input("new name: ")
path_to_dirs = input("path to directories: ")
list_dirs = get_dir_names(path_to_dirs)
go_through_dirs(old_name, new_name, list_dirs)




