import json

with open('rooms.json', 'r') as file:
    rooms_json_data = json.load(file)

with open('students.json', 'r') as file:
    students_json_data = json.load(file)


groups_json_data = rooms_json_data


for i, room in enumerate(groups_json_data):
    groups_json_data[i]['students'] = []


for student in students_json_data:
    room_id = student['room']
    room = groups_json_data[room_id]
    room['students'].append(student)
    groups_json_data[room_id] = room


with open('groups.json', 'w') as write_file:
    json.dump(groups_json_data, write_file, indent=4)



# 5 TODO: implement different output formats

# 5.1 TODO: Implement json to xml conversion

# 6 TODO: implement cli integration support
