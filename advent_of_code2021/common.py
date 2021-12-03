def get_data_from_file(filename):
    with open(filename) as f:
        file_data = f.read()
    return file_data
