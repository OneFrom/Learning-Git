# программа чтения файла по строкам 
filename1 = input('Введите имя копируемого файла:')
with open(filename1,'r') as file1:
    my_strings = file1.readlines()
    for my_str in my_strings:
            print(my_str)
    file1.close()
