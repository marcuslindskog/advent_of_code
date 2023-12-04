import re

def calculate_directory_sizes(input_string):
    lines = input_string.strip().split('\n')
    file_system = parse_file_system(lines)
    directory_sizes = {}
    calculate_total_sizes(file_system, directory_sizes)
    return directory_sizes

def parse_file_system(lines):
    file_system = {}
    current_directory = file_system['/'] = {'files': {}, 'subdirectories': {}}

    for line in lines:
        if line.startswith('$'):
            continue

        match = re.match(r'^(\d+) (.+)$', line)
        if match:
            size = int(match.group(1))
            file_name = match.group(2)
            current_directory['files'][file_name] = size
        else:
            command = line.split()[0]
            if command == 'cd':
                argument = line.split()[1]
                if argument == '..':
                    current_directory = current_directory['parent']
                else:
                    current_directory = current_directory['subdirectories'][argument]

                current_directory['parent'] = current_directory.get('parent', None)
            elif command == 'dir':
                directory_name = line.split()[1]
                current_directory['subdirectories'][directory_name] = {
                    'files': {},
                    'subdirectories': {},
                    'parent': current_directory
                }

    return file_system

def calculate_total_sizes(directory, directory_sizes):
    total_size = sum(directory['files'].values())

    for subdirectory in directory['subdirectories'].values():
        total_size += calculate_total_sizes(subdirectory, directory_sizes)

    directory_sizes[directory] = total_size
    return total_size

# Example input
input_string = '''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

directory_sizes = calculate_directory_sizes(input_string)
small_directories = [directory for directory, size in directory_sizes.items() if size <= 100000]
total_size = sum(size for size in directory_sizes.values() if size <= 100000)

print("Sum of total sizes of small directories:", total_size)
