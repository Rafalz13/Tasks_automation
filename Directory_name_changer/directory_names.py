import os

def get_dir_names(path_to_dirs=""):
    os.chdir(path_to_dirs)
    list_dir_prep = os.listdir()
    list_dir_post = []

    for dir in list_dir_prep:
        if "." not in dir:
            list_dir_post.append(dir)
    return list_dir_post




