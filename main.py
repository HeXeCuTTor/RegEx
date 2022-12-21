from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def correct_name():
    name_pattern = r'([А-Я])'
    name_substitution = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(name_pattern, name_substitution, line).split())) == 3:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
            column[2] = re.sub(name_pattern, name_substitution, line).split()[2]
        elif len((re.sub(name_pattern, name_substitution, line).split())) == 2:
            column[0] = re.sub(name_pattern, name_substitution, line).split()[0]
            column[1] = re.sub(name_pattern, name_substitution, line).split()[1]
            column[2] = ''
    return

def correct_phone():
    name_pattern = r"(\+7|8{1})\s*\(?(\d{3})\)?[\s|-]*(\d{3})[\s|-]*(\d{2})[\s|-]*(\d+)(\s?)\(?(доб\.)?(\s?)(\d+)?(\)?)"
    result = r"+7(\2)-\3-\4-\5\6\7\9"
    for column in contacts_list:
        column[5] = re.sub(name_pattern,result,column[5])
    return

def correct_repeating():
    contacts = [['lastname','firstname','surname','organization','position','phone','email']]
    list_contacts = []
    for column in contacts_list[1:]:
        surname = column[0]
        name = column[1]
        if column[2] == '':
            continue
        else:
            second_name = column[2]
        organization = column[3]
        job = column[4]
        phone = column[5]
        email = column[6]
        list_contacts = [surname,name,second_name,organization,job,phone,email]
        for names in contacts:
            if names[0] == surname:
                if names[1] == name:
                    names[3] = organization
                    names[4] = job
                    names[5] = phone
                    names[6] = email
                    list_contacts = []
                else:
                  continue
        if list_contacts != []:
            contacts.append(list_contacts)
    return contacts


if __name__ == '__main__':
    correct_name()
    correct_phone()
    correct_repeating()
    # pprint(contacts_list)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_repeating())


