import argparse
import json
import xmltodict


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--format', default='json', nargs='?',
                        help='specify output format')
    parser.add_argument('-s', '--students', default='students.json', nargs='?',
                        help='specify students.json file path')
    parser.add_argument('-r', '--rooms', default='rooms.json', nargs='?',
                        help='specify rooms.json file path')
    return parser.parse_args()


def open_files(std_file_path, rms_file_path):
    print(f'Opening {rms_file_path}')
    try:
        with open(rms_file_path, 'r') as file:
            rooms_list = json.load(file)
    except FileNotFoundError as e:
        print(e)
        raise SystemExit

    print(f'Openinig {std_file_path}')
    try:
        with open(std_file_path, 'r') as file:
            students_list = json.load(file)
    except FileNotFoundError as e:
        print(e)
        raise SystemExit

    return students_list, rooms_list


def generate_groups_list(students_list, rooms_list):
    groups_list = rooms_list

    for i, room in enumerate(groups_list):
        groups_list[i]['student'] = []

    for student in students_list:
        room_id = student['room']
        room = groups_list[room_id]
        room['student'].append(student)
        groups_list[room_id] = room

    print('Combined data generated successfully')
    return groups_list


def save_as_xml(groups_list):
    """
    xmltodict module require all nodes to be a dictionary
    with single-element dict as wrapper
    so data provided need some adjustments before conversion
    """
    rooms_dict = {}
    for i, room in enumerate(groups_list):
        room_name = f'Room_{i}'
        rooms_dict[room_name] = groups_list[i]
    single_root_dict = {'root': rooms_dict}
    groups_xml_data = xmltodict.unparse(single_root_dict, pretty=True)

    print('saving to groups.xml')
    with open('groups.xml', 'w') as file:
        file.write(groups_xml_data)
    print('SUCCESS!')


def save_as_json(groups_list):
    print('saving to groups.json')
    with open('groups.json', 'w') as write_file:
        json.dump(groups_list, write_file, indent=4)
    print('SUCCESS!')


def main():
    args = get_args()
    print('use -h flag to show help')

    output_format = args.format
    students_file_path = args.students
    rooms_file_path = args.rooms

    is_json = output_format == 'json'
    is_xml = output_format == 'xml'

    if not (is_json or is_xml):
        print(f'{output_format} format is not supported yet')
        raise SystemExit

    students_list, rooms_list = open_files(students_file_path, rooms_file_path)
    groups_list = generate_groups_list(students_list, rooms_list)

    if is_xml:
        save_as_xml(groups_list)
    if is_json:
        save_as_json(groups_list)


if __name__ == '__main__':
    main()
