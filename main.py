import os


def soldier(user_path, files_with_no_change, user_file_format):
    user_path = user_path
    files_with_no_change = files_with_no_change
    user_file_format = user_file_format
    i = 1
    os.chdir(user_path)
    files_in_folder = os.listdir(user_path)
    with open(files_with_no_change)as f:
        filelist = f.read().split("\n")
    for files in files_in_folder:
        if files not in filelist:
            os.rename(files, files.capitalize())
            name, extension = os.path.splitext(files)

        if extension == user_file_format:
            os.rename(files, f"{i}{user_file_format}")
            i = i+1


if __name__ == '__main__':
    User_path = input("Enter the path whose file names you want to prettify :")
    Files_with_no_change = input("Enter the files name whose name you don't want to chnage: ")
    User_file_format = input("Enter the file format whose name you want to prettify ")
    soldier(User_path, Files_with_no_change, User_file_format)