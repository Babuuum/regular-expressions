from pprint import pprint
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


crutch = 0
my_list = []
part_of_my_list = []
for search in contacts_list:
  if len(search[0].split(" ")) != 1:
    if len(search[0].split(" ")) == 3:
      part_of_my_list = search[0].split(' ')
      part_of_my_list += search[3:7]
    else:
      part_of_my_list = search[0].split(' ')
      part_of_my_list += search[2:7]
  elif len(search[1].split(" ")) != 1:
    part_of_my_list = [search[0]]
    part_of_my_list += search[1].split(' ')
    part_of_my_list += search[3:7]
  else:
    part_of_my_list = search[0:7]
  my_list += [part_of_my_list]

for search in my_list:
  part_of_my_list = search[:2]
  crutch = search[0] + " " + search[1]
  for search_2 in my_list:
    crutch_2 = 2
    if crutch ==  search_2[0] + " " + search_2[1] and search != search_2:
      for search_3 in search[2:7]:
        if search_3 != search_2[crutch_2] and search_3 != "":
          part_of_my_list += [search_3]
        elif search_2[crutch_2] != "":
          part_of_my_list += [search_2[crutch_2]]
        else:
          part_of_my_list += [""]
        crutch_2 += 1
      my_list[my_list.index(search)] = part_of_my_list
      my_list.remove(search_2)
for search in my_list:
  pattern_phone = re.compile(r"(\+7|8)\s*\(?(495)\)?[-\s]*(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})((\s*)?\(?(доб.)\s(\d*)\)?)?")
  result  = pattern_phone.sub(r"+7(\2)\3-\4-\5\7\8\9", search[5])
  my_list[my_list.index(search)][5] = result


with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(my_list)


