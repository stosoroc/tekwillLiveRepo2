import os


def check_path_is_folder(path):
    if not os.path.exists(path):
        raise Exception('Path does not exist')
    if not os.path.isdir(path):
        raise Exception('Path is not a directory')


def get_file_names_from_path(path):
    file_names = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if not os.path.isdir(full_path):
            file_names.append(entry)
    return file_names


def bulk_rename(folder_path, prefix):
    check_path_is_folder(folder_path)
    files = get_file_names_from_path(folder_path)
    all_file_paths = [os.path.join(folder_path, file) for file in files]
    sorted_files = sorted(all_file_paths, key=os.path.getctime)
    for idx, file in enumerate(sorted_files):
        file_name = os.path.split(file)[-1]
        file_extenion = file_name.split('.')[-1]
        new_file_name = os.path.join(folder_path, f'{prefix}{idx + 1}.{file_extenion}')
        os.rename(file, new_file_name)


if __name__ == '__main__':
    path = input('Folder path:')
    # try: # EX1
    #     check_path_is_folder(path)
    #     file_names = get_file_names_from_path(path)
    #     print(file_names)
    # except Exception as ex:
    #     print(ex)
    try:  # EX2
        prefix = input('Prefix')
        bulk_rename(path, prefix)
    except Exception as ex:
        print(ex)
