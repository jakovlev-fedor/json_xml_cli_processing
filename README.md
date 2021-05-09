# json_xml_cli_processing
**Exercising json / xml / cli operations**

- This script is meant to be executed from command line  
- It takes 2 files in json format to process  
*students.json*  
*rooms.json*  
- Sgript generates a new data model combined from these two files  
- The user can choose output format of json / xml by specifying certain flags when script execution called  

- CLI usage:  
```
usage: generate_groups.py [-h] [-f [FORMAT]] [-s [STUDENTS]] [-r [ROOMS]]

optional arguments:
  -h, --help            show this help message and exit
  -f [FORMAT], --format [FORMAT]
                        specify output format
  -s [STUDENTS], --students [STUDENTS]
                        specify students.json file path
  -r [ROOMS], --rooms [ROOMS]
                        specify rooms.json file path
```
