def str_file(path):
    import os
    strfile = os.path.basename(path)
    name, extension = os.path.splitext(strfile)
    direct = os.path.dirname(path)
    return direct, name, extension


path = r'/users/dmitr/OneDrive/Рабочий стол/Py_Task5/file.txt'
directory, name, extension = str_file(path)
print('Directory: ', directory)
print('Name: ', name)
print('Extension: ', extension)
