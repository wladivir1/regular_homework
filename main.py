import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv


def red_file (file):
    with open(file) as f:
        rows = csv.reader(f, delimiter=",")
        contact_list = list(rows)
    return contact_list

## 1. Выполните пункты 1-3 задания.
## Ваш код
def format_number(contacts_list):
    number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_updated = list()
    for card in contacts_list:
        card_as_string = ','.join(card)
        formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated

def format_full_name(contacts_list):
    name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_updated = list()
    for card in contacts_list:
        card_as_string = ','.join(card)
        formatted_card = re.sub(name_pattern_raw, name_pattern_new, card_as_string)
        card_as_list = formatted_card.split(',')
        contacts_list_updated.append(card_as_list)
    return contacts_list_updated

def join_duplicates(contacts_list):
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    contacts_list_updated = list()
    for card in contacts_list:
        if card not in contacts_list_updated:
            contacts_list_updated.append(card)
    return contacts_list_updated

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
def write_file(contacts_list):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
        
def main(file):
    contacts = red_file(file)
    contacts = format_number(contacts)
    contacts = format_full_name(contacts)
    contacts = join_duplicates(contacts)
    contacts[0][2] = 'patronymic'
    write_file(contacts) 


if __name__ == '__main__':
    file = 'phonebook_raws.csv'
    main(file)        
        