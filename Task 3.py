import os
from os import listdir


# функция для получения списка файлов определенного типа в текущей папке, кроме exception
def file_name_list(need_type, exception):
    res_list = []
    for file_in_dir in listdir(os.getcwd()):
        if file_in_dir.count(need_type) != 0 and file_in_dir != exception:
            res_list.append(file_in_dir)
    return res_list


# функция для получения списка данных имя/ кол-во строк/ максимальное кол-во символов
def get_order(file_list):
    size_order = list()
    max_len_line = list()
    dict_order = dict()
    for file_txt in file_list:
        with open(get_path(file_txt), 'r', encoding='utf-8') as file_in_path:
            file_list = file_in_path.readlines()
            max_len_line.append((max_search(file_list) - 1) * '*')
            dict_order[file_txt] = len(file_list)
            size_order.append(len(file_list))
    return size_order, dict_order, max_search(max_len_line)


# функция для сортировки словаря по возрастянию кол-ва строк
def get_sort_order(size_order, dict_order):
    new_order = []
    for elem in sorted(size_order):
        for key, value in dict_order.items():
            if value == elem and key not in new_order:
                new_order.append(key)
    return new_order


# функция создания пути файла
def get_path(file_for_dir):
    return os.path.join(os.getcwd(), file_for_dir)


# функция нахождения максимального значения длины строк. Только со строками
def max_search(list_need):
    max_len = 0
    for elem in list_need:
        if len(elem) > max_len:
            max_len = len(elem)
    return max_len


# функция создания нового файла по логике сортировки
def create_result_file(given_name):
    with open(get_path(given_name), 'w') as new_file:
        format_list, dict_result, max_line_len = get_order(file_name_list('txt', given_name))
        need_order = get_sort_order(format_list, dict_result)
        for file_name in need_order:
            with open(get_path(file_name), 'r', encoding='utf-8') as file:
                new_file.write(f'{max_line_len * "-"}\n'
                               f'Источник данных: {file_name}\n'
                               f'Количество строк файла {file_name} равно: {dict_result[file_name]}\n'
                               f'{max_line_len * "-"}\n')
                for line in file:
                    new_file.write(line)
                new_file.write('\n')
    return True


if create_result_file('result_file.txt'):
    print(f'Файл успешно создан\n'
          f'Ссылка на файл:\n'
          f'        {get_path("result_file.txt")}\n'
          f'При последующей работе учитывайте, что файл будет перезаписан')
