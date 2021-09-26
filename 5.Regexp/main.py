from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from collections import OrderedDict

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# RegExp
# \w+@\w+\.\w+  - поиск email
# ^(\w+)[,\s](\w+)[,\s](\w+|\s*).*(ФНС|Минфин|Ivan) - разбивка по ФИО
# \1,\2,\3,\4 - разбивка по ФИО
# (\+7|8)\s*(\s*|\()(495)(\s*|\)|-)\s*(\d{3})(\s*|\)|-)(\d{2})(\s*|\)|-)(\d{2})  регулярка для телефона
# +7(\3)\5-\7-\9 замена телефона
# (\(|\s*)(доб)[.\s*]\s*(\d+)(\)|\s*) правка доб. телефона
# \2.\3 правка доб. телефона


contacts_list_changed = []
for el in range(0, len(contacts_list)):
    lines = ','.join([str(i) for i in contacts_list[el]])
    regexp_changed_numbers_phone = re.compile(
        r"(\+7|8)\s*(\s*|\()(495)(\s*|\)|-)\s*(\d{3})(\s*|\)|-)(\d{2})(\s*|\)|-)(\d{2})")
    lines_with_changed_numbers_phone = regexp_changed_numbers_phone.sub(r"+7(\3)\5-\7-\9", lines)
    regexp_changed_additional_numbers_phone = re.compile(r"(\s*)(\(|\s*)(доб)[.\s*]\s*(\d+)(\)|\s*)")
    lines_with_changed_numbers_phone_all = regexp_changed_additional_numbers_phone.sub(r" \3.\4",
                                                                                       lines_with_changed_numbers_phone)
    contacts_list_changed.append(lines_with_changed_numbers_phone_all.split(','))


contacts_lfs = []
for el in contacts_list_changed:
    lines_lfs = ' '.join(el[0:3])
    contacts_lfs.append(lines_lfs.split(' '))
for el in range(len(contacts_list_changed)):
    for el1 in range(3):
        contacts_list_changed[el][el1] = contacts_lfs[el][el1]


index_list = []
for el in range(len(contacts_list_changed)):
    for el1 in range(el, len(contacts_list_changed)):
        if el1 != el:
            if contacts_list_changed[el][0] == contacts_list_changed[el1][0] and contacts_list_changed[el][1] == contacts_list_changed[el1][1]:
                index_list.append(int(el1))
                for index, elem in enumerate(contacts_list_changed[el1]):
                    if elem not in contacts_list_changed[el]:
                        contacts_list_changed[el][index] = contacts_list_changed[el1][index]


index_list.reverse()
for el in index_list:
    contacts_list_changed.remove(contacts_list_changed[el])
pprint(contacts_list_changed)


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_changed)
