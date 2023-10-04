import re
from collections import defaultdict
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv


def red_file (file):
    """Читает и возвращает данные с файла"""
    with open(file) as f:
        rows = csv.reader(f, delimiter=",")
        contact_list = list(rows)
    return contact_list

## 1. Выполните пункты 1-3 задания.
## Ваш код
def format_number(contacts_list):
    """Форматирует номер телефона и прводит к одному виду"""
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
                            
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    list_updated_number = list()
    
    for card in contacts_list:
        card_as_string = ','.join(card)      
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
        list_updated_number.append(formatted_card)
        
    return list_updated_number  

def format_full_name(contacts_list):
    """Форматирует фамилию имя отчество"""
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
                       
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    list_updated_name = list()
    
    for card in contacts_list:
        card_as_string = ''.join(card)
        formatted_card = re.sub(name_pattern_raw, name_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        list_updated_name.append(card_as_list)
        
    return list_updated_name

def join_duplicates(contacts_list):
    """Убирает дубили и списка"""
    data = defaultdict(list)
    
    for i in contacts_list:
        key = tuple(i[:2])
        for j in i:
            if j not in data[key]:
                data[key].append(j)
    new_list = list(data.values())
   
    return new_list

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
def write_file(contacts_list):
    """Записывает данные в файл"""
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
        
def main(file):
    contacts = red_file(file)
    number = format_number(contacts)
    name = format_full_name(number)
    contacts = join_duplicates(name)
    contacts[0][2] = 'patronymic'
    write_file(contacts) 


if __name__ == '__main__':
    file = 'phonebook_raws.csv'
    main(file)        
        