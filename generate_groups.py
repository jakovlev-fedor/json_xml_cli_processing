import json
import xmltodict

# --------------- OPEN REQUIRED FILES ---------------
with open('rooms.json', 'r') as file:
    rooms_list = json.load(file)

with open('students.json', 'r') as file:
    students_list = json.load(file)


# --------------- GENERATE NEW JSON ---------------
groups_list = rooms_list

for i, room in enumerate(groups_list):
    groups_list[i]['student'] = []

for student in students_list:
    room_id = student['room']
    room = groups_list[room_id]
    room['student'].append(student)
    groups_list[room_id] = room


# --------------- ADJUST NEW JSON FOR XML CONVERSION ---------------
rooms_dict = {}
for i, room in enumerate(groups_list):
    room_name = f'Room_{i}'
    rooms_dict[room_name] = groups_list[i]
single_root_dict = {'root': rooms_dict}
groups_xml_data = xmltodict.unparse(single_root_dict, pretty=True)


# --------------- WRITE NEW JSON ---------------
with open('groups.json', 'w') as write_file:
    json.dump(groups_list, write_file, indent=4)

# --------------- WRITE TO NEW XML ---------------
with open('groups.xml', 'w') as file:
    file.write(groups_xml_data)


# 6 TODO: implement cli integration support

# 7 TODO: refactor code
